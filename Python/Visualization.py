#!/usr/bin/env python
# coding: utf-8

# In[1]:


# ============================================================
# VISUALIZATION - EXPLORATORY DATA ANALYSIS
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Visualization style
sns.set_theme(style="whitegrid")

# ------------------------------------------------------------
# LOAD CLEANED DATASET
# ------------------------------------------------------------

df_clean = pd.read_csv("RT_IOT2022_cleaned.csv")

print("=" * 70)
print("IoT CYBERSECURITY THREATS - DATA VISUALIZATION")
print("=" * 70)

print("\nCleaned Dataset Shape:", df_clean.shape)


# ============================================================
# 1. DISTRIBUTION OF NETWORK ATTACK TYPES
# ============================================================

attack_counts = (
    df_clean["attack_type"]
    .value_counts()
    .reset_index()
)

attack_counts.columns = ["Attack Type", "Count"]

plt.figure(figsize=(12, 6))

ax = sns.barplot(
    data=attack_counts,
    x="Attack Type",
    y="Count",
    hue="Attack Type",
    palette="viridis",
    legend=False
)

ax.bar_label(
    ax.containers[0],
    fmt="%.0f",
    padding=3,
    fontsize=9
)

plt.title(
    "Distribution of Network Attack Types",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Attack Type")
plt.ylabel("Number of Records")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# ============================================================
# 2. NETWORK PROTOCOL DISTRIBUTION
# ============================================================

protocol_counts = (
    df_clean["proto"]
    .value_counts()
    .head(10)
    .reset_index()
)

protocol_counts.columns = ["Protocol", "Count"]

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=protocol_counts,
    x="Protocol",
    y="Count",
    hue="Protocol",
    palette="mako",
    legend=False
)

ax.bar_label(
    ax.containers[0],
    fmt="%.0f",
    padding=3,
    fontsize=9
)

plt.title(
    "Network Protocol Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Network Protocol")
plt.ylabel("Number of Records")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()


# ============================================================
# 3. NETWORK FLOW DURATION DISTRIBUTION
# ============================================================

plt.figure(figsize=(11, 6))

sns.histplot(
    data=df_clean,
    x="flow_duration",
    bins=50,
    kde=True
)

plt.title(
    "Network Flow Duration Distribution",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Flow Duration")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# ============================================================
# 4. NUMERICAL FEATURE OUTLIER ANALYSIS USING BOXPLOTS
# ============================================================

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

for feature in available_features:

    plt.figure(figsize=(11, 4))

    sns.boxplot(
        x=df_clean[feature]
    )

    plt.title(
        f"Outlier Analysis of {feature}",
        fontsize=15,
        fontweight="bold"
    )

    plt.xlabel(feature)
    plt.tight_layout()
    plt.show()


# ============================================================
# 5. ATTACK TYPE DISTRIBUTION ACROSS NETWORK PROTOCOLS
# ============================================================

attack_protocol = pd.crosstab(
    df_clean["proto"],
    df_clean["attack_type"]
)

plt.figure(figsize=(14, 8))

sns.heatmap(
    attack_protocol,
    cmap="YlOrRd",
    linewidths=0.3
)

plt.title(
    "Attack Type Distribution Across Network Protocols",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Attack Type")
plt.ylabel("Network Protocol")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.show()


# ============================================================
# 6. CORRELATION ANALYSIS OF NUMERICAL NETWORK FEATURES
# ============================================================

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

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    center=0,
    fmt=".2f",
    linewidths=0.5
)

plt.title(
    "Correlation Analysis of Numerical Network Features",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()
plt.show()


# ============================================================
# VISUALIZATION COMPLETED
# ============================================================

print("\n" + "=" * 70)
print("ALL 6 VISUALIZATIONS COMPLETED SUCCESSFULLY")
print("=" * 70)


# In[ ]:





# In[ ]:




