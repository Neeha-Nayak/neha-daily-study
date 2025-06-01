# 📉 Customer Churn Analysis with PySpark

This project demonstrates how to perform **Customer Churn Analysis** using PySpark, leveraging its powerful DataFrame API, preprocessing utilities, and machine learning pipeline. The dataset used is a sampled subset from a fictional telecom company, *Telco*, which offers home phone and internet services.

## 🧠 Objective

To predict customer churn — the likelihood of customers leaving the company — and identify key factors contributing to churn. Insights from this analysis can help improve customer retention strategies (though strategy development is beyond the scope of this project).

## 🗂️ Dataset Overview

- **Source**: Fictional dataset representing Telco's Q3 customer base.
- **Size**: 1,743 customers × 21 features.
- **Target Column**: `Churn` (Yes/No).
- **Features Include**:
  - Demographics: Age range, gender, partner status, dependents.
  - Services: Internet, phone, streaming, online security, backup, tech support.
  - Account Info: Contract type, payment method, billing, tenure, charges.
  - Customer Scores: Satisfaction, CLTV, churn score.

## ✅ Project Tasks

### 1. 🔍 Load Data
- Load Telco customer churn data into a PySpark DataFrame.
- Validate data format and structure.

### 2. 🧹 Data Preprocessing & Transformation
- Handle missing values, invalid entries, and convert data types.
- Perform filtering, grouping, and aggregations.
- Engineer relevant features for modeling.

### 3. 📊 Exploratory Data Analysis (EDA)
- Understand churn distribution and feature distributions.
- Visualize correlations and trends (age, contract type, services, etc.).
- Identify key predictors of churn using statistical analysis.


## 💡 Key Tools & Libraries
- Apache Spark (PySpark)
- Spark DataFrames
- Spark SQL

