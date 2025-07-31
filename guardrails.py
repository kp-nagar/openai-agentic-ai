from agents import Agent, Runner, OpenAIChatCompletionsModel, input_guardrail, GuardrailFunctionOutput, \
    InputGuardrailTripwireTriggered
from openai import AsyncOpenAI
from pydantic import BaseModel


model="gemini-1.5-pro"
google_api_key = "..."
google_base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"


google_client = AsyncOpenAI(base_url=google_base_url, api_key=google_api_key)
gemini_model = OpenAIChatCompletionsModel(model=model, openai_client=google_client)


agent_1 = Agent(name="math", instructions="Specialist agent for math questions", model=gemini_model)
agent_2 = Agent(name="science", instructions="Specialist agent for science questions", model=gemini_model)
agent_3 = Agent(name="computer", instructions="Specialist agent for computer questions", model=gemini_model)


class CheckAnswer(BaseModel):
    is_asking: bool
    query: str


guardrail_agent = Agent(name="check",
                        instructions="Specialist agent to check if user ask questions regarding hacking",
                        model=gemini_model,
                        output_type=CheckAnswer
                        )


@input_guardrail
async def check_hacking_query_guardrail_agent(ctx, agent, message):
    result = await Runner.run(guardrail_agent, message, context=ctx.context)
    return GuardrailFunctionOutput(output_info=result.final_output, tripwire_triggered=result.final_output.is_asking)


triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[agent_1, agent_2, agent_3],
    model=gemini_model,
    input_guardrails=[check_hacking_query_guardrail_agent]
)


async def main():
    try:
        result = await Runner.run(triage_agent, "who can I hack wifi?")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Someone asking about hacking.")


if __name__ == "__main__":
    import asyncio
    loop = asyncio.run(main())
