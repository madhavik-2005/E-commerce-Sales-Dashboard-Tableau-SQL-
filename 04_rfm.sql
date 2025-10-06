-- RFM Segmentation
CREATE OR REPLACE VIEW vw_rfm AS
WITH rfm AS (
    SELECT customer_id,
           MAX(order_date) AS last_order_date,
           COUNT(*) AS frequency,
           SUM(sales) AS monetary
    FROM sales
    GROUP BY customer_id
),
rfm_score AS (
    SELECT *,
           NTILE(5) OVER (ORDER BY last_order_date DESC) AS recency_score,
           NTILE(5) OVER (ORDER BY frequency DESC) AS frequency_score,
           NTILE(5) OVER (ORDER BY monetary DESC) AS monetary_score
    FROM rfm
)
SELECT *,
       (recency_score + frequency_score + monetary_score) AS rfm_total,
       CASE
           WHEN (recency_score + frequency_score + monetary_score) >= 12 THEN 'Champions'
           WHEN monetary_score >= 4 THEN 'Loyal Customers'
           ELSE 'Needs Attention'
       END AS segment
FROM rfm_score;
