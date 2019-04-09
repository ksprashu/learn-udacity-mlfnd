-- Q1
-- Provide the name of the sales_rep in each region with the largest amount of total_amt_usd sales.

-- get each region's max sales
SELECT t1.rep, t1.region, t1.total_sales 
FROM
    (SELECT region, max(total_sales) as max_total_sales
    FROM 
        (SELECT s.name rep, r.name region, sum(o.total_amt_usd) AS total_sales
        FROM sales_reps s
        JOIN accounts a
        ON a.sales_rep_id = s.id
        JOIN orders o
        ON o.account_id = a.id
        JOIN region r
        ON r.id = s.region_id
        GROUP BY s.name, r.name) AS t2
    GROUP BY region) AS t3
JOIN
-- get each sales rep's total sales with region names
(SELECT s.name rep, r.name region, sum(o.total_amt_usd) AS total_sales
FROM sales_reps s
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
JOIN region r
ON r.id = s.region_id
GROUP BY s.name, r.name) AS t1
ON t1.region = t3.region AND t1.total_sales = t3.max_total_sales;


-- Q2
-- For the region with the largest (sum) of sales total_amt_usd, how many total (count) orders were placed? 
SELECT r.name region_name, SUM(o.total_amt_usd) as total_amount, COUNT(o.total_amt_usd) as orders_count
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
JOIN accounts a
ON a.sales_rep_id = s.id
JOIN orders o
ON o.account_id = a.id
GROUP BY 1
ORDER BY 2 DESC


-- Q3
-- For the name of the account that purchased the most (in total over their lifetime as a customer) standard_qty paper, how many accounts still had more in total purchases? 

-- get the total std qty per account name
SELECT a.name account_name, SUM(standard_qty) total_std_qty, SUM(standard_qty) + SUM(gloss_qty) + SUM(poster_qty) AS total_qty
FROM accounts a
JOIN orders o
ON o.account_id = a.id
GROUP BY 1

-- actual query
SELECT COUNT(*) total_count
FROM
-- get the total std qty per account name
    (SELECT SUM(standard_qty) + SUM(gloss_qty) + SUM(poster_qty) AS total_qty
    FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
    GROUP BY a.name) t1
WHERE total_qty > 
    (SELECT SUM(standard_qty) total_std_qty
    FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
    GROUP BY a.name
    ORDER BY 1 DESC
    LIMIT 1);


-- Q4
-- For the customer that spent the most (in total over their lifetime as a customer) total_amt_usd, how many web_events did they have for each channel?

-- get the max of the spends of each customer
SELECT w.channel, COUNT(*) channel_count
FROM web_events w
WHERE w.account_id = 
(-- get the customer id with the max spend 
SELECT id FROM
    (-- get spends of each customer and get max of that
    SELECT a.id, SUM(o.total_amt_usd) as total_spend
    FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 1) t1
)
GROUP BY 1
ORDER BY 2

-- Q5
-- What is the lifetime average amount spent in terms of total_amt_usd for the top 10 total spending accounts?
SELECT AVG(total_spend) FROM
(-- get spends of each customer and get max of that
    SELECT a.id, SUM(o.total_amt_usd) as total_spend
    FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 10
) t1


-- Q6
-- What is the lifetime average amount spent in terms of total_amt_usd for only the companies that spent more than the average of all orders.

-- find average of all orders per customer
SELECT AVG(total_spend) average_spend FROM
    (-- get spends of each customer
    SELECT a.id, SUM(o.total_amt_usd) as total_spend
        FROM accounts a
        JOIN orders o
        ON o.account_id = a.id
        GROUP BY 1
    ) t1