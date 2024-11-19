from swarm import Agent, Swarm

client = Swarm()


def instructions(context_variables, *args, **kwargs):
    name = context_variables.get("name", "User")
    print(f"{args}, {kwargs}")
    return f"You are a helpful agent. Greet the user by name ({name})."


def print_account_details(context_variables: dict):
    user_id = context_variables.get("user_id", None)
    name = context_variables.get("name", None)
    print(f"Account Details: {name=} {user_id=}")
    return f"Success: {name=} {user_id=}"


agent = Agent(
    name="Agent",
    instructions=instructions,
    functions=[print_account_details],
)

context_variables = {
    "name": "James",
}

response = client.run(
    messages=[{"role": "user", "content": "Hi!"}],
    agent=agent,
    context_variables=context_variables,
    debug=True,
)
print(response.messages[-1]["content"])

response = client.run(
    messages=[
        {
            "role": "user",
            "content": "Print and explain my account details! Is there anything missing?",
        }
    ],
    agent=agent,
    context_variables=context_variables,
)
print(response.messages[-1]["content"])
