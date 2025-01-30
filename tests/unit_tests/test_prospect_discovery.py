from src.agents.prospect_discovery import ProspectDiscoveryAgent

def test_find_leads():
    agent = ProspectDiscoveryAgent(api_key="mock_key")
    leads = agent.find_leads("CTOs in Berlin")
    assert isinstance(leads, list)
    assert len(leads) > 0
