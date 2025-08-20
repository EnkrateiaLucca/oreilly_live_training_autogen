# AutoGen Studio: A Comprehensive Tutorial Guide

## What is AutoGen Studio?

AutoGen Studio is a **low-code interface** for rapidly prototyping AI agents and multi-agent systems. Built on AutoGen AgentChat, it provides a visual environment to design, test, and deploy conversational AI teams without extensive coding.

**Important Note:** AutoGen Studio is designed as a prototyping tool, not a production-ready application. Use it to experiment, demonstrate workflows, and export code for production implementations.

## Prerequisites & Installation

### System Requirements
- Python 3.10 or higher
- Node.js (version 14.15.0+ for source installation)
- API key for LLM provider (e.g., OpenAI)

### Installation Steps

1. **Create a Virtual Environment** (Recommended)
```bash
python -m venv autogen-env
source autogen-env/bin/activate  # On Windows: autogen-env\Scripts\activate
```

2. **Install AutoGen Studio**
```bash
pip install -U autogenstudio
```

3. **Set Up API Keys**
```bash
export OPENAI_API_KEY="your-api-key-here"  # On Windows: set OPENAI_API_KEY=your-api-key-here
```

4. **Launch AutoGen Studio**
```bash
autogenstudio ui --port 8081
```

Navigate to http://localhost:8081 in your browser.

## Core Components Overview

### 1. Team Builder
The visual interface where you create and configure multi-agent systems.

**Key Elements:**
- **Teams**: Groups of agents working together
- **Agents**: Individual AI entities with specific roles
- **Models**: LLM configurations (GPT-4, Claude, etc.)
- **Tools**: Functions agents can execute
- **Termination Conditions**: Rules for ending conversations

### 2. Playground
Interactive testing environment for your agent teams.

**Features:**
- Real-time message streaming
- Visual message flow
- Session management
- Performance monitoring

### 3. Gallery
Component marketplace for sharing and discovering pre-built agents and teams.

## Building Your First Agent Team

### Step 1: Access Team Builder
1. Click on "Team Builder" in the navigation
2. You'll see a visual canvas and component library

### Step 2: Create a Model Configuration
1. Click "Models" in the component library
2. Add a new model:
   - Name: `gpt-4-model`
   - Provider: `OpenAI`
   - Model: `gpt-4`
   - API Key: (use environment variable or enter directly)

### Step 3: Create Your First Agent
1. Click "Agents" in the component library
2. Configure the agent:
   ```
   Name: research_assistant
   System Message: "You are a helpful research assistant. Provide accurate, well-sourced information."
   Model: gpt-4-model
   ```

### Step 4: Create a Team
1. Click "Teams" in the component library
2. Drag your agent onto the team canvas
3. Configure team settings:
   ```
   Name: research_team
   Agents: [research_assistant]
   Termination: max_messages = 10
   ```

### Step 5: Add Tools (Optional)
Common tools to enhance agent capabilities:
- **Web Search**: Enable internet searches
- **Code Execution**: Run Python code
- **File Operations**: Read/write files

## Using the Playground

### Testing Your Team
1. Navigate to "Playground"
2. Select your team from the dropdown
3. Enter a task or question
4. Click "Run" to start the session

### Monitoring Execution
- **Message Flow**: View agent interactions in real-time
- **Artifacts**: Check generated files or code
- **Metrics**: Monitor token usage and response times

## Practical Example: Customer Support Bot Team

Let's build a practical customer support system with multiple specialized agents.

### Use Case: E-Commerce Support Team

**Team Components:**

1. **Greeting Agent**
   ```
   Name: greeter
   System Message: "You are a friendly customer service representative. 
                    Greet customers warmly and identify their needs."
   ```

2. **Order Specialist**
   ```
   Name: order_specialist
   System Message: "You handle order-related inquiries. Check order status, 
                    process returns, and track shipments."
   Tools: [database_query, tracking_api]
   ```

3. **Technical Support**
   ```
   Name: tech_support
   System Message: "You provide technical assistance for product issues. 
                    Offer troubleshooting steps and solutions."
   Tools: [knowledge_base_search, code_execution]
   ```

4. **Team Configuration**
   ```json
   {
     "name": "customer_support_team",
     "agents": ["greeter", "order_specialist", "tech_support"],
     "team_type": "sequential",
     "termination_condition": {
       "type": "max_messages",
       "max_messages": 15
     }
   }
   ```

### Workflow Example

**Customer Query:** "My order #12345 hasn't arrived, and the tracking isn't working"

**Team Response Flow:**
1. **Greeter** identifies this as an order + technical issue
2. **Order Specialist** checks order status and tracking information
3. **Technical Support** troubleshoots the tracking system issue
4. Team provides comprehensive solution

## Advanced Features

### JSON Configuration Editor
Switch between visual and JSON modes for precise control:
```json
{
  "name": "advanced_team",
  "agents": [...],
  "model_client": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 1000
  }
}
```

### Python Integration
Export and use teams programmatically:
```python
from autogenstudio.teammanager import TeamManager

tm = TeamManager()
result_stream = tm.run(
    task="Analyze customer feedback and generate report",
    team_config="customer_support_team.json"
)

for message in result_stream:
    print(message)
```

### Gallery Integration
1. **Import Components**: Browse and import pre-built agents
2. **Share Your Work**: Export teams for community use
3. **Version Control**: Track component versions

## Best Practices

### 1. Agent Design
- **Single Responsibility**: Each agent should have one clear role
- **Clear Instructions**: Write specific, actionable system messages
- **Tool Selection**: Only add tools the agent actually needs

### 2. Team Composition
- **Complementary Skills**: Combine agents with different strengths
- **Efficient Communication**: Minimize unnecessary agent interactions
- **Clear Termination**: Set appropriate message limits

### 3. Testing Strategy
- **Start Simple**: Test with basic queries first
- **Iterate Gradually**: Add complexity incrementally
- **Monitor Performance**: Track token usage and response quality

## Deployment Options

### Export to Python
1. Click "Export" in Team Builder
2. Choose Python format
3. Integrate into your application

### Docker Deployment
```bash
# Build container
docker build -t my-agent-team .

# Run team endpoint
docker run -p 8080:8080 my-agent-team
```

### API Endpoint Setup
```python
from fastapi import FastAPI
from autogenstudio.teammanager import TeamManager

app = FastAPI()
tm = TeamManager()

@app.post("/chat")
async def chat(task: str):
    result = tm.run(task=task, team_config="team.json")
    return {"response": result}
```

## Troubleshooting Common Issues

### API Key Errors
- Verify environment variable is set correctly
- Check API key permissions and quotas
- Try direct configuration in model settings

### Agent Communication Issues
- Review system messages for clarity
- Check termination conditions
- Verify model configurations

### Performance Problems
- Reduce max_tokens for faster responses
- Optimize team size (fewer agents = faster)
- Use appropriate models for task complexity

## Exercise: Build Your Own Team

**Challenge:** Create a "Research and Writing Team" that can:
1. Research a topic online
2. Organize information into key points
3. Write a structured article
4. Review and edit the content

**Suggested Team Structure:**
- Researcher Agent (with web search tool)
- Organizer Agent (structures information)
- Writer Agent (creates content)
- Editor Agent (reviews and polishes)

## Key Takeaways

1. **AutoGen Studio** simplifies multi-agent system development
2. **Visual Interface** makes agent configuration accessible
3. **Playground** enables rapid testing and iteration
4. **Export Options** support production deployment
5. **Community Gallery** accelerates development with shared components

## Next Steps

1. Experiment with different agent combinations
2. Explore available tools and integrations
3. Share your creations in the Gallery
4. Build production applications using exported code
5. Contribute to the AutoGen open-source project

---

**Remember:** AutoGen Studio is your prototyping playground. Use it to experiment, learn, and build amazing multi-agent systems!