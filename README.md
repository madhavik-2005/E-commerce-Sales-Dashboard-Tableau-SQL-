🏗 Project Structure

e-commerce/
├─ data/ – CSV datasets for analysis
│   ├─ 10000 Sales Records.csv – Raw sales data
│   ├─ vw_rfm.csv – RFM (Recency, Frequency, Monetary) customer data
│   ├─ vw_cohort.csv – Cohort analysis data
│   └─ sales_forecast.csv – Sales forecasting data

├─ models/ – Saved machine learning models
│   └─ churn_model.pkl – Pre-trained churn prediction model

├─ scripts/ – Python scripts for ETL and model training
│   ├─ etl.py – Extract, Transform, Load (ETL) script for database
│   ├─ train_churn.py – Train churn prediction model
│   └─ train_forecast.py – Train sales forecasting model

├─ sql/ – SQL scripts for database operations
│   ├─ 01_create_tables.sql – Create database tables
│   ├─ 02_load_data.sql – Load CSV data into tables
│   ├─ 03_transformations.sql – Data cleaning and transformations
│   ├─ 04_rfm.sql – RFM table creation
│   └─ 05_cohort.sql – Cohort table creation

├─ streamlit/ – Streamlit dashboard app
│   └─ app.py – Interactive E-Commerce dashboard

├─ tableau/ – Files for Tableau visualization
│   ├─ export_csv.py – Script to export data for Tableau
│   ├─ vw_rfm.csv – RFM dataset for Tableau
│   ├─ sales_forecast.csv – Forecast dataset for Tableau
│   └─ vw_cohort.csv – Cohort dataset for Tableau

├─ requirements.txt – Python dependencies
└─ README.md – Project documentation
