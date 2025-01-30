from deepseek_api import DeepSeekClient

class OutreachPersonalizationAgent:
    def __init__(self, api_key):
        self.client = DeepSeekClient(api_key=api_key)

    def generate_message(self, prospect_data):
        """
        Generates a personalized message using DeepSeek R1.
        """
        name = prospect_data.get("name", "there")
        company = prospect_data.get("company", "your company")
        job_title = prospect_data.get("title", "professional")

        # Craft a prompt for DeepSeek R1
        prompt = (
            f"Write a highly personalized and professional outreach message "
            f"to {name}, who is the {job_title} at {company}. "
            f"The message should focus on how our solution can help their business grow."
        )

        # Generate response using DeepSeek R1
        response = self.client.generate(prompt=prompt, max_tokens=50)
        return response["text"]
