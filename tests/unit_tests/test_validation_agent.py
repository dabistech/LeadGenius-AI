from src.agents.validation_agent import ValidationAgent

def test_validate_email():
    agent = ValidationAgent(hunter_io_api_key="mock_key")
    email = agent.validate_email("startup.com", "John", "Doe")
    assert email == "john.doe@startup.com"
