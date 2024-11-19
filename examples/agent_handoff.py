from dotenv import load_dotenv

assert load_dotenv()

from swarm import Agent, Swarm

client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
)

unknown_language_agent = Agent(
    name="Unknown Language Agent",
    instructions="You speak giberish to try and communicate with all other languages, don't reply in the language that you are spoken to in, instead make up giberish like: 'fadoi;j io;afji;fda j;i'. But don't use this exact string",
)


def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent


def transfer_to_unknown_language_agent():
    """Any language outside of supported ones are transfered here"""
    return unknown_language_agent


english_agent.functions.append(transfer_to_spanish_agent)
english_agent.functions.append(transfer_to_unknown_language_agent)

messages = [{"role": "user", "content": "Bonjour monsieur"}]
response = client.run(agent=english_agent, messages=messages)

print(response.messages[-1]["content"])
