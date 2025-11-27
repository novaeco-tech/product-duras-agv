import requests
import os
from unittest.mock import patch

API_URL = "http://api:8000"

# This test runs *locally* against the duras-agv-api only.
# It MUST mock any calls to external enablers (e.g., agro-api, ai-api).

@patch('requests.post')
@patch('requests.get')
def test_create_autonomous_mission(mock_get, mock_post):
    """
    Tests that the 'duras-agv-api' correctly orchestrates calls to the
    'agro-api' and 'ai-api' when a new mission is created.
    """
    
    # 1. Configure the mock for 'agro-api'
    # This simulates the 'agro-api' returning farm plot data
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "plot_id": "plot-456",
        "coordinates": "[...]"
    }
    
    # 2. Configure the mock for 'ai-api'
    # This simulates the 'ai-api' accepting a new mission
    mock_post.return_value.status_code = 202
    mock_post.return_value.json.return_value = {"mission_id": "mission-789"}

    # 3. Call our internal 'duras-agv-api' endpoint
    response = requests.post(
        f"{API_URL}/v1/missions",
        json={"farm_id": "farm-123", "task": "scan"}
    )
    
    # 4. Test 1: Did our own API succeed?
    assert response.status_code == 201
    assert response.json()["status"] == "pending"
    
    # 5. Test 2: Did our API correctly call the external 'agro-api'?
    mock_get.assert_called_with("http://agro-api:8000/v1/farms/farm-123/plot")
    
    # 6. Test 3: Did our API correctly call the external 'ai-api'?
    mock_post.assert_called_with(
        "http://ai-api:8000/v1/missions",
        json={"coordinates": "[...]", "task": "scan"}
    )
    
    # 7. Test 4: Did our API save the mission ID it got from 'ai-api'?
    assert response.json()["ai_mission_id"] == "mission-789"