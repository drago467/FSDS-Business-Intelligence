SELECT
    order_id,
    customer_id,
    DATE(order_date) AS order_date,
    total_amount,
    status
FROM
    sample_datawarehouse.orders
WHERE
    status != 'cancelled'
