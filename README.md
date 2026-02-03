# Exam Integrity Detection — Online Cheating Prediction System

Exam Integrity Detection is a machine learning project that predicts whether an online exam session shows signs of cheating. The project includes:

- A training pipeline to build a classifier (Cheating / No Cheating)
- A Streamlit web app for inference and visualization
- Support for real-world datasets provided as CSVs containing coordinates extracted from images or video frames collected during exam sessions

This repository is intended for research, demonstration, and education. Do NOT use this as a sole source of truth for academic integrity decisions — real deployment requires human review, strong privacy controls, and institutional policy.

---

## Demo

https://github.com/user-attachments/assets/56e20ac3-2ab8-4de3-8f3a-41a9fee39a5f


## Highlights of the update

- The Streamlit app can now ingest CSVs of image/frame coordinates (per-session) and derive features from bounding boxes/landmarks to predict cheating/no-cheating.
- The project supports both real-world CSVs; when using real data, please follow the privacy and consent guidelines in the “Privacy & Responsible Use” section below.

---

## Features

- Binary classification: cheating vs no cheating
- Accepts input as:
  - Per-session aggregated features (CSV row per session), or
  - Per-frame / per-image coordinate CSVs (multiple rows per session) which the app aggregates into session features automatically
- Streamlit dashboard:
  - Upload CSVs with coordinates 
  - Interactive form and per-session predictions 

---

## Data: real-world CSV format (coordinates)

When using real-world data, the app expects a CSV containing coordinates extracted from images/frames. The app can accept either:

A) Aggregated per-session CSV (one row per session) — your usual pipeline
B) Per-frame CSV (one row per frame/image) — the app groups by session_id and computes derived session-level features

---

## Privacy & Responsible Use (important)

You are now working with real-world data that may include personally-identifiable information (PII) and biometric data. Before using real exam recordings:

- Confirm that you have explicit consent to collect and process the data for research or operational use.
- Anonymize or pseudonymize identifiers (do not commit raw images or PII to the repository).
- Minimize data retention and store data securely (encrypted storage, access control).
- Consider institutional approvals (IRB / ethics), legal counsel, and compliance with local laws (GDPR, CCPA).
- Use model outputs only as a signal to trigger human review; do not take punitive actions solely on automated predictions.

---

## Contributing

Contributions welcome. Suggested workflow:
1. Open an issue describing the change or bug
2. Fork and create a feature branch
3. Implement tests and update docs
4. Open a pull request

---
