# Exploratory Data Analysis of IoT Security Threats and Attack Patterns

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the RT-IOT2022 dataset to investigate IoT network traffic characteristics and patterns associated with different cybersecurity attack categories.

The project covers data understanding, data cleaning, preprocessing, statistical analysis, and visualization of network attack types, communication protocols, flow duration, potential numerical outliers, attack distribution across protocols, and correlations between numerical network features.

**Sprint:** Sprint 1 — Data Understanding, Data Cleaning and Exploratory Data Analysis  
**Industry:** Internet of Things (IoT) Cybersecurity

---

## Problem Statement

IoT networks generate diverse network traffic from multiple devices, protocols, and services. Malicious activities can exhibit different traffic patterns, making cybersecurity threat analysis challenging.

The RT-IOT2022 dataset contains network traffic records representing different attack categories and multiple network-level features. Systematic inspection, cleaning, and exploratory analysis are required to understand the data quality and identify patterns in attack categories, protocols, traffic behavior, potential outliers, and relationships between network features.

This project analyzes the dataset to develop a data-driven understanding of IoT network traffic and provide a foundation for further feature engineering, feature selection, and advanced cybersecurity analysis in Sprint 2.

---

## Project Objectives

- Understand the structure and characteristics of the RT-IOT2022 dataset.
- Assess data quality and identify missing values and duplicate records.
- Handle missing values and duplicate records during preprocessing.
- Standardize inconsistent categorical values and prepare data for analysis.
- Analyze the distribution of IoT attack types and network protocols.
- Examine network flow duration and packet-related characteristics.
- Identify potential outliers in selected numerical network features.
- Examine relationships and correlations between numerical network features.
- Present findings using statistical summaries and visualizations.

---

## Dataset

**Dataset Name:** RT-IOT2022 Dataset

The dataset contains network traffic observations with numerical and categorical features related to communication protocols, services, packet counts, flow characteristics, traffic rates, and attack categories.

**Dataset Source:** The notebook identifies the dataset as RT-IOT2022 but does not provide an external source URL. Add the verified dataset source link when available.

### Important Features

| Feature | Description |
|---|---|
| `proto` | Network communication protocol |
| `service` | Network service associated with the traffic |
| `flow_duration` | Duration of the network flow |
| `fwd_pkts_tot` | Total number of forward packets |
| `bwd_pkts_tot` | Total number of backward packets |
| `flow_pkts_per_sec` | Number of packets transmitted per second |
| `payload_bytes_per_second` | Payload transmission rate |
| `down_up_ratio` | Ratio between download and upload traffic |
| `attack_type` | Category of network traffic or cyber attack |

---

## Tools and Technologies

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

## Project Workflow

**Industry Selection → Problem Identification → Dataset Collection → Data Cleaning → Data Transformation → Data Analysis → Data Visualization → Insights → Recommendations**

### Sprint 1 Workflow

1. Problem Definition
2. Data Collection
3. Data Understanding
4. Data Quality Assessment
5. Data Cleaning and Preprocessing
6. Exploratory Data Analysis
7. Data Visualization
8. Interpretation of Findings

---

## Data Cleaning and Preprocessing

The project includes the following data preparation activities:

- Dataset structure and data-type inspection
- Missing-value identification and handling
- Duplicate record identification and removal
- Categorical text standardization
- Numerical data-type checking and conversion where required
- Invalid-value checking
- IQR-based outlier investigation
- Column-name standardization
- Final dataset validation

Potential outliers were investigated rather than automatically removed, since extreme network traffic values may represent meaningful traffic behavior.

### Final Dataset Status

- **Records:** 118,088
- **Features:** 84
- **Remaining missing values:** 0
- **Remaining exact duplicate rows:** 0

---

## Data Analysis and Visualization

### 1. Attack Type Distribution

Examines the frequency of attack categories represented in the dataset.

<img width="882" height="428" alt="Distribution of IoT Attack Types" src="https://github.com/user-attachments/assets/adf4fd75-4315-4eb4-9a89-b44195e5ec1d" />

### 2. Network Protocol Distribution

Examines the distribution of network communication protocols in the observed traffic.

<img width="887" height="532" alt="Network Protocol Distribution" src="https://github.com/user-attachments/assets/f3f55d77-87d0-46a2-a1ff-b01149e12b84" />

### 3. Network Flow Duration Distribution

Explores the distribution and variability of network flow durations.

<img width="883" height="527" alt="Distribution of Network Flow Duration " src="https://github.com/user-attachments/assets/e2a521f5-abbb-451e-8c11-4c558d809927" />

### 4. Numerical Feature Outlier Analysis

Uses a boxplot to inspect potential extreme observations in flow duration. The notebook also includes IQR-based outlier analysis for selected numerical network features.

<img width="842" height="315" alt="outlier analysis of flow duration " src="https://github.com/user-attachments/assets/a8263766-b4b3-43c4-ac7d-aa90d3ff4436" />

### 5. Attack Type Distribution Across Network Protocols

Uses a heatmap to compare the distribution of attack categories across network protocols.

<img width="880" height="436" alt="Attack Types Across Network Protocols" src="https://github.com/user-attachments/assets/25ae5b0b-fcb2-4364-972f-eae41bb042da" />


### 6. Correlation Analysis of Numerical Network Features

Uses a correlation heatmap to examine relationships among selected numerical network features.

<img width="890" height="650" alt="Correlation Between Network Traffic Features" src="https://github.com/user-attachments/assets/2134eb64-f780-4701-922a-6a0a2afa3321" />

### 7. Flow Duration Across Attack Categories

Compares flow-duration characteristics across attack categories using a boxplot.

<img width="892" height="465" alt="Flow Duration Across IoT Attack Categories" src="https://github.com/user-attachments/assets/fdd6fdf6-104a-4373-b735-dafc4ac7a7c4" />


---

## Key Insights

The notebook's analysis and written findings cover these observations:

- Attack categories have different levels of representation in the dataset.
- Network traffic is distributed across multiple communication protocols.
- Flow duration varies across traffic observations and includes potentially unusual short- and long-duration flows.
- Selected numerical network features contain potential extreme observations.
- The distribution of attack categories differs across network protocols.
- Numerical network features exhibit varying levels of correlation.
- Traffic characteristics can vary across attack categories.

Detailed statistical results are available in the notebook outputs.

---

## Recommendations and Future Scope

The following are proposed next steps for further investigation:

1. Perform feature engineering on packet, byte, duration, and traffic-rate attributes.
2. Apply feature selection to identify informative network features.
3. Investigate attack-specific traffic characteristics in greater depth.
4. Examine class imbalance before building machine learning models.
5. Explore attack classification and anomaly detection in Sprint 2.
6. Compare machine learning models using appropriate evaluation metrics if modelling is undertaken.

These are proposed future steps, not results claimed as completed in Sprint 1.

---

## Project Folder Structure

```text
IoT_Cybersecurity_EDA/
│
├── README.md
│
├── Notebook/
│   └── Data_Analysis_EDA_Mahumidhaa_A_P.ipynb
│
└── Visualizations/
    ├── attack_type_distribution.png
    ├── network_protocol_distribution.png
    ├── flow_duration_distribution.png
    ├── flow_duration_boxplot.png
    ├── attack_type_protocol_heatmap.png
    ├── correlation_heatmap.png
    └── attack_category_flow_duration.png
```

---

## Author

- **Name:** Madhumidhaa A P
- **Student ID:** AF05308674
- **Organization:** Anudip Foundation
- **Course:** AIML
- **Batch Code:** ANP-D7444

---

## References

- **Dataset:** RT-IOT2022 Dataset
- **Tools:** Python, Jupyter Notebook, NumPy, Pandas, Matplotlib, Seaborn
- **Methods:** Data cleaning, exploratory data analysis, statistical analysis, data visualization, correlation analysis, and outlier analysis
