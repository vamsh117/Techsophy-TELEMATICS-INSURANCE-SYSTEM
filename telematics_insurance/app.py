from flask import Flask, render_template
import pandas as pd
from behavior_analysis import analyze_behavior
from risk_scoring import calculate_risk
from feedback_module import get_safety_feedback

app = Flask(__name__)

@app.route("/")
def dashboard():
    df = pd.read_csv("telematics_data.csv")
    score = analyze_behavior(df)
    risk, premium = calculate_risk(score)
    feedback = get_safety_feedback(score)

    return render_template("dashboard.html",
                           score=score,
                           risk=risk,
                           premium=f"{premium * 100}%",
                           feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
