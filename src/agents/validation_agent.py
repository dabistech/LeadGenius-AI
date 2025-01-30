import requests

class ValidationAgent:
    def __init__(self, hunter_io_api_key):
        self.hunter_io_api_key = hunter_io_api_key

    def validate_email(self, domain, first_name, last_name):
        """
        Validates email using Hunter.io API.
        """
        url = f"https://api.hunter.io/v2/email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={self.hunter_io_api_key}"
        response = requests.get(url).json()
        if response['data']:
            return response['data']['email']
        return None
