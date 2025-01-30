from transformers import pipeline

class OutreachPersonalizationAgent:
    def __init__(self):
        self.text_generator = pipeline("text-generation", model="gpt-2")

    def generate_message(self, prospect_data):
        """
        Generates a personalized message based on prospect data.
        """
        name = prospect_data.get("name", "there")
        company = prospect_data.get("company", "your company")
        prompt = f"Write a personalized outreach message to {name} at {company}:"
        message = self.text_generator(prompt, max_length=50)[0]['generated_text']
        return message
