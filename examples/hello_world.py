from dotenv import load_dotenv

assert load_dotenv()
from swarm import Agent, Swarm

client = Swarm()


def transfer_to_agent_b():
    return agent_b


agent_a = Agent(
    name="Agent A",
    instructions="You are a helpful agent.",
    functions=[transfer_to_agent_b],
)

agent_b = Agent(
    name="Agent B",
    instructions="Only speak in Haikus.",
)

response = client.run(
    agent=agent_a,
    messages=[{"role": "user", "content": "I want to talk to smell funny."}],
)

print(response.messages[-1]["content"])
