# filename: fine_tuning_chatgpt.py

import nbformat as nbf

nb = nbf.v4.new_notebook()

intro = """\
# Fine Tuning with the ChatGPT API

This tutorial is based on the information provided in the OpenAI guide for fine-tuning. It provides a simple yet authentic example for fine-tuning involved obtaining structured outputs. 

Please note that the actual fine-tuning process can't be done via the API, but you can use the fine-tuned model via the API. The fine-tuning process is done on OpenAI's servers and requires a special request to OpenAI.

## What is Fine-Tuning?

Fine-tuning is a process to improve the performance of a model on a specific task. It involves continuing the training of the model on a new dataset. In the case of GPT-3, the model is initially trained on a large corpus of the internet, and then fine-tuned on a specific task using a smaller dataset.
"""

code_imports = """\
import openai
openai.api_key = 'your-api-key'
"""

fine_tuning = """\
## Fine-Tuning with ChatGPT

As mentioned earlier, the fine-tuning process is done on OpenAI's servers. You need to provide a dataset for fine-tuning. The dataset should be in a specific format. Each example in the dataset consists of a `role`, `content`, and optional `extras`. The `role` can be 'system', 'user', or 'assistant', and the `content` contains the text of the message from the role.

Here is an example of a conversation:
