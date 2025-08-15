{{ config(materialized='table') }}

SELECT
    e.EmployeeKey
FROM {{ ref('DimEmployee1') }} e
UNION ALL
SELECT
    d.DateKey
FROM {{ ref('DimDate1') }} d

