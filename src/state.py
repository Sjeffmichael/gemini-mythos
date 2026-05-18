from typing import List, TypedDict, Optional

class VulnerabilityReport(TypedDict):
    file_path: str
    vulnerability_type: str
    description: str
    severity: str
    reproduction_steps: Optional[str]
    is_validated: bool
    poc_script: Optional[str]
    execution_output: Optional[str]
    patch_diff: Optional[str]
    validation_tests: Optional[str]

class AgentState(TypedDict):
    repo_url: Optional[str]
    codebase_root: str
    interest_areas: List[str]
    vulnerability_reports: List[VulnerabilityReport]
    current_file: Optional[str]
    audit_log: List[str]
    recursion_count: int
    execution_results: List[str]
    total_cost: float
