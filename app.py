from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Datos globales
datos = {
    "temperatura": 0.0,
    "ph": 0.0,
    "temperaturaSet": 25.0,
    "phSet": 7.0,
    "tDis": 0,
    "vDis": 0,
    "dispensar": False
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/dato", methods=["GET", "POST"])
def api_dato():
    global datos
    if request.method == "POST":
        data = request.get_json()
        datos["temperatura"] = data.get("temperatura", datos["temperatura"])
        datos["ph"] = data.get("ph", datos["ph"])
        return jsonify(datos)
    elif request.method == "GET":
        return jsonify(datos)

@app.route("/api/update", methods=["POST"])
def update():
    global datos
    data = request.get_json()
    datos["temperaturaSet"] = data.get("temperaturaSet", datos["temperaturaSet"])
    datos["phSet"] = data.get("phSet", datos["phSet"])
    datos["tDis"] = data.get("tDis", datos["tDis"])
    datos["vDis"] = data.get("vDis", datos["vDis"])
    datos["dispensar"] = data.get("dispensar", False)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
