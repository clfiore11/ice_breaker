from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms.ollama import Ollama
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("hello LangChain!")

    summary_template = """
    given the LinkedIn information {information} about the person I want you to create:
    1. a short summary
    2. two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = Ollama(model="mistral", temperature=0)

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/cfiore11/", mock=True)
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
