import sys
sys.path.insert(0, '/code')

from main import app

def test_api_suma():
  with app.test_client() as client:
    response = client.post('/suma', 
                         json={"a": 4, "b": 6},
                         content_type='application/json')
    
    assert response.status_code == 200
    data = response.get_json()
    assert data["resultado"] == 10