{{ config(
    materialized='table'
) }}

SELECT s.*, c.FirstName, c.MiddleName, c.LastName
FROM
    `fsds-bi.sample_datawarehouse.DimCustomer` c
JOIN
    `fsds-bi.sample_datawarehouse.FactInternetSales` s
ON
    c.CustomerKey = s.CustomerKey

