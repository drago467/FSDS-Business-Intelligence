{{ config(
    materialized='table'
) }}

SELECT 
    s.*, 
    c.FirstName, 
    c.MiddleName, 
    c.LastName
FROM
    {{ source('sample_datawarehouse', 'DimCustomer') }} c
JOIN
    {{ source('sample_datawarehouse', 'FactInternetSales') }} s
ON
    c.CustomerKey = s.CustomerKey
