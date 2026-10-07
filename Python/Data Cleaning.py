#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ============================================================
# PART 2 - DATA CLEANING AND PREPROCESSING
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

file_path = "RT_IOT2022_uncleaned_practice.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("DATA CLEANING AND PREPROCESSING")
print("=" * 70)


# ------------------------------------------------------------
# 2. Create a Copy for Cleaning
# ------------------------------------------------------------

df_clean = df.copy()

print("\nOriginal Dataset Shape:", df_clean.shape)


# ------------------------------------------------------------
# 3. Standardize Column Names
# ------------------------------------------------------------

df_clean.columns = (
    df_clean.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

print("\nColumn names standardized.")


# ------------------------------------------------------------
# 4. Check Column Names
# ------------------------------------------------------------

print("\nColumn Names After Standardization:")
print(df_clean.columns.tolist())


# ------------------------------------------------------------
# 5. Remove Unnecessary Index Column
# ------------------------------------------------------------

index_columns = [
    col for col in df_clean.columns
    if col in ["unnamed:_0", "unnamed:0"]
]

if index_columns:

    df_clean = df_clean.drop(
        columns=index_columns
    )

    print("\nRemoved unnecessary index column(s):")
    print(index_columns)

else:

    print("\nNo unnecessary index column found.")


# ------------------------------------------------------------
# 6. Check Data Types
# ------------------------------------------------------------

print("\nData Types Before Cleaning:")
display(
    df_clean.dtypes.to_frame(
        name="Data Type"
    )
)


# ------------------------------------------------------------
# 7. Identify Numerical and Categorical Columns
# ------------------------------------------------------------

numeric_columns = (
    df_clean
    .select_dtypes(include=np.number)
    .columns
)

categorical_columns = (
    df_clean
    .select_dtypes(
        include=["object", "string", "category"]
    )
    .columns
)

print("\nNumber of Numerical Columns:",
      len(numeric_columns))

print("Number of Categorical Columns:",
      len(categorical_columns))


# ------------------------------------------------------------
# 8. Convert Numerical Columns Where Required
# ------------------------------------------------------------

if "flow_duration" in df_clean.columns:

    df_clean["flow_duration"] = pd.to_numeric(
        df_clean["flow_duration"],
        errors="coerce"
    )

print("\nNumerical conversion completed.")


# ------------------------------------------------------------
# 9. Check Missing Values Before Cleaning
# ------------------------------------------------------------

print("\nMissing Values Before Cleaning:")

missing_before = df_clean.isnull().sum()

missing_before_summary = pd.DataFrame({
    "Missing Values": missing_before,
    "Percentage": (
        missing_before / len(df_clean) * 100
    ).round(2)
})

display(
    missing_before_summary[
        missing_before_summary["Missing Values"] > 0
    ].sort_values(
        by="Missing Values",
        ascending=False
    )
)


# ------------------------------------------------------------
# 10. Handle Missing Numerical Values
# ------------------------------------------------------------

for col in numeric_columns:

    if df_clean[col].isnull().sum() > 0:

        median_value = df_clean[col].median()

        df_clean[col] = (
            df_clean[col]
            .fillna(median_value)
        )

print("\nMissing numerical values handled using median.")


# ------------------------------------------------------------
# 11. Handle Missing Categorical Values
# ------------------------------------------------------------

for col in categorical_columns:

    if df_clean[col].isnull().sum() > 0:

        df_clean[col] = (
            df_clean[col]
            .fillna("unknown")
        )

print("Missing categorical values handled.")


# ------------------------------------------------------------
# 12. Standardize Categorical Values
# ------------------------------------------------------------

for col in categorical_columns:

    df_clean[col] = (
        df_clean[col]
        .astype("string")
        .str.strip()
        .str.lower()
    )

print("\nCategorical values standardized.")


# ------------------------------------------------------------
# 13. Check Duplicate Records
# ------------------------------------------------------------

duplicates_before = (
    df_clean.duplicated().sum()
)

print("\nDuplicate Rows Before Removal:",
      duplicates_before)


# ------------------------------------------------------------
# 14. Remove Exact Duplicate Records
# ------------------------------------------------------------

df_clean = (
    df_clean
    .drop_duplicates()
    .copy()
)

duplicates_after = (
    df_clean.duplicated().sum()
)

print("Duplicate Rows After Removal:",
      duplicates_after)


# ------------------------------------------------------------
# 15. Check Negative Values
# ------------------------------------------------------------

print("\nNegative Value Analysis:")

important_columns = [
    "flow_duration",
    "fwd_pkts_tot",
    "bwd_pkts_tot"
]

for col in important_columns:

    if col in df_clean.columns:

        negative_count = (
            df_clean[col] < 0
        ).sum()

        print(
            f"{col}: {negative_count} negative values"
        )


# ------------------------------------------------------------
# 16. IQR Outlier Detection
#     Outliers are identified but NOT removed.
# ------------------------------------------------------------

if "flow_duration" in df_clean.columns:

    Q1 = df_clean["flow_duration"].quantile(0.25)
    Q3 = df_clean["flow_duration"].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - (1.5 * IQR)
    upper_bound = Q3 + (1.5 * IQR)

    outlier_condition = (
        (df_clean["flow_duration"] < lower_bound) |
        (df_clean["flow_duration"] > upper_bound)
    )

    outlier_count = (
        outlier_condition.sum()
    )

    print("\nFlow Duration Outlier Analysis")
    print("--------------------------------")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Potential Outliers:", outlier_count)

    # Important:
    # Outliers are not removed because extreme
    # network traffic values may represent
    # legitimate IoT traffic behaviour.


# ------------------------------------------------------------
# 17. Check Missing Values After Cleaning
# ------------------------------------------------------------

print("\nMissing Values After Cleaning:")

total_missing = (
    df_clean.isnull().sum().sum()
)

print(
    "Total Missing Values:",
    total_missing
)


# ------------------------------------------------------------
# 18. Check Duplicate Values After Cleaning
# ------------------------------------------------------------

print("\nDuplicate Rows After Cleaning:")

print(
    "Duplicate Rows:",
    df_clean.duplicated().sum()
)


# ------------------------------------------------------------
# 19. Final Dataset Shape
# ------------------------------------------------------------

print("\nFinal Dataset Shape:")
print(df_clean.shape)


# ------------------------------------------------------------
# 20. Final Dataset Information
# ------------------------------------------------------------

print("\nFinal Dataset Information:")

df_clean.info()


# ------------------------------------------------------------
# 21. Final Missing Value Verification
# ------------------------------------------------------------

print("\nFinal Missing Value Verification:")

if df_clean.isnull().sum().sum() == 0:

    print("✓ No missing values remain.")

else:

    print(
        "Missing values remain:",
        df_clean.isnull().sum().sum()
    )


# ------------------------------------------------------------
# 22. Final Duplicate Verification
# ------------------------------------------------------------

print("\nFinal Duplicate Verification:")

if df_clean.duplicated().sum() == 0:

    print("✓ No duplicate rows remain.")

else:

    print(
        "Duplicate rows remain:",
        df_clean.duplicated().sum()
    )


# ------------------------------------------------------------
# 23. Final Cleaned Dataset Preview
# ------------------------------------------------------------

print("\nFinal Cleaned Dataset - First 5 Records:")

display(
    df_clean.head()
)


# ------------------------------------------------------------
# 24. Save Cleaned Dataset
# ------------------------------------------------------------

output_file = "RT_IOT2022_cleaned.csv"

df_clean.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 70)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 70)

print("Final Rows       :", df_clean.shape[0])
print("Final Columns    :", df_clean.shape[1])
print("Missing Values   :", df_clean.isnull().sum().sum())
print("Duplicate Rows   :", df_clean.duplicated().sum())

print("\nCleaned CSV saved as:")
print(output_file)


# In[ ]:




