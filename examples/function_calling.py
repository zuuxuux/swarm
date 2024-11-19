import requests

from swarm import Agent, Swarm

client = Swarm()


def get_weather(location) -> str:
    print(location)
    return "{'temp':67, 'unit':'F'}"


def get_ip():
    # Using a public API to get external IP
    response = requests.get("https://api.ipify.org")
    return response.text


location_getter_agent = Agent(
    name="Location getter",
    instructions="You have to get the user's location. You must return a location, your best guess location. Even if you can't determine by IP address, you must make a best guess. Don't say you don't know",
    functions=[get_ip],
)


def transfer_to_location_getter_agent():
    """Gets the location getter agent, good when you need to know user's location"""
    return location_getter_agent


agent = Agent(
    name="Agent",
    instructions="You are a helpful agent. Return the weather from the region using all tools. You may need to use IP address to guess the location",
    functions=[get_weather, get_ip],
)

messages = [{"role": "user", "content": "What's the weather in my location?"}]

response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
