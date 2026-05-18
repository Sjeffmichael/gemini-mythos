# Gemini Mythos: Project Specification & Strategy (v8)

## 1. Project Mission Statement
**Project Name:** Gemini Mythos
**Team:** Invencible
**The Core Thesis:** Replicating the frontier cybersecurity capabilities of **Anthropic’s Mythos** by applying the **"Jagged Frontier"** philosophy proposed by **Aisle**.

While Anthropic focuses on the raw power of a single frontier model, Gemini Mythos proves that the "moat" is the **system**, not just the model. By orchestrating **Gemini 2.5 Pro**, **Gemini 2.5 Flash**, and **Gemini 3.1 Flash Lite** within an always-on governance scaffold, we aim to match—and in false-positive discrimination, exceed—the results of frontier-scale autonomous cybersecurity agents.

---

## 2. Competition Context: TechEx 2026
**Hackathon:** [TechEx Intelligent Enterprise Solutions](https://lablab.ai/ai-hackathons/techex-intelligent-enterprise-solutions-hackathon)
**Primary Tracks:**
* **Track 1: Agent Security & AI Governance (Powered by Veea):** All agent traffic is forced through **Veea Lobster Trap** to enforce P4-style firewall rules, providing a total audit trail of autonomous intent.
* **Track 2: AI Agents with Google AI Studio:** We leverage the **Gemini 2.5 Pro** model's context window to ingest entire enterprise repositories for deep-logic auditing.

---

## 3. The "Aisle" Approach to Mythos
**Reference Article:** [AI Cybersecurity after Mythos: The Jagged Frontier (Aisle)](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)

**Key Philosophy Points:**
1.  **Jagged Capabilities:** Using **Gemini 3.1 Flash Lite** for ultra-fast broad-spectrum scanning, **Gemini 2.5 Pro** for complex mathematical reasoning, and **Gemini 2.5 Flash** for reliable validation.
2.  **The Scaffold is the Moat:** The value lies in the targeting, iterative deepening, and the validation loop.
3.  **Maintainer Trust:** We prioritize "False Positive Discrimination," ensuring that vulnerabilities reported are logically sound and reproducible.

---

## 4. Technical Architecture: The Five-Stage Pipeline

| Stage | Model Role | Official Model ID | Purpose |
| :--- | :--- | :--- | :--- |
| **Stage 1** | **The Scout** | `gemini-3.1-flash-lite` | Rapidly maps the attack surface and entry points. |
| **Stage 2** | **The Analyst** | `gemini-2.5-pro` | Deep-logic audit of integer arithmetic and state logic. |
| **Stage 3** | **The Validator** | `gemini-2.5-flash` | Peer-reviews findings to eliminate false positives. |
| **Stage 4** | **The Oracle** | `gemini-2.0-flash-lite` | Generates and executes a PoC script in a sandbox. |
| **Stage 5** | **The Remediator** | `gemini-2.5-flash` | Generates side-by-side patches and unit tests. |

---

## 5. Innovation Differentiators
*   **1M Context "Full-Brain" Audit:** Feed the entire repository into Gemini 2.5 Pro for cross-file logic auditing to catch vulnerabilities that chunked-RAG systems miss.
*   **Autonomous Exploit Oracle:** The system generates a **Python/Bash PoC script** and verifies it in real-time within a sandboxed environment.
*   **Always-On Governance:** Every prompt and response is proxied through **Veea Lobster Trap**. Governance is not optional; there is no opt-out checkbox, ensuring a 100% audit trail.
*   **Financial Control:** Integrated usage of **Google AI Studio Spend Caps** to manage high-performance reasoning costs without risking over-usage.

---

## 6. Public Interface: The "Sentinel" Dashboard
Designed in Streamlit as a high-density, innovative command center for enterprise security.

### 6.1 UI Components
*   **Multi-Stage Progress Tracker (`st.status`):** Visualizes the real-time transition between Scout, Analyst, Validator, and Oracle agents.
*   **The "Jagged Frontier" Radar:** A Plotly-powered radar chart showing Gemini Mythos’s performance across multiple vectors (Memory Safety, Logic, Auth, Math) vs. standard scanners.
*   **Tabbed Intelligence Center:**
    * **Dashboard:** Executive high-level scoring, "Jagged Frontier" radar, and vulnerability trends.
    * **Audit Terminal:** Real-time stream of agent reasoning logs and Veea rule enforcement (P4-style) badges.
    * **Remediations:** Side-by-side interactive "Diff" view for code remediation and patch verification.
    * **Proof of Concept:** Downloadable reproduction script and real-time terminal output from the Oracle sandbox.

---

## 7. Deployment Strategy
*   **Backend:** Dockerized Python logic hosted on **Railway.app**.
*   **Frontend:** **Streamlit Cloud** for the public dashboard.
*   **Governance Proxy:** Forced routing through **Lobster Trap** managed service (port 8081) using **GOOGLE_API_KEY** for secure authentication.

---

## 8. Development Workflow (For Gemini CLI)

### Task 1: The "Sentinel" UI Skeleton
> "Generate a Streamlit dashboard with a professional dark theme and a sidebar including a GitHub URL input and a mandatory 'Governance Pulse' status light. In the main area, create four tabs: Summary, Analyst Reasoning, Remediation, and Veea Audit Logs. Add a placeholder for a Radar Chart using plotly."

### Task 2: The Agentic Progress Loop
> "Write a Python function using st.status that updates the UI as it iterates through a LangGraph state machine, calling **gemini-3.1-flash-lite** for scanning and **gemini-3.1-pro-preview** for deep analysis, with real-time logging to the 'Analyst Reasoning' tab."

### Task 3: The Validator Agent Prompt
> "Create a system prompt for **gemini-3.1-pro-preview** that acts as a skeptical senior security engineer. It receives a vulnerability report and must attempt to prove the bug is a false positive based on current code constraints."