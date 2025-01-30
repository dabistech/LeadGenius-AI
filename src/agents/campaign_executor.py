import sendgrid
from sendgrid.helpers.mail import Mail
from twilio.rest import Client

class CampaignExecutorAgent:
    def __init__(self, sendgrid_api_key, twilio_account_sid, twilio_auth_token):
        self.sendgrid_client = sendgrid.SendGridAPIClient(sendgrid_api_key)
        self.twilio_client = Client(twilio_account_sid, twilio_auth_token)

    def send_email(self, to_email, subject, content):
        """
        Sends an email using SendGrid.
        """
        message = Mail(
            from_email="noreply@leadgenius.ai",
            to_emails=to_email,
            subject=subject,
            html_content=content
        )
        response = self.sendgrid_client.send(message)
        return response.status_code

    def send_sms(self, to_phone, message):
        """
        Sends an SMS using Twilio.
        """
        self.twilio_client.messages.create(
            body=message,
            from_="+1234567890",  # Your Twilio number
            to=to_phone
        )
