# Exam Integrity Detection — Online Cheating Prediction System

Exam Integrity Detection is a small machine learning project that predicts whether an online exam session shows signs of cheating. The project includes:

- A Streamlit web app for inference and visualization
- Explainability with SHAP (global feature importance bar plot)
- A synthetic dataset (generated for privacy) — no real student data is included

This repository is intended for research, demonstration, and education. Do NOT use this as a single source of truth for academic integrity decisions; real deployment requires careful policy, human review, privacy, and fairness checks.


## Demo

https://github.com/user-attachments/assets/1d0ea363-f5e4-4e24-ad53-2a0bd75edd93


## Features

- Binary classification: cheating vs no cheating
- Input features (examples — adapt to your dataset):
  - avg_time_per_q (Average seconds spent per question)
  - accuracy (Overall exam accuracy)
  - fast_answer_ratio (Questions answered too fast)
  - answer_change_rate (Average answer changes per question)
- Streamlit dashboard:
  - Form to enter feature values for a single session
  - Predicted label (Cheating / No Cheating) and probability
  - Global feature importance SHAP bar plot
- Synthetic dataset generation script (privacy-first)

---


## Contributing

Contributions are welcome:
- Open an issue describing the change or bug
- Fork and submit a pull request with tests and documentation updates

---
