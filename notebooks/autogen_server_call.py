import asyncio
import json
from autogen_agentchat.teams import BaseGroupChat
from autogenstudio.teammanager import TeamManager

async def load_and_run_team():
    """
    Two methods to load and run a team from a saved configuration:
    1. Using BaseGroupChat.load_component (direct AutoGen approach)
    2. Using TeamManager (AutoGen Studio approach)
    """
    
    # Method 1: Direct AutoGen approach using BaseGroupChat
    print("Method 1: Loading team using BaseGroupChat.load_component...")
    try:
        # Load the team configuration from JSON file
        with open("team.json", "r") as f:
            team_config = json.load(f)
        
        # Load the team from the configuration
        team = BaseGroupChat.load_component(team_config)
        print(f"Team loaded successfully with participants: {[p.name for p in team._participants]}")
        
        # Run the team with a task
        result = await team.run(task="What is the weather in New York?")
        print("\nDirect AutoGen Result:")
        print(result)
    except Exception as e:
        print(f"Method 1 Error: {e}")
    
    # Method 2: AutoGen Studio approach using TeamManager
    print("\n" + "="*50)
    print("Method 2: Using TeamManager from AutoGen Studio...")
    try:
        # Initialize the TeamManager
        manager = TeamManager()
        
        # Run a task with the team configuration file
        result = await manager.run(
            task="What is the weather in New York?",
            team_config="./team.json"
        )
        
        print("\nTeamManager Result:")
        if hasattr(result, 'messages'):
            for msg in result.messages:
                print(msg)
        else:
            print(result)
    except Exception as e:
        print(f"Method 2 Error: {e}")

# Run the async function
if __name__ == "__main__":
    asyncio.run(load_and_run_team())