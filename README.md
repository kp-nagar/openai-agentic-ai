# openai-agentic-ai

```
Agents - Represent LLMs

Handoffs - represent interactions

Guardrails - represent controls
```

### Three steps
- Create an instance of Agent.
- Use with trace() to trace the agent.
- call runner.run() run the agent.

## 🔧 Tools

✅ What are Tools?

Tools are external capabilities that agents can use to complete a task they couldn't do alone. These tools are usually functions, APIs, or systems the agent can call.

### 🧠 Think of them as:

“I’m an AI agent. If I can’t answer directly, I’ll call a tool to help me — like a calculator, code interpreter, or web search.”

### 📌 Examples:

Function Calling in OpenAI's Assistants API

code_interpreter, retrieval, functions

Calling external tools via LangChain or CrewAI (tool=WeatherAPI, tool=SearchDocs, etc.)

Internal Python functions (e.g. def get_stock_price(ticker): ...)

### 🧪 When to use:

- For data retrieval

- Math computations

- Database lookups

- Custom business logic


## 🤝 Handoffs

✅ What are Handoffs?

Handoffs are when one agent passes control or context to another agent. It’s like a relay race — Agent A does part of the task, then hands over to Agent B.

### 🧠 Think of them as:

“I’ve done my part. Now this part of the task is best handled by someone else.”

### 📌 Examples:

Agent 1: "Math Expert" → Agent 2: "Explanation Writer"

In LangGraph: a node decides to hand off to a different agent node

In CrewAI: task transitions to another agent in sequence

In RAG systems: Extractor Agent → Validator Agent → Formatter Agent

### 🧪 When to use:
- For multi-role workflows

- When specialized agents collaborate

- When agents operate sequentially or hierarchically


| Concept      | Tools                                | Handoffs                                   |
| ------------ | ------------------------------------ | ------------------------------------------ |
| Purpose      | Extend agent capabilities            | Delegate part of the task to another agent |
| Involves     | Functions, APIs, models              | Multiple agents                            |
| Triggered by | Agent not having internal capability | Task workflow design                       |
| Used in      | OpenAI Assistants, LangChain, CrewAI | CrewAI, LangGraph, multi-agent systems     |
| Example      | Code interpreter, file search        | Math Agent → Report Agent                  |


