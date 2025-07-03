import pandas as pd
import numpy as np

def generate_telematics_data(num_records=500):
    np.random.seed(42)
    data = {
        'driver_id': np.random.randint(1000, 1100, size=num_records),
        'speed': np.random.normal(60, 10, size=num_records),  # km/h
        'acceleration': np.random.normal(0.6, 0.3, size=num_records),  # m/s²
        'brake_force': np.random.normal(0.4, 0.2, size=num_records),    # scale 0–1
        'steering_angle': np.random.normal(0, 15, size=num_records),   # degrees
        'timestamp': pd.date_range(start='2025-01-01', periods=num_records, freq='min')
    }
    df = pd.DataFrame(data)
    df.to_csv('telematics_data.csv', index=False)
    print(" Generated telematics_data.csv")

if __name__ == "__main__":
    generate_telematics_data()
