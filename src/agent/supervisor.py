import asyncio
import logging
import os
import sys
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent
from deepagents.backends import FilesystemBackend

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# --- Configuration ---
INFERENCE_SERVER_URL = "http://localhost:8000/v1"
MCP_SERVER_URL = "http://localhost:5050/mcp"
base_dir = os.path.dirname(os.path.abspath(__file__))

# --- LLM Setup ---
llm = ChatOpenAI(
    model="Qwen/Qwen3-8B-AWQ",
    openai_api_key="lm-studio",
    openai_api_base=INFERENCE_SERVER_URL,
    temperature=0,
)

async def initialize_agent():
    print("--- Connecting to MCP Server and getting tools ---")
    client = MultiServerMCPClient({
        "opensearch": {
            "transport": "http",
            "url": MCP_SERVER_URL,
        }
    })
    tools = await client.get_tools()
    
    print("\n--- Initializing Security Supervisor Agent ---")

    # Create the Deep Agent using your AGENTS.md instructions
    agent = create_deep_agent(
        model=llm,
        tools=tools,
        memory=["../AGENTS.md"],                       # Agent identity and general instructions
        skills=["../skills/"],
        backend=FilesystemBackend(root_dir=base_dir)  # Persistent file storage
    )

    if __name__ == "__main__":
        print("\n=== STARTING SECURITY ASSESSMENT (STREAMING) ===\n")
        
        input_data = {
            "messages": [
                {"role": "user", "content": "Perform a comprehensive security assessment of my web application at http://testphp.vulnweb.com"},
            ]
        }

        # This loop catches events as they happen in the background
        async for event in agent.astream_events(input_data, version="v2"):
            kind = event["event"]

            # 1. SHOW THE AGENT'S THOUGHTS (Chat tokens)
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    # print the "thinking" word by word
                    print(content, end="", flush=True)

            # 2. SHOW WHEN A TOOL STARTS (e.g., Recon, SQLi checks)
            elif kind == "on_tool_start":
                print(f"\n\n[ACTION]: Calling tool '{event['name']}'...")
                print(f"[INPUT]: {event['data'].get('input')}")

            # 3. SHOW WHEN A TOOL FINISHES
            elif kind == "on_tool_end":
                print(f"\n[RESULT]: Tool '{event['name']}' finished execution.")
                print("-" * 30 + "\n")

        print("\n=== ASSESSMENT COMPLETE ===")

    # Crucial for LangGraph: Return the agent object to the graph variable
    return agent

# --- LANGGRAPH EXPORT ---
# LangGraph Studio looks for this 'graph' variable
graph = asyncio.run(initialize_agent())

if __name__ == "__main__":
    pass
