import pandas as pd

def analyze_behavior(df):
    df['speeding'] = df['speed'] > 80
    df['harsh_acceleration'] = df['acceleration'] > 1.0
    df['harsh_braking'] = df['brake_force'] > 0.6
    df['sharp_turn'] = abs(df['steering_angle']) > 25

    behavior_score = 100
    behavior_score -= df['speeding'].sum() * 0.5
    behavior_score -= df['harsh_acceleration'].sum() * 0.8
    behavior_score -= df['harsh_braking'].sum() * 0.7
    behavior_score -= df['sharp_turn'].sum() * 0.6

    return round(max(0, behavior_score), 2)

if __name__ == "__main__":
    df = pd.read_csv('telematics_data.csv')
    score = analyze_behavior(df)
    print(f"Driver Safety Score: {score}/100")
