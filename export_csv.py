import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
engine = create_engine('postgresql://postgres:Maha#1415@localhost:5432/ecommerce')

# List of tables you want to export
tables = ['sales', 'vw_rfm', 'vw_cohort', 'sales_forecast']

# Export each table to CSV
for table in tables:
    df = pd.read_sql(f'SELECT * FROM {table}', engine)
    df.to_csv(f'{table}.csv', index=False)
    print(f'{table}.csv created successfully!')
