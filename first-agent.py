from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai import AsyncOpenAI


model="gemini-1.5-pro"
google_api_key = "..."
google_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"


google_client = AsyncOpenAI(base_url=google_base_url, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model=model, openai_client=google_client)

agent = Agent(name="story teller", instructions="You are a story teller", model=gemini_model)


result = Runner.run_sync(agent, "Tell me a story about a brave knight and a dragon.")
print(result.final_output)
