from fastapi.testclient import TestClient
from app import app  # Ensure 'app.py' has a FastAPI instance

client = TestClient(app)  # Create a test client for the FastAPI app

def test_homepage():
    response = client.get("/")  # Call the homepage route

    assert response.status_code == 200  # Check if the request was successful
    
    # Check if the title is within the response text, even if there are extra tags or spaces
    assert "<title>" in response.text  # Check for the opening <title> tag
    assert "Spoorthi Profile" in response.text  # Check for the profile name within the <title> tag
