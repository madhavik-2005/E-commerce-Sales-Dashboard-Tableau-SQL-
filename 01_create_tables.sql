CREATE TABLE sales_raw (
    order_id BIGINT PRIMARY KEY,
    order_date DATE,
    ship_date DATE,
    country VARCHAR(50),
    region VARCHAR(50),
    category VARCHAR(50),
    sales_channel VARCHAR(50),
    order_priority VARCHAR(10),
    quantity INT,
    unit_price NUMERIC(12,2),
    unit_cost NUMERIC(12,2),
    sales NUMERIC(12,2),
    total_cost NUMERIC(12,2),
    profit NUMERIC(12,2)
);
