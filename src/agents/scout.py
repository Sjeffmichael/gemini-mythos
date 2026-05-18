import os
from typing import List
from langchain_openai import ChatOpenAI
from src.state import AgentState
from pydantic import BaseModel, Field
from src.utils.cost import calculate_cost

class ScoutFindings(BaseModel):
    interesting_files: List[str] = Field(description="List of file paths that require deep audit.")
    reasoning: str = Field(description="Explanation for why these files were selected.")

def scout_node(state: AgentState) -> AgentState:
    """
    Scout Agent:
    Identifies high-risk files. Traffic is routed through Lobster Trap for governance.
    """
    model_name = "gemini-3.1-flash-lite"
    
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("CRITICAL ERROR: GOOGLE_API_KEY is not set in the environment variables.")

    llm = ChatOpenAI(
        model=model_name, 
        openai_api_key=api_key,
        base_url="http://localhost:8081/v1",
        extra_body={
            "_lobstertrap": {
                "declared_intent": "code_discovery",
                "agent_id": "scout-v1"
            }
        }
    )
    structured_llm = llm.with_structured_output(ScoutFindings)
    
    codebase_root = state.get("codebase_root", ".")
    
    files = []
    for root, _, filenames in os.walk(codebase_root):
        for f in filenames:
            rel_path = os.path.relpath(os.path.join(root, f), codebase_root)
            if not any(ignored in rel_path for ignored in ["node_modules", ".git/", "__pycache__"]):
                files.append(rel_path)
    
    file_list_str = "\n".join(files[:500]) # Increased for Aisle benchmarks
    
    prompt = f"""
    You are a Security Scout. Your goal is to identify files in the codebase that handle:
    1. Untrusted network input
    2. Memory management (especially in C/C++)
    3. Authentication or Authorization logic
    4. Data parsing (XML, JSON, custom binary formats)
    
    Codebase structure:
    {file_list_str}
    
    Identify the top priority files for a deep security audit.
    """
    
    try:
        # Use full response to get token usage
        response = llm.invoke(prompt)
        findings = structured_llm.invoke(prompt) # Structured output doesn't always return usage in this SDK version easily
        
        # Estimate usage (Structured output is a second call usually, but let's approximate)
        # Note: In production, we'd use a single response with tool_calls
        input_tokens = len(prompt) // 4
        output_tokens = 500
        cost = calculate_cost(model_name, input_tokens, output_tokens)
        
        log_entry = f"Scout identified {len(findings.interesting_files)} files: {findings.reasoning}"
    except Exception as e:
        log_entry = f"Scout request intercepted/failed: {str(e)}"
        return {
            "interest_areas": [],
            "audit_log": state.get("audit_log", []) + [log_entry],
            "total_cost": state.get("total_cost", 0)
        }
    
    return {
        "interest_areas": findings.interesting_files,
        "audit_log": state.get("audit_log", []) + [log_entry],
        "total_cost": state.get("total_cost", 0) + cost
    }
