import sys
import time
import threading
import requests
sys.path.insert(0, '/code')

from main import app

def run_flask_app():
  app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def test_e2e_full_workflow():
  # Iniciar Flask en un hilo separado
  flask_thread = threading.Thread(target=run_flask_app, daemon=True)
  flask_thread.start()
  time.sleep(3)  # Esperar que Flask inicie
  
  try:
    # Test 1: Verificar que la página principal carga
    response = requests.get("http://localhost:5000", timeout=5)
    assert response.status_code == 200
    assert "Flask App" in response.text
    assert "API funcionando" in response.text
    
    # Test 2: Verificar que la API funciona end-to-end
    api_response = requests.post("http://localhost:5000/suma", 
                               json={"a": 10, "b": 15},
                               timeout=5)
    assert api_response.status_code == 200
    data = api_response.json()
    assert data["resultado"] == 25
    
    # Test 3: Verificar manejo de errores
    error_response = requests.post("http://localhost:5000/suma", 
                                 json={"a": "invalid"},
                                 timeout=5)
    # Debería fallar pero no crash la app
    assert error_response.status_code != 200 or "error" in error_response.text.lower()
    
  except requests.exceptions.RequestException as e:
    assert False, f"Failed to connect to Flask app: {e}"