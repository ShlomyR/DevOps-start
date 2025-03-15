from fastapi.testclient import TestClient
from app.main import app  # Replace with your actual FastAPI app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DevOps!"}  # Adjust based on your FastAPI response
