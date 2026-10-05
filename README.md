# Comparing with NLP (Natural Language Processing)

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit-learn-ML-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains an end-to-end natural language processing pipeline that analyzes and classifies text data (such as Reddit posts based on Political Lean) using TF-IDF feature extraction and various machine learning algorithms[cite: 18].

---

## Project Workflow
1. **Data Loading & Preparation**: Reading data from CSV files and combining `Title` and `Text` columns into a unified `content` feature[cite: 18].
2. **Data Cleaning**: Dropping missing values within the target label (`Political Lean`)[cite: 18].
3. **Feature Engineering**: Transforming textual contents into numerical representation using `TfidfVectorizer` with English stop words filtering[cite: 18].
4. **Model Benchmarking**: Evaluating multiple machine learning models (Logistic Regression, Random Forest, MultinomialNB, etc.) via an automated testing function (`algo_test`)[cite: 18].
5. **Model Serialization**: Saving the trained classification model using `joblib` (`nlp_model.pkl`)[cite: 18].
6. **Web Application**: Interactive user interface built using Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/comparing-with-nlp.git](https://github.com/YOUR_USERNAME/comparing-with-nlp.git)
   cd comparing-with-nlp
