from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load datasets
traffic_df = pd.read_csv('datasets/traffic.csv')
rta_df = pd.read_csv('datasets/RTA Dataset.csv')

@app.route('/api/traffic')
def get_traffic():
    return jsonify(traffic_df.sample(100).to_dict(orient='records'))

@app.route('/api/simulate', methods=['POST'])
def simulate():
    data = request.json
    junction = data['junction']
    
    # Simple congestion simulation
    simulated = traffic_df.copy()
    simulated.loc[simulated['Junction'] == junction, 'Vehicles'] *= 3
    return jsonify(simulated.to_dict(orient='records'))

@app.route('/api/emergency', methods=['POST'])
def emergency():
    data = request.json
    return jsonify({
        "status": "success",
        "message": f"Emergency received at {data['location']}",
        "heart_rate": data['heart_rate']
    })

@app.route('/')
def dashboard():
    return send_file('../frontend/index.html')

if __name__ == '__main__':
    app.run(port=5000)