DROP TABLE IF EXISTS sales;

CREATE TABLE sales AS
SELECT *,
       COALESCE(profit,0) AS gross_margin,
       'C' || order_id AS customer_id  -- create a fake customer_id for testing
FROM sales_raw;
