from src.agents.prospect_discovery import ProspectDiscoveryAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.outreach_agent import OutreachPersonalizationAgent
from src.agents.campaign_executor import CampaignExecutorAgent

def test_end_to_end_workflow():
    # Step 1: Discover Leads
    pda = ProspectDiscoveryAgent(api_key="mock_key")
    leads = pda.find_leads("CTOs in Berlin SaaS startups")
    assert len(leads) > 0, "No leads found."

    # Step 2: Validate Contact Information
    vae = ValidationAgent(hunter_io_api_key="mock_key")
    lead = leads[0]
    email = vae.validate_email(lead["company"], lead["name"].split()[0], lead["name"].split()[-1])
    assert email is not None, "Email validation failed."

    # Step 3: Generate Personalized Message
    opa = OutreachPersonalizationAgent()
    message = opa.generate_message({"name": lead["name"], "company": lead["company"]})
    assert len(message) > 0, "Message generation failed."

    # Step 4: Execute Campaign
    cea = CampaignExecutorAgent(
        sendgrid_api_key="mock_sendgrid_key",
        twilio_account_sid="mock_twilio_sid",
        twilio_auth_token="mock_twilio_token"
    )
    response_code = cea.send_email(email, "Partnership Opportunity", message)
    assert response_code == 202, "Email sending failed."
