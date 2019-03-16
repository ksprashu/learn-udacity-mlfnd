-- Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order.
SELECT a.name, MIN(o.occurred_at) AS order_date
FROM orders AS o
    JOIN accounts AS a
    ON o.account_id = a.id
GROUP BY a.name, o.occurred_at
ORDER BY o.occurred_at;

-- Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name.
SELECT a.name, SUM(o.total_amt_usd)
FROM orders AS o
    JOIN accounts AS a
    ON a.id = o.account_id
GROUP BY a.name
ORDER by a.name;

-- Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name.
SELECT MAX(w.occurred_at), w.channel, a.name
FROM web_events w
    JOIN accounts a
    ON w.account_id = a.id
GROUP BY a.name, w.channel, w.occurred_at
ORDER BY w.occurred_at DESC;

-- Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used.
SELECT w.channel, COUNT(w.channel) AS ch_count
FROM web_events w
GROUP BY w.channel
ORDER BY ch_count;

-- Who was the primary contact associated with the earliest web_event? 
SELECT a.primary_poc 
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
ORDER BY w.occurred_at
LIMIT 1

SELECT a.primary_poc, MIN(w.occurred_at)
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
GROUP BY a.id, a.primary_poc, w.occurred_at
ORDER BY w.occurred_at
LIMIT 1;

-- What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest.
SELECT a.name, MIN(o.total_amt_usd)
FROM orders o
JOIN accounts a
ON a.id = o.account_id
GROUP BY a.name, o.total_amt_usd
ORDER BY o.total_amt_usd;

-- Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from fewest reps to most reps.
SELECT r.name, COUNT(s.id) AS rep_count
FROM region r
JOIN sales_reps s
ON s.region_id = r.id
GROUP BY r.name
ORDER BY rep_count;