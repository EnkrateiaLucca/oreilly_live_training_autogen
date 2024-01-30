# O'Reilly Live Trainining - Getting Started with AutoGen

## Setup

**Conda**

- Install [anaconda](https://www.anaconda.com/download)
- Create an environment: `conda create -n oreilly-autogen`
- Activate your environment with: `conda activate oreilly-autogen`
- Install requirements with: `pip install -r requirements.txt`
- Setup your openai [API key](https://platform.openai.com/)

**Pip**


1. **Create a Virtual Environment:**
    Navigate to your project directory. If using Python 3's built-in `venv`:
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

```python3 -m ipykernel install --user --name=oreilly-autogen```