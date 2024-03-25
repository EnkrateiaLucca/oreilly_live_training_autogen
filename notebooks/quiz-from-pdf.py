#!/usr/bin/env python
# coding: utf-8

import argparse
import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent


def generate_quiz(url, num_questions):
    config_list = autogen.config_list_from_json("./OAI_CONFIG_LIST")
    
    llm_config = {
        "seed": 42,
        "config_list": config_list,
        "temperature": 0,
    }
    
    assistant = RetrieveAssistantAgent(
        name="assistant",
        system_message="You are a helpful assistant.",
        llm_config=llm_config,
    )
    
    rag_proxy_agent = RetrieveUserProxyAgent(
        name="ragproxyagent",
        retrieve_config={
            "task": "qa",
            "docs_path": url
        }
    )
    
    # Initiate chat and ask question
    assistant.reset()
    output_quiz = rag_proxy_agent.initiate_chat(assistant, 
                                                problem=f"""Create a quiz with {num_questions} questions to practice my understanding of the this paper.
                              Outputs should be the {num_questions} questions as bullet points, then a section named answers with the corresponding answers separate.""")
    return output_quiz


def main():
    parser = argparse.ArgumentParser(description="Generate a quiz from a specified source.")
    parser.add_argument("-url", type=str, help="URL of the source document", required=True)
    parser.add_argument("-n", type=int, help="Number of questions to generate", default=5)
    
    args = parser.parse_args()
    
    print(args.url)
    quiz = generate_quiz(args.url, args.n)
    print(quiz)


if __name__ == "__main__":
    main()