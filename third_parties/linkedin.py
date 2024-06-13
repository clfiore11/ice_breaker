import os
import requests

from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """scrape information from LinkedIn profiles, 
    manually scrape information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/clfiore11/41a1fad21421c10fa5d4a4c0efd40efc/raw/3791c02c688852a73205518cfc3fd6a1307db42a/dummy_linkedin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        pass

    data = response.json()

    return data




if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/cfiore11/",
        )
    )