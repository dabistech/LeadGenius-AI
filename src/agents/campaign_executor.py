import sendgrid
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

class CampaignExecutorAgent:
    def __init__(self, sendgrid_api_key, twilio_account_sid, twilio_auth_token, crm_wrapper, insights_agent):
        self.sendgrid_client = sendgrid.SendGridAPIClient(sendgrid_api_key)
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)
        self.crm_wrapper = crm_wrapper
        self.insights_agent = insights_agent

    def execute_campaign(self, lead):
        # Score the lead
        score = self.insights_agent.score_lead(lead)
        if score < 7:
            print(f"Lead scored {score}. Skipping outreach.")
            return

        # Send email/SMS
        email = lead["email"]
        self.send_email(email, "Partnership Opportunity", "Hi, let's connect!")

        # Sync lead with CRM
        self.crm_wrapper.create_contact(
            email=email,
            first_name=lead["first_name"],
            last_name=lead["last_name"],
            company=lead["company"],
        )
