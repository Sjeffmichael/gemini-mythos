import os
from typing import List, Optional
from langchain_openai import ChatOpenAI
from src.state import AgentState, VulnerabilityReport
from pydantic import BaseModel, Field
from src.utils.cost import calculate_cost

class AuditResult(BaseModel):
    has_vulnerability: bool
    vulnerability_type: Optional[str]
    description: Optional[str]
    severity: Optional[str]
    reproduction_steps: Optional[str]

def analyst_node(state: AgentState) -> AgentState:
    """
    Analyst Agent (Gemini Pro):
    Performs deep-context reasoning on multiple related files to find cross-file flaws.
    """
    if not state["interest_areas"]:
        return {"audit_log": state["audit_log"] + ["Analyst found no files to audit."]}
    
    # In "S-Class" mode, we audit a batch of files to find cross-file logic bugs
    current_batch = state["interest_areas"][:5] # Batch of 5 files for deep context
    remaining_files = state["interest_areas"][5:]
    
    model_name = "gemini-2.5-pro" # Switched to 2.5 Pro for deep reasoning with better rate limits
    llm = ChatOpenAI(
        model=model_name,
        openai_api_key=os.getenv("GOOGLE_API_KEY"),
        base_url="http://localhost:8081/v1",
        extra_body={
            "_lobstertrap": {
                "declared_intent": "cross_file_logic_audit",
                "declared_paths": current_batch,
                "agent_id": "analyst-pro-v1"
            }
        }
    )
    structured_llm = llm.with_structured_output(AuditResult)
    
    codebase_root = os.path.abspath(state.get("codebase_root", "."))
    
    batch_content = ""
    for file_path in current_batch:
        full_path = os.path.abspath(os.path.join(codebase_root, file_path))
        try:
            with open(full_path, "r") as f:
                batch_content += f"\n--- FILE: {file_path} ---\n{f.read()}\n"
        except Exception as e:
            batch_content += f"\n--- FILE: {file_path} (FAILED TO READ: {e}) ---\n"

    prompt = f"""
    You are a Senior Security Auditor (Mythos Level). 
    Perform a DEEP CONTEXT audit on this batch of files. 
    Look for CROSS-FILE logic vulnerabilities, race conditions, and complex state machine flaws.
    
    BATCH FILES:
    {batch_content}
    
    Identify high-confidence "Jagged Frontier" vulnerabilities that span these files.
    """
    
    try:
        result = structured_llm.invoke(prompt)
        cost = calculate_cost(model_name, len(batch_content)//4, 1000)
    except Exception as e:
        return {
            "interest_areas": remaining_files,
            "audit_log": state["audit_log"] + [f"Analyst Pro audit of batch {current_batch} failed: {str(e)}"],
            "recursion_count": state.get("recursion_count", 0) + 1
        }
    
    new_reports = list(state.get("vulnerability_reports", []))
    if result.has_vulnerability:
        report: VulnerabilityReport = {
            "file_path": ", ".join(current_batch),
            "vulnerability_type": result.vulnerability_type,
            "description": result.description,
            "severity": result.severity,
            "reproduction_steps": result.reproduction_steps,
            "is_validated": False,
            "poc_script": None,
            "patch_diff": None
        }
        new_reports.append(report)
        log_msg = f"Analyst Pro found {result.severity} cross-file vulnerability in {current_batch}: {result.vulnerability_type}"
    else:
        log_msg = f"Analyst Pro audited batch {current_batch} and found no cross-file vulnerabilities."
    
    return {
        "interest_areas": remaining_files,
        "vulnerability_reports": new_reports,
        "audit_log": state["audit_log"] + [log_msg],
        "recursion_count": state.get("recursion_count", 0) + 1,
        "total_cost": state.get("total_cost", 0) + cost
    }
