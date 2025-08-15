{{ config(materialized='table') }}

SELECT
    SUM(total_amount) AS total_revenue
FROM
    {{ ref('stg_orders') }}
