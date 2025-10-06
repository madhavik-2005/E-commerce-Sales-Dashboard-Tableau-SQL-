import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:Maha#1415@localhost:5432/ecommerce')
df = pd.read_csv('data/10000 Sales Records.csv')

# Clean columns
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Convert dates
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

# Drop rows with invalid dates
df = df.dropna(subset=['order_date','ship_date'])

# Convert numeric columns
num_cols = ['order_id','units_sold','unit_price','unit_cost','total_revenue','total_cost','total_profit']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Rename columns to match DB table
df = df.rename(columns={
    'order_id':'order_id',
    'order_date':'order_date',
    'ship_date':'ship_date',
    'country':'country',
    'region':'region',
    'item_type':'category',
    'sales_channel':'sales_channel',
    'order_priority':'order_priority',
    'units_sold':'quantity',
    'unit_price':'unit_price',
    'unit_cost':'unit_cost',
    'total_revenue':'sales',
    'total_cost':'total_cost',
    'total_profit':'profit'
})

# Load into DB
df.to_sql('sales_raw', engine, if_exists='replace', index=False)
print("Data loaded successfully!")
