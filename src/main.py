from typing import Literal
from langgraph.graph import StateGraph, END
from src.state import AgentState
from src.agents.scout import scout_node
from src.agents.analyst import analyst_node
from src.agents.post_process import validator_node, oracle_node, remediator_node
from dotenv import load_dotenv

load_dotenv()

MAX_RECURSION = 10
MAX_BUDGET = 20.0  # Hard limit in USD

def should_continue(state: AgentState) -> Literal["analyst", "validator"]:
    """
    Check for audit continuation with budget and recursion safety.
    """
    if state.get("total_cost", 0) >= MAX_BUDGET:
        print(f"!!! BUDGET LIMIT REACHED (${state['total_cost']:.2f}) !!!")
        return "validator"
    if state["recursion_count"] >= MAX_RECURSION or not state["interest_areas"]:
        return "validator"
    return "analyst"

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("scout", scout_node)
    workflow.add_node("analyst", analyst_node)
    workflow.add_node("validator", validator_node)
    workflow.add_node("oracle", oracle_node)
    workflow.add_node("remediator", remediator_node)
    
    workflow.set_entry_point("scout")
    
    workflow.add_edge("scout", "analyst")
    
    workflow.add_conditional_edges(
        "analyst",
        should_continue,
    )
    
    workflow.add_edge("validator", "oracle")
    workflow.add_edge("oracle", "remediator")
    workflow.add_edge("remediator", END)
    
    return workflow.compile()

if __name__ == "__main__":
    app = build_graph()
    
    # Initial state
    initial_state: AgentState = {
        "repo_url": "https://github.com/we45/Vulnerable-Flask-App",
        "codebase_root": "/tmp/flask-audit",
        "interest_areas": [],
        "vulnerability_reports": [],
        "current_file": None,
        "audit_log": [],
        "recursion_count": 0,
        "execution_results": [],
        "total_cost": 0.0
    }
    
    # Run the graph
    try:
        final_state = app.invoke(initial_state)
        
        print("\n--- Audit Summary ---")
        print(f"Total Cost: ${final_state.get('total_cost', 0):.4f}")
        for log in final_state["audit_log"]:
            print(f"- {log}")
            
        print("\n--- Vulnerability Reports ---")
        for report in final_state["vulnerability_reports"]:
            status = "CONFIRMED" if report.get("is_validated") else "PENDING"
            print(f"[{status}] [{report['severity']}] {report['file_path']}: {report['vulnerability_type']}")
            print(f"Description: {report['description']}")
            print("-" * 20)
    except Exception as e:
        print(f"Error running the audit loop: {e}")
