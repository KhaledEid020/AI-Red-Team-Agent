### Goal

Create an AI agent that leverages a Supervisor architecture for automated penetration testing activities with the following technical features:

- The Supervisor must convert the security assessment objective into a structured **TODO list**.
- The Supervisor must **dynamically** create specialized **sub-agents** and assign each sub-agent specific tools to use.
- The Supervisor and sub-agents must have access to the following tools: `read_file`, `write_file`, and `edit_file` for **context engineering** support.
---
### Approach

To achieve our goal, the best approach to use is using **Deep Agents** which built on **Langchain** and **Langgraph** frameworks.

* Deep agent will allow us to create and manage structured task lists for tracking progress through complex workflows using built in tool called **write_todos**.
* It will also dynamically launch ephemeral subagents for complex and independent tasks ysing built in tool called **task**.
* It have Filesystem Tools such as **ls**, **read_file**, **write_file**, **edit_file**, **glob** and **grep**.

---

### Infrastructure Overview

In this POC, we will use a **real infrastructure** instead of dummy ones, and by the end, we will see **real-world results**.

![Nua](https://github.com/user-attachments/assets/3a38a57d-1582-4c3c-b0ce-bae7db79538f)

---

As illustrated in the image above, we set up the following:
* Local SLM Qwen3-8B-AWQ using vLLM, we use local and not cloud model for data confidently in domain like Cybersecurity. The local LLM will be available at http://localhost:8000/v1

* **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** Pentest MCP server, which will beavailable at http://localhost:5050/mcp
---
### Deep Agent Architecture Overview

![Nua-Copy of Infra](https://github.com/user-attachments/assets/a88182de-95da-4526-9744-9fec0b362687)

---
### How the Agent Works

1. The user will request: “Perform a comprehensive security assessment of my web application at http://testphp.vulnweb.com”, which is a deliberately vulnerable website used for testing purposes.
2. The Supervisor will plan the assessment by using available MCP tools to transform this objective into a structured TODO list.
3. The Supervisor will create a sub-agent for each task and assign a specific MCP tool to it.
4. Each sub-agent will perform its assigned task, invoke the designated tool, and return the results to the Supervisor node. 
5. The Supervisor will adjust the TODO list accordingly, if needed, until the objective is completed.


The screenshot below shows what the Supervisor thinks after the user enters the prompt.

<p align="left">
  <img 
    src="https://github.com/user-attachments/assets/ec1a8252-a9ce-4ea2-91ef-34c7aaa0caac"
    alt="Supervisor reasoning after user prompt submission"
    width="700"
  />
</p>

<p align="left">
  <em>Figure 1: Supervisor’s reasoning flow after the user submits a prompt.</em>
</p>


<img width="1044" height="443" alt="image" src="https://github.com/user-attachments/assets/79636b53-b115-424f-b6c7-42c1f1e06302" />

<img width="1043" height="389" alt="image" src="https://github.com/user-attachments/assets/a02003bc-e7c9-4fb8-a93f-9ac6f91a29b1" />

<img width="1037" height="425" alt="image" src="https://github.com/user-attachments/assets/eac44f10-e891-4a15-b81f-a1c4c6ae722b" />

<img width="1036" height="438" alt="image" src="https://github.com/user-attachments/assets/585e400a-30e8-49fe-88af-fa7a31603ae4" />


and so on...


Also, we connect the agent with LangSmith as shown below.

<img width="1073" height="489" alt="image" src="https://github.com/user-attachments/assets/f52d0e01-b9a5-4d3a-a733-190ebca45735" />
