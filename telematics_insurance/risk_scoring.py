def calculate_risk(score):
    if score > 90:
        return "Low", -0.2
    elif score > 75:
        return "Medium", 0.0
    elif score > 60:
        return "High", 0.1
    else:
        return "Critical", 0.25

if __name__ == "__main__":
    import pandas as pd
    from behavior_analysis import analyze_behavior

    df = pd.read_csv("telematics_data.csv")
    score = analyze_behavior(df)
    risk_level, premium_change = calculate_risk(score)

    print(f"Score: {score}")
    print(f"Risk Level: {risk_level}")
    print(f"Premium Adjustment: {premium_change * 100}%")
