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

1. [Autogen Demo: Building Our First Agent](notebooks/1.0-ls-autogen-demo-building-our-first-agent.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/1.0-ls-autogen-demo-building-our-first-agent.ipynb)

2. [Autogen Demo: Student Assistant Expert](notebooks/2.0-ls-autogen-demo-student-assistant-expert.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/2.0-ls-autogen-demo-student-assistant-expert.ipynb)

3. [Autogen Demo: Retrieval Augmented Chat](notebooks/3.0-ls-autogen-demo-retrieval-augmented-chat.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/3.0-ls-autogen-demo-retrieval-augmented-chat.ipynb)

4. [Autogen Demo: Writer Commander Safeguard Multi-Agent Coding](notebooks/4.0-ls-autogen-demo-writer-commander-safeguard-multi-agent-coding.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/4.0-ls-autogen-demo-writer-commander-safeguard-multi-agent-coding.ipynb)

5. [Autogen Demo: Dynamic Group Chat](notebooks/5.0-ls-autogen-demo-dynamic-group-chat.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/5.0-ls-autogen-demo-dynamic-group-chat.ipynb)

6. [Autogen Demo: Agent Builder Recipe](notebooks/6.0-ls-autogen-demo-agent-builder-recipe.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/6.0-ls-autogen-demo-agent-builder-recipe.ipynb)

7. [Autogen Demo: Research Assistant](notebooks/7.0-ls-autogen-demo-research-assistant.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/7.0-ls-autogen-demo-research-assistant.ipynb)

8. [Autogen Demo: Personal Assistant](notebooks/8.0-ls-autogen-demo-personal-assistant.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/8.0-ls-autogen-demo-personal-assistant.ipynb)

9. [Building a Autogen Agent: Desktop Tasks](notebooks/building-a-autogen-agent-desktop-tasks.ipynb)

   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/building-a-autogen-agent-desktop-tasks.ipynb)

10. [Demo: Autogen Function Calling](notebooks/demo-autogen-function-calling.ipynb)

    [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/EnkrateiaLucca/oreilly_live_training_autogen/blob/main/notebooks/demo-autogen-function-calling.ipynb)
