from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

datos_sensor = {}
comando_pendiente = {}

@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    global datos_sensor
    datos_sensor = request.get_json()
    return jsonify({"status": "ok"})

@app.route('/api/datos', methods=['GET'])
def obtener_datos():
    return jsonify(datos_sensor)

@app.route('/api/comando', methods=['GET'])
def obtener_comando():
    return jsonify(comando_pendiente)

@app.route('/api/comando', methods=['POST'])
def actualizar_comando():
    global comando_pendiente
    comando_pendiente = request.get_json()
    return jsonify({"status": "comando actualizado"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
