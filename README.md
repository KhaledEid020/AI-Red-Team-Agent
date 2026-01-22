### Goal

Create an AI agent that leverages a Supervisor architecture for automated penetration testing activities with the following technical features:

- The Supervisor must convert the security assessment objective into a structured **TODO list**.
- The Supervisor must **dynamically** create specialized **sub-agents** and assign each sub-agent specific tools to use.
- The Supervisor and sub-agents must have access to the following tools: `read_file`, `write_file`, and `edit_file` for **context engineering** support.

### Approach

To achieve our goal, the best approach to use is using **Deep Agents** which built on **Langchain** and **Langgraph** frameworks.

* Deep agent will allow us to create and manage structured task lists for tracking progress through complex workflows using built in tool called **write_todos**.
* It will also dynamically launch ephemeral subagents for complex and independent tasks ysing built in tool called **task**.
* It have Filesystem Tools such as **ls**, **read_file**, **write_file**, **edit_file**, **glob** and **grep**.

In this POC, we will use a **real infrastructure** instead of dummy ones, and by the end, we will see **real-world results**.

![[Nua.jpg]]

As illustrated in the image above, we set up the following:
* Local SLM Qwen3-8B-AWQ using vLLM, we use local and not cloud model for data confidently in domain like Cybersecurity. The local LLM will be available at http://localhost:8000/v1

* **[hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)** Pentest MCP server, which will beavailable at http://localhost:5050/mcp


### Deep Agent Architecture Overview


![[Nua-Copy of Infra.jpg]]

### How the Agent Works

![[Pasted image 20260122141319.png]]

![[Pasted image 20260122141442.png]]

![[Pasted image 20260122141736.png]]

![[Pasted image 20260122141836.png]]

![[Pasted image 20260122142100.png]]

and so on...


Also, we connect the agent with LangSmith as shown below.

![[LangSmith.png]]
