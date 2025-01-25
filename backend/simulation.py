import pandas as pd

class TrafficSimulator:
    def __init__(self):
        self.data = pd.read_csv('datasets/traffic.csv')
    
    def predict_congestion(self, junction):
        junction_data = self.data[self.data['Junction'] == junction]
        return {
            'junction': junction,
            'predicted_congestion': junction_data['Vehicles'].mean() * 1.5
        }