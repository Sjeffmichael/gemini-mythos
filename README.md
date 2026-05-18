# 🛡️ Gemini Mythos

**Team:** Invencible  
**Hackathon:** [TechEx Intelligent Enterprise Solutions](https://lablab.ai/ai-hackathons/techex-intelligent-enterprise-solutions-hackathon)  
**Primary Tracks:** 
1. Agent Security & AI Governance (Powered by Veea)
2. AI Agents with Google AI Studio

---

## 📖 The Core Thesis

Replicating the frontier cybersecurity capabilities of **Anthropic’s Mythos** by applying the **"Jagged Frontier"** philosophy. 

While Anthropic focuses on the raw power of a single frontier model, **Gemini Mythos** proves that the "moat" is the **system**, not just the model. By orchestrating a multi-agent pipeline using a mix of **Gemini 2.5 Pro**, **Gemini 2.5 Flash**, and **Gemini Flash Lite** models within an always-on governance scaffold, we aim to match—and in false-positive discrimination, exceed—the results of frontier-scale autonomous cybersecurity agents.

---

## 🚀 Technical Architecture: The Five-Stage Pipeline

We utilize LangGraph to orchestrate a deterministic, 5-stage state machine that balances reasoning depth with API cost and speed.

| Stage | Agent Role | Gemini Model | Purpose |
| :--- | :--- | :--- | :--- |
| **1** | **The Scout** | `gemini-3.1-flash-lite` | Ultra-fast mapping of the attack surface. Identifies files handling untrusted input, auth, and memory management. |
| **2** | **The Analyst** | `gemini-2.5-pro` | Performs a "Full-Brain" deep-logic audit across batches of files to catch complex, cross-file vulnerabilities (e.g., SSRF, Prompt Injection, RCE). |
| **3** | **The Validator** | `gemini-2.5-flash` | Acts as the Skeptical "Devil's Advocate". Peer-reviews findings to eliminate false positives and ensure the logic flaw is genuinely exploitable at the code level. |
| **4** | **The Oracle** | `gemini-2.0-flash-lite` | The Autonomous Exploit Oracle. Generates a Python Proof-of-Concept (PoC) script and executes it in a sandboxed environment to empirically prove the exploit. |
| **5** | **The Remediator** | `gemini-2.5-flash` | Generates a secure, Git-compatible patch (Diff) and validation unit tests. |

---

## 🌟 Innovation Differentiators

*   **1M Context "Full-Brain" Audit:** Feeds entire repositories into Gemini 2.5 Pro for cross-file logic auditing to catch vulnerabilities that traditional chunked-RAG systems miss.
*   **Autonomous Exploit Oracle:** The system doesn't just guess; it generates a PoC script and verifies the vulnerability in real-time within a sandboxed execution environment.
*   **Always-On Governance (Veea):** Every prompt and response is proxied through a **Veea Lobster Trap** managed proxy (running locally on port 8081). Governance is not optional; there is no opt-out checkbox, ensuring a 100% audit trail of autonomous agent intent.
*   **Targeted Model Allocation:** Cost and speed are optimized by mapping the right model to the right task, avoiding global rate-limit bottlenecks.

---

## 💻 Public Interface: The "Sentinel" Dashboard

Designed in Streamlit as a high-density command center for enterprise security:
*   **Live Multi-Stage Tracker:** Visualizes the real-time transition across the LangGraph state machine.
*   **"Jagged Frontier" Radar Chart:** Plotly-powered executive comparison of Gemini Mythos vs. standard SAST scanners.
*   **Interactive Tabs:**
    *   **Summary:** Executive metrics and confirmed vulnerability dataframe.
    *   **Analyst Reasoning:** A real-time terminal stream of the AI's internal thought process.
    *   **Remediation & PoC:** Side-by-side view of the generated patch, unit tests, and sandbox execution logs.
    *   **Veea Audit Logs:** The intercepted network payloads and governance metadata from the Lobster Trap proxy.

---

## 🛠️ Setup & Local Development

### Prerequisites
*   Docker and Docker Compose
*   Google AI Studio API Key (`GOOGLE_API_KEY`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/gemini-mythos.git
    cd gemini-mythos
    ```

2.  **Configure Environment:**
    Create a `.env` file in the root directory and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_api_key_here
    ```

3.  **Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    This will start:
    *   The **Lobster Trap Proxy** on `http://localhost:8081`
    *   The **Sentinel Dashboard** on `http://localhost:8501`

4.  **Access the Application:**
    Open your browser and navigate to `http://localhost:8501`. 
    
    *For a demonstration, enter the following repository URL and click **Start Deep Audit**:*
    `https://github.com/vulnerable-apps/damn-vulnerable-MCP-server`

---
*Built for the TechEx Intelligent Enterprise Solutions Hackathon - 2026*
