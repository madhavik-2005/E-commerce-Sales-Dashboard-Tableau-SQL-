
## E-Commerce Sales Dashboard

An interactive E-Commerce Sales Dashboard built using Python (Streamlit), PostgreSQL, and Tableau. This project allows users to explore sales performance, customer RFM segmentation, cohort retention, churn prediction, and forecast analysis
## 🛠 Technologies Used

* Python 3.11

* Streamlit for interactive web dashboards

* Pandas for data manipulation

* SQLAlchemy for PostgreSQL database connections

* PostgreSQL for data storage

* Scikit-learn for churn prediction

* Joblib for saving ML models

* Tableau Public for visual analytics
## 📌 Key Features

1. Revenue Overview (KPIs) – Total Sales, Total Profit

2. Top Customers – Top 10 customers by sales

3. RFM Segments – Customer segmentation based on Recency, Frequency, and Monetary value

4. Cohort Analysis – Visualize retention of customer cohorts over time

5. Churn Prediction – Predict likelihood of customer churn using Gradient Boosting

6. Sales Forecasting – Line chart showing predicted sales

6. Tableau Dashboards – Interactive charts for visual insights
## ⚙️ Setup Instructions

1️⃣ Clone the repository

    git clone <https://github.com/madhavik-2005/E-commerce-Sales-Dashboard-Tableau-SQL->
    cd e-commerce

2️⃣ Install Python dependencies

    pip install -r requirements.txt

3️⃣ Set up PostgreSQL

* Install PostgreSQL if not already installed.

* Create a database named ecommerce.

* Import the CSV files into the database:

    * sales → 10000 Sales Records.csv

* Tip: Use pgAdmin or the COPY command for importing CSVs.

4️⃣ Update DB credentials in streamlit/app.py

    from sqlalchemy import create_engine
    from urllib.parse import quote_plus

    user = "your_postgres_user"
    password = "your_postgres_password"  
    host = "localhost"
    port = "5432"
    db = "ecommerce"
    engine = create_engine(f'postgresql://{user}:{password_enc}@{host}:{port}/{db}')

5️⃣ Train Churn Model 

    python scripts/train_churn.py

* Trains a Gradient Boosting Classifier for churn prediction.

* Handles class imbalance with SMOTE.

* Saves model to models/churn_model.pkl.

6️⃣ Run Streamlit Dashboard

    streamlit run streamlit/app.py


* Open your browser at http://localhost:8501/

* View KPIs, top customers, RFM segments, and cohort analysis interactively.

7️⃣ Tableau Dashboard

* Connect Tableau Public to CSVs in the tableau/ folder.

* Create visualizations:

    * Revenue Overview (KPIs)

    * Top Customers Bar Chart

    * RFM Pie/Bar Charts

    * Cohort Heatmap

    * Forecast Line Chart

    * Optional Churn Probability Dashboard

Tip: Since Tableau Public doesn’t support PostgreSQL connection, use exported CSVs.
## 📊 Dashboard Features

1. Total Sales & Profit KPIs – Shows key business metrics at a glance

2. Top 10 Customers – Identifies revenue-generating customers

3. RFM Segmentation – Helps marketing target valuable customers

4. Cohort Analysis – Tracks customer retention over time

5. Forecast & Churn Analysis – Guides sales strategy and customer engagement
## 💡 Notes

* PostgreSQL must be running and accessible from Streamlit.

* Encode special characters in DB password using quote_plus.

* For deployment, use Streamlit Cloud and store DB credentials in secrets.toml.

* Tableau dashboards are for interactive visual exploration; Streamlit dashboard is for live KPIs and ML insights.
## 📈 Future Enhancements

* Add behavioral features to RFM for improved churn prediction.

* Include forecasting models for revenue projection.

* Add interactive filters and drill-downs in Tableau.

* Deploy on Streamlit Cloud for public access.
## 📂 References

* Streamlit Documentation

* SQLAlchemy Documentation

* PostgreSQL Documentation

* Scikit-learn Gradient Boosting
## 🏁 Conclusion

This E-Commerce Analytics project provides a complete end-to-end solution for analyzing sales and customer behavior. Using SQL, Python, Streamlit, and Tableau, the project enables:

* Efficient data extraction, transformation, and loading (ETL) from raw sales data into structured tables.

* Customer segmentation through RFM analysis and cohort analysis to understand purchasing behavior over time.

* Churn prediction using a machine learning model to identify customers at risk of leaving, helping in proactive retention strategies.

* Sales forecasting to aid in demand planning and business decision-making.

* Interactive dashboards via Streamlit and Tableau for easy visualization of KPIs, top customers, revenue trends, RFM segments, and cohort patterns.

This project demonstrates how data-driven insights can improve business strategy, enhance customer engagement, and optimize revenue.
## 🪪 License

© 2025 Madhavi. All rights reserved.

This project is licensed for personal and educational use only.
Commercial redistribution or modification without permission is prohibited.

For collaboration or commercial inquiries, please contact Madhavi directly.
