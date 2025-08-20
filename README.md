# O'Reilly Live Trainining - Getting Started with AutoGen

## Setup

**Conda**

- Install [anaconda](https://www.anaconda.com/download)
- This repo was tested on a Mac with python=3.11
- Create an environment: `conda create -n oreilly-autogen python=3.11`
- Activate your environment with: `conda activate oreilly-autogen`
- Install requirements with: `pip install -r requirements.txt`
- Setup your openai [API key](https://platform.openai.com/)

**Pip**


1. **Create a Virtual Environment:**
    Navigate to your project directory. Make sure you hvae python3.11 installed! 
    If using Python 3's built-in `venv`:
    ```bash
    python -m venv oreilly_env
    ```
    If you're using `virtualenv`:
    ```bash
    virtualenv oreilly-autogen
    ```

2. **Activate the Virtual Environment:**
    - **On Windows:**
      ```bash
      .\oreilly-autogen\Scripts\activate
      ```
    - **On macOS and Linux:**
      ```bash
      source oreilly-autogen/bin/activate
      ```

3. **Install Dependencies from `requirements.txt`:**
    ```bash
    pip install python-dotenv
    pip install -r requirements.txt
    ```

4. Setup your openai [API key](https://platform.openai.com/)

Remember to deactivate the virtual environment once you're done by simply typing:
```bash
deactivate
```

## Setup your .env file

- Change the `.env.example` file to `.env` and add your OpenAI API key.

## To use this Environment with Jupyter Notebooks:

- ```pip install jupyter```
- ```python3 -m ipykernel install --user --name=oreilly-autogen```

## Notebooks

Here are the notebooks available in the `notebooks/` folder:

1. [Autogen Basics](notebooks/1.0-autogen-basics.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/1.0-autogen-basics.ipynb)

2. [Code Concepts](notebooks/2.0-code-concepts.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/2.0-code-concepts.ipynb)

3. [Autogen Messages](notebooks/3.0-autogen-messages.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/3.0-autogen-messages.ipynb)

4. [Data Analysis Conversation Example](notebooks/3.1-data-analysis-conversation-example.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/3.1-data-analysis-conversation-example.ipynb)

5. [Tools](notebooks/4.0-tools.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/4.0-tools.ipynb)

6. [Autogen Teams](notebooks/5.0-autogen-teams.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/5.0-autogen-teams.ipynb)

7. [Autogen Teams Selector GroupChat](notebooks/5.1-autogen-teams-selector-groupchat.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/5.1-autogen-teams-selector-groupchat.ipynb)

8. [Multi-Agent with Agents as Tools](notebooks/5.2-multi-agent-with-agents-as-tools.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/5.2-multi-agent-with-agents-as-tools.ipynb)

9. [Company Research Agent](notebooks/6.0-company-research-agent.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/6.0-company-research-agent.ipynb)

10. [RSS Feed Agent](notebooks/6.1-rss-feed-agent.ipynb)

    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/6.1-rss-feed-agent.ipynb)
