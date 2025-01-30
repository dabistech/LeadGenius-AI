import requests
from src.utils.api_wrapper import LinkedInAPIWrapper

class ProspectDiscoveryAgent:
    def __init__(self, api_key):
        self.linkedin_api = LinkedInAPIWrapper(api_key)

    def find_leads(self, query):
        """
        Extracts leads based on a query (e.g., "CTOs in Berlin SaaS startups").
        """
        print(f"Searching for leads with query: {query}")
        leads = self.linkedin_api.extract_data(query)
        return leads
