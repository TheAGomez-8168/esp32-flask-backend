from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Esto permite que la web pueda hacer peticiones a este backend desde otro dominio

# Variable global para guardar el dato recibido de la ESP32
dato_esp32 = ""

@app.route('/api/dato', methods=['GET', 'POST'])
def manejar_dato():
    global dato_esp32
    if request.method == 'POST':
        # ESP32 envía dato aquí
        dato_esp32 = request.json.get('dato', '')
        return jsonify({'mensaje': 'Dato recibido', 'dato': dato_esp32})
    else:
        # Página web consulta el dato aquí
        return jsonify({'dato': dato_esp32})

import os  # al inicio del archivo, si no está ya

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # toma el puerto de la variable PORT o usa 5000
    app.run(host='0.0.0.0', port=port)

