-- Q1
-- Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

WITH table1 AS (SELECT s.name rep, r.name region, sum(o.total_amt_usd) AS total_sales
        FROM sales_reps s
        JOIN accounts a
        ON a.sales_rep_id = s.id
        JOIN orders o
        ON o.account_id = a.id
        JOIN region r
        ON r.id = s.region_id
        GROUP BY s.name, r.name),

    table2 AS (SELECT region, max(total_sales) as max_total_sales
    FROM table1
    GROUP BY region)

-- get each region's max sales
SELECT table1.rep, table1.region, table1.total_sales 
FROM
    table2
JOIN
-- get each sales rep's total sales with region names
    table1
ON table1.region = table2.region AND table1.total_sales = table2.max_total_sales;

