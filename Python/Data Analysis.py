#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ============================================================
# DATA ANALYSIS - EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

import pandas as pd
import numpy as np

# ------------------------------------------------------------
# LOAD THE CLEANED DATASET
# ------------------------------------------------------------

df_clean = pd.read_csv("RT_IOT2022_cleaned.csv")

print("=" * 70)
print("EXPLORATORY DATA ANALYSIS OF IoT CYBERSECURITY THREATS")
print("=" * 70)

print("\nCleaned Dataset Shape:", df_clean.shape)


# ============================================================
# 1. DISTRIBUTION OF NETWORK ATTACK TYPES
# ============================================================

print("\n" + "=" * 70)
print("1. DISTRIBUTION OF NETWORK ATTACK TYPES")
print("=" * 70)

attack_counts = df_clean["attack_type"].value_counts()

attack_summary = pd.DataFrame({
    "Number of Records": attack_counts,
    "Percentage": (
        df_clean["attack_type"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
    )
})

print("\nTotal Attack Categories:",
      df_clean["attack_type"].nunique())

display(attack_summary)

print("\nMost Frequently Represented Attack Type:")
print(attack_counts.idxmax(),
      "->", attack_counts.max(), "records")

print("\nLeast Frequently Represented Attack Type:")
print(attack_counts.idxmin(),
      "->", attack_counts.min(), "records")


# ============================================================
# 2. NETWORK PROTOCOL DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("2. NETWORK PROTOCOL DISTRIBUTION")
print("=" * 70)

protocol_counts = df_clean["proto"].value_counts()

print("\nTotal Unique Network Protocols:",
      df_clean["proto"].nunique())

print("\nProtocol Distribution:")
display(
    protocol_counts.to_frame(name="Number of Records")
)

print("\nTop 10 Network Protocols:")
display(
    protocol_counts.head(10)
    .to_frame(name="Number of Records")
)


# ============================================================
# 3. NETWORK FLOW DURATION DISTRIBUTION
# ============================================================

print("\n" + "=" * 70)
print("3. NETWORK FLOW DURATION DISTRIBUTION")
print("=" * 70)

flow_duration_stats = df_clean["flow_duration"].describe()

print("\nFlow Duration Statistical Summary:")
display(
    flow_duration_stats.to_frame(name="Value")
)

print("\nFlow Duration Mean:",
      round(df_clean["flow_duration"].mean(), 4))

print("Flow Duration Median:",
      round(df_clean["flow_duration"].median(), 4))

print("Flow Duration Standard Deviation:",
      round(df_clean["flow_duration"].std(), 4))

print("Flow Duration Skewness:",
      round(df_clean["flow_duration"].skew(), 4))


# ============================================================
# 4. NUMERICAL FEATURE OUTLIER ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("4. NUMERICAL FEATURE OUTLIER ANALYSIS")
print("=" * 70)

numerical_features = [
    "flow_duration",
    "fwd_pkts_tot",
    "bwd_pkts_tot",
    "flow_pkts_per_sec",
    "payload_bytes_per_second",
    "down_up_ratio"
]

available_features = [
    feature
    for feature in numerical_features
    if feature in df_clean.columns
]

outlier_results = []

for feature in available_features:

    Q1 = df_clean[feature].quantile(0.25)
    Q3 = df_clean[feature].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outlier_condition = (
        (df_clean[feature] < lower_bound) |
        (df_clean[feature] > upper_bound)
    )

    outlier_count = outlier_condition.sum()

    outlier_percentage = (
        outlier_count / len(df_clean) * 100
    )

    outlier_results.append({
        "Feature": feature,
        "Q1": Q1,
        "Q3": Q3,
        "IQR": IQR,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound,
        "Potential Outliers": outlier_count,
        "Outlier Percentage": round(outlier_percentage, 2)
    })

outlier_summary = pd.DataFrame(outlier_results)

print("\nIQR-Based Outlier Summary:")
display(outlier_summary)

print(
    "\nNote: Potential outliers are identified but not removed "
    "because extreme network traffic values may represent "
    "legitimate or security-relevant behaviour."
)


# ============================================================
# 5. ATTACK TYPE DISTRIBUTION ACROSS NETWORK PROTOCOLS
# ============================================================

print("\n" + "=" * 70)
print("5. ATTACK TYPE DISTRIBUTION ACROSS NETWORK PROTOCOLS")
print("=" * 70)

attack_protocol = pd.crosstab(
    df_clean["proto"],
    df_clean["attack_type"]
)

print("\nAttack Type vs Network Protocol Cross-Tabulation:")
display(attack_protocol)

protocol_attack_summary = attack_protocol.copy()

protocol_attack_summary["Total Records"] = (
    protocol_attack_summary.sum(axis=1)
)

protocol_attack_summary = protocol_attack_summary.sort_values(
    "Total Records",
    ascending=False
)

print("\nProtocol-Wise Attack Summary:")
display(protocol_attack_summary)


# ============================================================
# 6. CORRELATION ANALYSIS OF NUMERICAL NETWORK FEATURES
# ============================================================

print("\n" + "=" * 70)
print("6. CORRELATION ANALYSIS OF NUMERICAL NETWORK FEATURES")
print("=" * 70)

selected_features = [
    "flow_duration",
    "fwd_pkts_tot",
    "bwd_pkts_tot",
    "flow_pkts_per_sec",
    "payload_bytes_per_second",
    "down_up_ratio"
]

available_correlation_features = [
    feature
    for feature in selected_features
    if feature in df_clean.columns
]

correlation_matrix = df_clean[
    available_correlation_features
].corr(numeric_only=True)

print("\nCorrelation Matrix:")
display(correlation_matrix.round(3))


# ============================================================
# FINAL EDA SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("EDA ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("""
Analyses performed:

1. Distribution of Network Attack Types
2. Network Protocol Distribution
3. Network Flow Duration Distribution
4. Numerical Feature Outlier Analysis
5. Attack Type Distribution Across Network Protocols
6. Correlation Analysis of Numerical Network Features
""")

print("=" * 70)


# In[ ]:




