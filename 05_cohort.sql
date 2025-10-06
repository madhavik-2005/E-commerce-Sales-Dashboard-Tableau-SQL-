-- Cohort Analysis
CREATE OR REPLACE VIEW vw_cohort AS
WITH customer_cohort AS (
    SELECT customer_id,
           DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM sales
    GROUP BY customer_id
),
orders_by_month AS (
    SELECT customer_id,
           DATE_TRUNC('month', order_date) AS order_month
    FROM sales
)
SELECT c.cohort_month,
       o.order_month,
       COUNT(DISTINCT o.customer_id) AS active_customers,
       DATE_PART('month', AGE(o.order_month, c.cohort_month)) + 1 AS cohort_index
FROM customer_cohort c
JOIN orders_by_month o ON c.customer_id = o.customer_id
GROUP BY c.cohort_month, o.order_month
ORDER BY c.cohort_month, o.order_month;
