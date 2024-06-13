import os
from dotenv import load_dotenv

load_dotenv()
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)

from langchain import hub

def lookup(name: str) -> str:
    llm = Ollama(model="mistral", 
                 temperature=0
                 )
    
    template = """given the full name {name_of_person} I want you to get me a link to their LinkedIn profile page. Your answer should contain only a URL"""



if __name__ == "__main__":
    linkedin_url = lookup("Chris Fiore")
    print(linkedin_url)