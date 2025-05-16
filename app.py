import os
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Variables globales para simular valores leídos y configurados
temperatura = 25.0
ph = 7.0

temperaturaSet = 26.5
phSet = 7.2
tdis = 10
vdis = 5
dispensar_flag = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get_data', methods=['GET'])
def get_data():
    # Enviar datos que solo ESP32 lee (sensores y valores configurables)
    return jsonify({
        'temperatura': temperatura,
        'ph': ph,
        'temperaturaSet': temperaturaSet,
        'phSet': phSet,
        'tdis': tdis,
        'vdis': vdis,
        'dispensar': dispensar_flag
    })

@app.route('/api/set_data', methods=['POST'])
def set_data():
    global temperaturaSet, phSet, tdis, vdis, dispensar_flag
    data = request.json

    # Actualizar solo variables manipulables
    if 'temperaturaSet' in data:
        temperaturaSet = float(data['temperaturaSet'])
    if 'phSet' in data:
        phSet = float(data['phSet'])
    if 'tdis' in data:
        tdis = int(data['tdis'])
    if 'vdis' in data:
        vdis = int(data['vdis'])
    if 'dispensar' in data:
        dispensar_flag = bool(data['dispensar'])

    return jsonify({"status": "ok"})

# Ruta para que el ESP32 pueda enviar datos reales de sensores
@app.route('/api/send_sensor', methods=['POST'])
def send_sensor():
    global temperatura, ph
    data = request.json
    if 'temperatura' in data:
        temperatura = float(data['temperatura'])
    if 'ph' in data:
        ph = float(data['ph'])
    return jsonify({"status": "sensor data received"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
