from flask import Flask, jsonify, request
from calc.calc import suma  # Cambiar esta línea

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>Flask App</h1><p>API funcionando</p>"

@app.route("/suma", methods=["POST"])
def sumar():
  data = request.get_json()
  resultado = suma(data["a"], data["b"])
  return jsonify({"resultado": resultado})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)