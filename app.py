from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 for local dev
    app.run(host='0.0.0.0', port=port)

CORS(app)
# Factores de emisión en kg CO2 por km
EMISSION_FACTORS = {
    "pie": 0,
    "bicicleta": 0,
    "auto": 0.21,
    "moto": 0.12,
    "tren": 0.05
}

@app.route('/api/transport-options', methods=['GET'])
def get_transport_options():
    return jsonify(EMISSION_FACTORS)

@app.route('/api/calculate', methods=['POST'])
def calculate_footprint():
    data = request.get_json()
    
    nombre = data.get('nombre')
    distancia = float(data.get('distancia'))
    transporte = data.get('transporte')

    factor = EMISSION_FACTORS.get(transporte, 0)
    huella = round(distancia * factor, 2)

    return jsonify({
        'nombre': nombre,
        'distancia': distancia,
        'transporte': transporte,
        'huella': huella
    })

if __name__ == '__main__':
    app.run(debug=True)