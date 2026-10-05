# Comparing with NLP (Reddit Political Lean Classification)

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit-learn-ML-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains a natural language processing (NLP) and machine learning pipeline designed to analyze and classify text data (Reddit posts based on Political Lean) using TF-IDF and classification algorithms[cite: 18].

---

## Project Workflow
schl
1. **Data Preprocessing**: Loading dataset, combining `Title` and `Text` features into a unified `content` column, and cleaning missing values[cite: 18].
2. **Feature Extraction**: Transforming textual content into numerical vectors via `TfidfVectorizer`[cite: 18].
3. **Model Training & Evaluation**: Benchmarking multiple classifiers (Logistic Regression, Random Forest, MultinomialNB, etc.) using train/test splits[cite: 18].
4. **Model Serialization**: Saving the optimized model using `joblib` (`nlp_model.pkl`)[cite: 18].
5. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/reddit-political-nlp.git](https://github.com/YOUR_USERNAME/reddit-political-nlp.git)
   cd reddit-political-nlp
