# Advanced EDA & Feature Engineering on E-Commerce Orders Dataset

## Overview

This project focuses on transforming raw and incomplete e-commerce transaction data into a clean, reliable, and machine-learning-ready dataset. The workflow includes missing value treatment, outlier detection and handling, feature engineering, and statistical analysis using Python-based data science tools.

The final dataset is optimized for predictive analytics, business intelligence, and machine learning applications.

---

## Project Objectives

* Handle missing values using Mean, Mode, and KNN Imputation techniques.
* Detect and treat outliers using the Interquartile Range (IQR) method.
* Engineer meaningful predictive features from existing attributes.
* Perform statistical analysis and exploratory data preparation.
* Generate a clean dataset suitable for machine learning models.

---

## Business Problem

E-commerce datasets often contain missing values, inconsistencies, and extreme observations that can negatively impact data analysis and machine learning model performance.

This project addresses these challenges by implementing a complete preprocessing pipeline that converts raw transactional data into a high-quality dataset suitable for predictive modeling and business intelligence applications.

---

## Dataset Information

**Dataset:** E-Commerce Orders Dataset

**Records:** 1200

**Features:** 14

### Available Attributes

* OrderID
* Date
* CustomerID
* Product
* Quantity
* UnitPrice
* ShippingAddress
* PaymentMethod
* OrderStatus
* TrackingNumber
* ItemsInCart
* CouponCode
* ReferralSource
* TotalPrice

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* OpenPyXL

---

## Data Preprocessing

### Missing Value Treatment

The dataset contained missing values in both categorical and numerical features. Multiple imputation techniques were applied to improve data quality.

#### Mean Imputation

Applied to numerical columns where missing values were replaced with the average value of the respective feature.

Examples:

* Quantity
* UnitPrice

Mean imputation helps preserve the overall distribution of numerical data.

Example:

```python
df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].mean()
)
```

#### Mode Imputation

Applied to categorical columns:

* CouponCode
* PaymentMethod

Mode imputation replaces missing values with the most frequently occurring category.

Example:

```python
df["CouponCode"] = df["CouponCode"].fillna(
    df["CouponCode"].mode()[0]
)
```

#### KNN Imputation

Applied to numerical columns:

* Quantity
* UnitPrice
* ItemsInCart
* TotalPrice

K-Nearest Neighbors (KNN) Imputer estimates missing values using similar observations in the dataset.

```python
imputer = KNNImputer(n_neighbors=5)
```

KNN imputation preserves relationships between variables and often produces more accurate estimates than simple statistical methods.

---

## Outlier Detection and Treatment

Outliers were identified and treated using the Interquartile Range (IQR) method.

### Formula

IQR = Q3 − Q1

Lower Bound = Q1 − 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR

Values outside the acceptable range were capped to reduce the influence of extreme observations while maintaining data integrity.

### Benefits

* Reduces noise in the dataset
* Improves model performance
* Prevents skewed statistical results
* Enhances prediction accuracy

---

## Feature Engineering

To improve predictive capability, several new features were generated.

### RevenuePerItem

Measures revenue generated per item sold.

```python
RevenuePerItem = TotalPrice / Quantity
```

### AverageCartValue

Represents the average monetary value of products in a shopping cart.

```python
AverageCartValue = TotalPrice / ItemsInCart
```

### CouponUsed

Binary feature indicating whether a coupon was applied.

```python
1 = Coupon Used
0 = Coupon Not Used
```

### OrderMonth

Extracted from the Date column to capture seasonal purchasing patterns.

### OrderYear

Extracted from the Date column to support long-term trend analysis.

---

## Exploratory Data Analysis (EDA)

The preprocessing pipeline enables further exploratory analysis, including:

* Sales Distribution Analysis
* Product Popularity Analysis
* Coupon Usage Trends
* Payment Method Preferences
* Customer Purchasing Behavior
* Cart Value Distribution

---

## Statistical Analysis

Descriptive statistics were generated to understand the overall distribution of data.

Metrics analyzed:

* Mean
* Median
* Standard Deviation
* Minimum and Maximum Values
* Quartiles
* Dataset Summary Statistics

Example:

```python
df.describe()
```

---

## Machine Learning Readiness

After preprocessing, the dataset satisfies key machine learning requirements:

* No critical missing values
* Reduced outlier influence
* Enhanced feature set
* Improved consistency
* Better predictive capability

The final dataset can be directly used for:

* Classification Models
* Regression Models
* Clustering Algorithms
* Recommendation Systems
* Customer Segmentation
* Sales Forecasting

---

## Output

The processed dataset is exported as:

```text
Final_ML_Ready_Dataset.xlsx
```

This dataset is ready for analytics and machine learning workflows.

---

## Project Workflow

1. Load Dataset
2. Inspect Dataset Structure
3. Identify Missing Values
4. Apply Mean Imputation
5. Apply Mode Imputation
6. Apply KNN Imputation
7. Detect Outliers using IQR
8. Treat Outliers
9. Engineer New Features
10. Generate Statistical Summary
11. Export ML-Ready Dataset

---

## Results

✔ Successfully handled missing values

✔ Detected and treated outliers

✔ Generated multiple predictive features

✔ Improved dataset quality and consistency

✔ Produced a machine-learning-ready dataset

✔ Enhanced suitability for predictive analytics and business decision-making

---
