import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer



df = pd.read_excel(
    r"C:\Users\harsh\Downloads\Dataset for Data Analytics.xlsx"
)

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())



print("\nMissing Values Before Imputation")
print(df.isnull().sum())



if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna(
        df["CouponCode"].mode()[0]
    )

if "PaymentMethod" in df.columns:
    df["PaymentMethod"] = df["PaymentMethod"].fillna(
        df["PaymentMethod"].mode()[0]
    )



numerical_cols = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

numerical_cols = [
    col for col in numerical_cols
    if col in df.columns
]

imputer = KNNImputer(n_neighbors=5)

df[numerical_cols] = imputer.fit_transform(
    df[numerical_cols]
)



print("\nMissing Values After Imputation")
print(df.isnull().sum())


for col in numerical_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    df[col] = np.where(
        df[col] < lower_bound,
        lower_bound,
        df[col]
    )

    df[col] = np.where(
        df[col] > upper_bound,
        upper_bound,
        df[col]
    )

print("\nOutliers Treated Successfully")


df["RevenuePerItem"] = np.where(
    df["Quantity"] != 0,
    df["TotalPrice"] / df["Quantity"],
    0
)

df["AverageCartValue"] = np.where(
    df["ItemsInCart"] != 0,
    df["TotalPrice"] / df["ItemsInCart"],
    0
)

df["CouponUsed"] = np.where(
    df["CouponCode"].notnull(),
    1,
    0
)


df["Date"] = pd.to_datetime(df["Date"])

df["OrderMonth"] = df["Date"].dt.month

df["OrderYear"] = df["Date"].dt.year



print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe())


output_file = "Final_ML_Ready_Dataset.xlsx"

df.to_excel(
    output_file,
    index=False
)

print("\nML Ready Dataset Saved Successfully")
print(f"File Name: {output_file}")
