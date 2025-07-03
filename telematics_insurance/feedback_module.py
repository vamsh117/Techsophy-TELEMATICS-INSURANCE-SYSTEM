def get_safety_feedback(score):
    if score > 90:
        return "Great driving! Keep it up!"
    elif score > 75:
        return "Good, but avoid speeding and harsh turns."
    elif score > 60:
        return "You need to drive more cautiously. Avoid sudden brakes and accelerations."
    else:
        return "High risk driving detected! Immediate improvement needed for safety and lower premiums."

if __name__ == "__main__":
    import pandas as pd
    from behavior_analysis import analyze_behavior

    df = pd.read_csv("telematics_data.csv")
    score = analyze_behavior(df)

    print(get_safety_feedback(score))
