
import json
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.conditions import TextMentionTermination

# Create an agent with OpenAI model client
agent = AssistantAgent(
    name="weather_agent",
    model_client=OpenAIChatCompletionClient(
        model="gpt-4o-mini",
    ),
    system_message="You are a helpful AI assistant. Solve tasks using your tools. Reply with TERMINATE when the task has been completed."
)

# Create a team with termination condition
agent_team = RoundRobinGroupChat(
    [agent], 
    termination_condition=TextMentionTermination("TERMINATE")
)

# Dump the team configuration to a component spec
config = agent_team.dump_component()

# Convert to dictionary and save as JSON file
team_config = config.model_dump()

# Save team configuration to file
with open("team.json", "w") as f:
    json.dump(team_config, f, indent=4)

print("Team configuration saved to team.json")
print("\nConfiguration preview:")
print(json.dumps(team_config, indent=2)[:500] + "...")

