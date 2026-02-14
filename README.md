# Logistics Delay Analytics Pipeline

## Project Overview
This project implements an end-to-end logistics data analytics pipeline designed to analyze shipment delays, identify operational risk factors, and predict potential delays using machine learning. The pipeline follows real-world data engineering practices such as metadata-driven ingestion, structured data processing, automated orchestration, and business intelligence reporting.

The project simulates how logistics and supply chain organizations monitor delivery performance and make data-driven operational decisions.

---

## Business Problem
Logistics delays increase operational costs, reduce customer satisfaction, and disrupt supply chains. Organizations require analytics systems to:
- Identify delay-prone routes and carriers
- Monitor shipment performance trends
- Predict potential delays in advance
- Support decision-making using dashboards

This project addresses these challenges by combining data engineering, analytics, and machine learning into a single automated pipeline.

---

## Solution Overview
The pipeline processes logistics data through the following stages:
1. Data ingestion using a metadata-driven manifest
2. Data cleaning and transformation using Pandas
3. Machine learning model for delay prediction
4. Pipeline orchestration with logging
5. Visualization using Power BI dashboards

---

## Architecture
CSV Data Sources  
→ Ingestion Layer  
→ Data Processing Layer  
→ Machine Learning Layer  
→ Analytics & Visualization Layer  

This architecture reflects common industry patterns used in batch analytics pipelines.

---

## Technology Stack

### Programming & Analytics
- Python
- Pandas
- NumPy
- Scikit-learn

### Data Engineering
- Metadata-driven ingestion using CSV manifest
- Pipeline orchestration using Python
- Structured logging

### Visualization
- Power BI Desktop

---

## Project Structure
logistics-bigdata-project/
│
├── scripts/
│ ├── ingest_files.py
│ ├── step2_pandas_process.py
│ └── step3_ml_delay_model.py
│
├── ingestion_manifest.csv
├── run_pipeline.py
├── pipeline_run.log
├── logistics_delay_dashboard.pbix
└── README.md


## Pipeline Components

### Data Ingestion
Uses a manifest-based ingestion approach to track data sources and ingestion status. This design mirrors enterprise ETL pipelines and improves traceability and reliability.

### Data Processing
Raw logistics data is cleaned, transformed, and prepared for analysis using Pandas.

### Machine Learning
A machine learning model is trained to predict shipment delays based on historical logistics data. Model evaluation metrics are generated to assess performance.

### Pipeline Orchestration
The pipeline is orchestrated using `run_pipeline.py`, which:
- Executes each step sequentially
- Logs execution timestamps and status
- Stops execution if any step fails

### Analytics Dashboard
Processed data is visualized in Power BI to analyze delay trends, route performance, and carrier efficiency.

---

## How to Run the Project

### Prerequisites
- Python 3.x
- Required Python libraries installed
- Power BI Desktop (for viewing the dashboard)



#####Cleaned and processed logistics dataset

Trained machine learning model

Pipeline execution logs

Interactive Power BI dashboard

Cloud Architecture Mapping

The local implementation aligns with cloud-based data platforms:

Local Component	Cloud Equivalent
CSV Data Files	AWS S3 / Azure Blob Storage
Python Scripts	AWS Glue / Azure Databricks
Pipeline Orchestration	Apache Airflow
Power BI Desktop	Power BI Service
Key Learning Outcomes

End-to-end data pipeline design

Metadata-driven data ingestion

Data transformation using Pandas

Machine learning integration

Pipeline orchestration and logging

Business intelligence reporting

Future Enhancements

Deploy the pipeline on AWS or Azure

Schedule workflows using Apache Airflow

Add real-time streaming using Kafka

Improve model accuracy with feature engineering

Automate dashboard refresh using Power BI Service

Author

Sourav K
Final Year BCA Student
Focus Areas: Data Science, Analytics, Data Engineering, Machine Learning


## How to Run the Project

### Prerequisites
- Python 3.x
- Required Python libraries installed
- Power BI Desktop (for viewing the dashboard)

### Run Command
```bash
python run_pipeline.py


###3Logs
###Pipeline execution details are stored in:

pipeline_run.logOutputs
