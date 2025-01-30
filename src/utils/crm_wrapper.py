class CRMInsightsAgent:
    def __init__(self, api_key):
        self.client = DeepSeekClient(api_key=api_key)

    def score_lead(self, lead_data):
        """
        Scores a lead based on CRM data using DeepSeek R1.
        """
        prompt = (
            f"Analyze the following lead data and assign a score from 1 to 10 "
            f"based on their likelihood to convert: {lead_data}"
        )
        response = self.client.generate(prompt=prompt, max_tokens=10)
        return int(response["text"].strip())
