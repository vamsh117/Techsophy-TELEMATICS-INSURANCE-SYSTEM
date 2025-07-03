# Techsophy-TELEMATICS-INSURANCE-SYSTEM

# Telematics-Based Usage-Based Insurance System

## Overview

This project presents a modular, AI-driven telematics system that analyzes real-time driving behavior to enable **usage-based insurance (UBI)** pricing. Traditional auto insurance often lacks fairness, basing premiums on static attributes like age or location. Our system enables **dynamic premium adjustment** and **safety feedback** based on how a person actually drives.

The system processes telematics data (speed, acceleration, braking force, steering behavior, etc.) to:
- Analyze driving behavior
- Calculate a personalized safety score
- Assess risk levels
- Adjust insurance premiums
- Provide personalized safety recommendations via a user-friendly web dashboard

---

## Key Features

- **Behavior Analysis:** Quantifies risky driving patterns such as harsh acceleration, sharp turns, and speeding.
- **Risk Scoring:** Translates driving behavior into risk categories (Low, Medium, High, Critical).
- **Premium Adjustment:** Dynamically increases or decreases insurance premium based on real-world behavior.
- **Feedback Engine:** Offers actionable suggestions to improve driver safety.
- **Interactive Dashboard:** Web-based interface to visualize and interpret the scoring results.

---

## System Architecture

The project follows a modular design pattern for clarity, scalability, and maintainability:

| Module                | Responsibility                                                  |
|-----------------------|------------------------------------------------------------------|
| `data_generator.py`   | Simulates telematics data (speed, acceleration, etc.)            |
| `behavior_analysis.py`| Calculates a driver safety score based on driving behavior       |
| `risk_scoring.py`     | Determines risk level and corresponding premium adjustment       |
| `feedback_module.py`  | Provides personalized safety tips based on score                 |
| `app.py`              | Integrates all modules and serves the dashboard via Flask        |

---

## Technologies Used

- **Language:** Python 3.10+
- **Framework:** Flask (for web application)
- **Libraries:** Pandas, NumPy
- **Frontend:** HTML5, CSS3 (Jinja2 templating engine)
- **Data Format:** CSV (simulated telematics data)

---



