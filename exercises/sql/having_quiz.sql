-- How many of the sales reps have more than 5 accounts that they manage?
SELECT s.name, COUNT(a.id) accounts
FROM sales_reps s
    JOIN accounts a
    ON a.sales_rep_id = s.id
GROUP BY s.name
HAVING COUNT(a.id) > 5
ORDER BY accounts;

-- How many accounts have more than 20 orders?
SELECT a.name, COUNT(o.id) orders
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
HAVING COUNT(o.id) > 20
ORDER BY orders;

-- Which account has the most orders?
SELECT a.name, COUNT(o.id) orders
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
ORDER BY orders DESC
LIMIT 1;

-- Which accounts spent more than 30,000 usd total across all orders?
SELECT a.name, SUM(o.total_amt_usd) total
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
HAVING SUM(o.total_amt_usd) > 30000
ORDER BY total;

-- Which accounts spent less than 1,000 usd total across all orders?
SELECT a.name, SUM(o.total_amt_usd) total
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
HAVING SUM(o.total_amt_usd) < 1000
ORDER BY total;


-- Which account has spent the most with us?
SELECT a.name, SUM(o.total_amt_usd) total
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
ORDER BY total DESC
LIMIT 1;

-- Which account has spent the least with us?
SELECT a.name, SUM(o.total_amt_usd) total
FROM accounts a
    JOIN orders o
    ON o.account_id = a.id
GROUP BY a.name
ORDER BY total
LIMIT 1;

-- Which accounts used facebook as a channel to contact customers more than 6 times?
SELECT a.name, w.channel, COUNT(w.occurred_at) contacts
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
WHERE w.channel = 'facebook'
GROUP BY a.name, w.channel
HAVING COUNT(w.occurred_at) > 6
ORDER BY contacts;

-- Which account used facebook most as a channel? 
SELECT a.name, w.channel, COUNT(w.occurred_at) contacts
FROM accounts a
JOIN web_events w
ON w.account_id = a.id
WHERE w.channel = 'facebook'
GROUP BY a.name, w.channel
ORDER BY contacts DESC
LIMIT 1;

-- Which channel was most frequently used by most accounts?
SELECT w.channel, COUNT(w.channel) usage
FROM web_events w
JOIN accounts a
ON a.id = w.account_id
GROUP BY w.channel
ORDER BY usage DESC