#!/usr/bin/env python
# coding: utf-8

# In[4]:


# ============================================================
# PART 1 - DATA LOADING AND INITIAL DATA INSPECTION
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

file_path = "RT_IOT2022_uncleaned_practice.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("DATA LOADING AND INITIAL DATA INSPECTION")
print("=" * 70)

print("\nDataset loaded successfully!")


# ------------------------------------------------------------
# 2. Shape
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("1. DATASET SHAPE")
print("-" * 70)

print("Number of Rows    :", df.shape[0])
print("Number of Columns :", df.shape[1])
print("Shape             :", df.shape)


# ------------------------------------------------------------
# 3. Head
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("2. FIRST FIVE RECORDS")
print("-" * 70)

display(df.head())


# ------------------------------------------------------------
# 4. Tail
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("3. LAST FIVE RECORDS")
print("-" * 70)

display(df.tail())


# ------------------------------------------------------------
# 5. Random Sample
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("4. RANDOM SAMPLE OF RECORDS")
print("-" * 70)

display(df.sample(5))


# ------------------------------------------------------------
# 6. Info
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("5. DATASET INFORMATION")
print("-" * 70)

df.info()


# ------------------------------------------------------------
# 7. Data Types
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("6. DATA TYPES OF FEATURES")
print("-" * 70)

display(
    df.dtypes.to_frame(name="Data Type")
)


# ------------------------------------------------------------
# 8. Numerical Description
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("7. DESCRIPTIVE STATISTICS - NUMERICAL FEATURES")
print("-" * 70)

display(df.describe())


# ------------------------------------------------------------
# 9. Categorical Description
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("8. DESCRIPTIVE STATISTICS - CATEGORICAL FEATURES")
print("-" * 70)

display(
    df.describe(include="str")
)


# ------------------------------------------------------------
# 10. Missing Values
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("9. MISSING VALUE ANALYSIS")
print("-" * 70)

missing_values = df.isnull().sum()

missing_summary = pd.DataFrame({
    "Missing Values": missing_values,
    "Missing Percentage": (
        missing_values / len(df) * 100
    ).round(2)
})

display(
    missing_summary[
        missing_summary["Missing Values"] > 0
    ].sort_values(
        by="Missing Values",
        ascending=False
    )
)


# ------------------------------------------------------------
# 11. Duplicate Records
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("10. DUPLICATE RECORD ANALYSIS")
print("-" * 70)

duplicate_count = df.duplicated().sum()

print("Number of Duplicate Rows:", duplicate_count)


# ------------------------------------------------------------
# 12. Unique Values
# ------------------------------------------------------------

print("\n" + "-" * 70)
print("11. UNIQUE VALUE ANALYSIS")
print("-" * 70)

unique_summary = pd.DataFrame({
    "Column": df.columns,
    "Unique Values": [
        df[col].nunique()
        for col in df.columns
    ]
})

display(unique_summary)


# ------------------------------------------------------------
# 13. Dataset Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("INITIAL DATA INSPECTION COMPLETED")
print("=" * 70)

print("Rows              :", df.shape[0])
print("Columns           :", df.shape[1])
print("Total Missing     :", df.isnull().sum().sum())
print("Duplicate Rows     :", df.duplicated().sum())
print("Numerical Columns :", len(df.select_dtypes(include=np.number).columns))
print("Categorical Columns:", len(
    df.select_dtypes(include=["object", "string", "category"]).columns
))


# In[ ]:




