import pandas as pd
from prophet import Prophet
from sqlalchemy import create_engine

# DB connection
engine = create_engine('postgresql://postgres:Maha#1415@localhost:5432/ecommerce')

# Aggregate daily sales
df = pd.read_sql("SELECT order_date, SUM(sales) as total_sales FROM sales GROUP BY order_date", engine)
df.rename(columns={'order_date':'ds','total_sales':'y'}, inplace=True)

# Train Prophet model
m = Prophet(yearly_seasonality=True, weekly_seasonality=True)
m.fit(df)

# Forecast next 30 days
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)

# Save to DB
forecast[['ds','yhat','yhat_lower','yhat_upper']].to_sql('sales_forecast', engine, if_exists='replace', index=False)
print("Sales forecast completed!")
