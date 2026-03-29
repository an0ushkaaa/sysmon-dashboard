import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_loads(client):
    response = client.get('/')
    assert response.status_code == 200

def test_metrics_endpoint(client):
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'cpu_percentage' in data