# Online Fashion Shopping Agent - README

## Overview
The **Online Fashion Shopping Agent** is an AI-powered virtual assistant designed to help users navigate multiple fashion e-commerce platforms efficiently. It interprets user requests, determines the appropriate tools to use, and integrates relevant data to provide a structured and helpful response.

## Features
- **Product Search**: Finds products based on specified attributes (name, color, price, size).
- **Shipping Estimation**: Determines shipping feasibility and estimated arrival time.
- **Discount Application**: Validates and applies promo codes to adjust prices.
- **Price Comparison**: Compares product prices across multiple e-commerce platforms.
- **Return Policy Check**: Retrieves return policy details from different stores.

---

## Comparative Conceptual Map
| Methodology | Strengths | Weaknesses |
|------------|-----------|------------|
| **ReAct** | Uses reasoning and action steps iteratively | Slower due to iterative execution |
| **Toolformer** | API calling for enhanced external capabilities | Limited decision-making ability |
| **Chain of Tools** | Structured tool execution for complex workflows | Requires well-defined task dependencies |
| **LATS** | Tree search planning for efficient decision-making | High computational cost |
| **ReST Meets ReAct** | Continuous learning via reinforcement | Needs large datasets for optimal training |

---

## Short Written Analysis
The agent applies **structured reasoning** to select the best tool for each query. Compared to other approaches:
- **ReAct** is useful for step-by-step decision-making.
- **Toolformer** enables API-based querying.
- **Chain of Tools** supports structured workflows.
- **LATS** is more efficient for complex decision-heavy tasks.
- **ReST Meets ReAct** improves over time with reinforcement learning.

Our agent aligns most closely with **ReAct**, as it follows an **iterative reasoning-action flow**.

---

## Design Decisions
### **Agent Architecture & Tool Selection**
1. **Reasoning Module**: Determines the relevant tool(s) based on keywords in the query.
2. **Tool Calls**: Executes the appropriate tool with extracted parameters.
3. **Observation & Integration**: Combines tool outputs into a structured final response.

### **Prompt Structure**
- **System Prompt**: Defines the assistant’s role and available tools.
- **User Queries**: Provides structured user inputs.
- **Agent Output**: Ensures logical reasoning and action steps.

---

## Challenges & Improvements
### **Challenges Faced**
- Handling ambiguous queries with **missing details**.
- Extracting structured parameters **from natural language**.
- Ensuring smooth **multi-tool execution**.

### **Improvements**
- Enhanced **query parsing with regex** for better keyword extraction.
- Implemented **multi-turn reasoning** to handle complex requests.
- Optimized **tool selection logic** for more precise actions.

---

## Open Questions & References
### **Open Questions**
- Can the agent handle **conversational multi-turn interactions** effectively?
- How can it **improve contextual awareness** over multiple queries?
- Could **LLM fine-tuning** improve its decision-making?

### **References**
1. **ReAct: Synergizing Reasoning and Acting in Language Models** *(Yao et al., 2022)*.
2. **Toolformer: Language Models Can Teach Themselves to Use Tools** *(Schick et al., 2023)*.
3. **Chain of Tools: Integrating APIs for Complex Reasoning** *(OpenAI Research, 2023)*.
4. **LATS: Language Agent Tree Search for Decision Making** *(DeepMind, 2022)*.
5. **ReST Meets ReAct: Enhancing LLMs with Reinforcement Learning** *(Meta AI, 2023)*.

---

## Running the Agent
1. **Clone the Repository**:
   ```bash
   git clone <repo_url>
   cd online-shopping-agent
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Agent**:
   ```bash
   python agent.py
   ```

This will execute **predefined demonstration tasks** to showcase the agent’s capabilities.

---

## Contribution
Feel free to contribute improvements! Open an issue or submit a pull request on GitHub.

---

**Developed by:** Bonala Rahul 
**Date:** 2025

