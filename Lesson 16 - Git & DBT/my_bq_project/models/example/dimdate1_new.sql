{{ config(materialized='table') }}

SELECT
    *
FROM {{ ref('DimDate1') }}
WHERE DayNumberOfWeek = 1
