-- Find the sales in terms of total dollars for all orders in each year, ordered from greatest to least. Do you notice any trends in the yearly sales totals?
SELECT DATE_PART('year', occurred_at) sales_year, SUM(total_amt_usd) yearly_total
FROM orders
GROUP BY 1
ORDER BY 2 DESC


-- Which month did Parch & Posey have the greatest sales in terms of total dollars? Are all months evenly represented by the dataset?
SELECT DATE_TRUNC('month', occurred_at) sales_month, SUM(total_amt_usd) total
FROM orders
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

SELECT month_period, COUNT(*) month_count
FROM
(SELECT DATE_TRUNC('month', occurred_at) month_period
FROM orders
GROUP BY 1) AS table1
GROUP BY month_period
ORDER BY month_count;

-- Which year did Parch & Posey have the greatest sales in terms of total number of orders? Are all years evenly represented by the dataset?
SELECT DATE_PART('year', occurred_at) sales_month, SUM(total_amt_usd) total
FROM orders
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- Which month did Parch & Posey have the greatest sales in terms of total number of orders? Are all months evenly represented by the dataset?
SELECT DATE_TRUNC('month', occurred_at) sales_month, SUM(total) total
FROM orders
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- In which month of which year did Walmart spend the most on gloss paper in terms of dollars?
SELECT DATE_PART('month', o.occurred_at) month_name, DATE_PART('year', o.occurred_at) year_name, SUM(o.gloss_amt_usd)
FROM orders o
JOIN accounts a
ON a.id = o.account_id
WHERE a.name = 'Walmart'
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 1;