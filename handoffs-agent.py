from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI


model="gemini-1.5-pro"
google_api_key = "..."
google_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"


google_client = AsyncOpenAI(base_url=google_base_url, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model=model, openai_client=google_client)


agent_1 = Agent(name="math", instructions="Specialist agent for math questions", model=gemini_model)
agent_2 = Agent(name="science", instructions="Specialist agent for science questions", model=gemini_model)
agent_3 = Agent(name="computer", instructions="Specialist agent for computer questions", model=gemini_model)


triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[agent_1, agent_2, agent_3],
    model=gemini_model
)


result = Runner.run_sync(triage_agent, "What is the 2+2?")
print(result.final_output)
