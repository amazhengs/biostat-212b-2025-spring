# biostat-212b-2025-spring

# Diabetes Risk Predictor App

**A simple but interactive, multilingual web app** that predicts diabetes risk using a logistic regression model trained on U.S. health survey data (BRFSS 2015).  
Built with [Streamlit](https://streamlit.io) for accessibility and interactivity.

---
## Background / Motivation

From the course content in BIOSTATS 212B, I wanted to create a simple, public-facing tool that demonstrates understanding of logistic regression and also has a general educational purpose. Diabetes is a growing health concern globally (~38.4M cases in the U.S. alone), and early awareness tools can help initiate conversations and behavior regarding risk and prevention. I was able to explore machine learning techniques and later, neural networks through my group assignments in this course, but I myself wanted to implement the tools that my group mentioned in Assignment 1 and 2.

This diabetes risk assessment app was built to be simple, interpretable, and multilingual (English, French, Simplified Chinese, Korean), reflecting my desire to promote inclusivity and real-world applicability. These specific languages were chosen simply because I was personally most familiar with them, but realistically, an application like this would be expanded for even more. This project seeks to demonstrate how machine learning can support population health through transparent and interactive interfaces.

## About the App

This educational tool estimates the probability of having diabetes based on simple self-reported health and lifestyle inputs like:

- Age  
- Body Mass Index (BMI)  
- General health status
- Blood pressure
- Blood cholesterol
- Physical activity  
- Smoking habits  

It uses a **Logistic Regression model** trained on the publicly available CDC’s 2015 Behavioral Risk Factor Surveillance System (BRFSS) — one of the most comprehensive health surveys in the United States.

---

## Language Support

The app currently supports the following languages:
- English 🇺🇸
- French 🇫🇷
- Simplified Chinese 🇨🇳
- Korean 🇰🇷

---

## Trying Out the App

**[Launch the app](https://biostat-212b-2025-spring-nswp6f3cjv3mivbmcey7fa.streamlit.app/)**  

---

## Model Details

- **Dataset:** [CDC BRFSS 2015 Diabetes Indicators](https://archive.ics.uci.edu/dataset/891/cdc+diabetes+health+indicators)
- **Model type:** Logistic Regression (sklearn)
- **Test Accuracy:** 86.13%
- **Preprocessing:** Selected key features ("Age", "BMI", "GenHlth","HighBP", "HighChol", "PhysHlth", "Smoker", "PhysActivity"), label encoding for binary inputs

---

## File Structure

```
diabetes-risk-predictor/
├── simple_diabetes_app.py                  # streamlit app code
├── simple_diabetes_model.pkl  # trained simple logistic regression model
├── requirements.txt        # package dependencies and required modules
└── README.md               # this descriptive file
```

---

## How to Run Locally

1. Clone this repo:

   ```bash
   git clone https://github.com/amazhengs/212b-biostats-2025-spring
   cd diabetes-risk-predictor
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run simple_diabetes_app.py
   ```

---

## ⚠️ Disclaimer

This tool is **not a diagnostic device**. It is trained on self-reported, population-level data and is meant for **educational purposes only**.
Always consult a medical professional for health concerns.

---

## Submission Summary + Student Information

- **Course**: BIOSTATS 212B – Spring 2025 - Prof. Angshuman Saha
- **Project**: Optional Individual Extra Credit Project
- **Author**: Karen Zheng 504969951
- **Title**: Simple Multilingual Diabetes Risk Predictor App
- **Technologies Used**: Python, Streamlit, Logistic Regression, GitHub  
- **Live App**: https://biostat-212b-2025-spring-nswp6f3cjv3mivbmcey7fa.streamlit.app/
- **GitHub Repo**: https://github.com/amazhengs/biostat-212b-2025-spring

My app uses CDC survey-based health inputs to estimate diabetes risk using logistic regression.
It supports four languages (English, French, Simplified Chinese, Korean) and includes explanations of the model and its coefficients.
Model accuracy: **86.13%**
