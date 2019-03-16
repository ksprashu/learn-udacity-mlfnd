-- For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account. 
SELECT a.name, AVG(o.standard_qty) avg_std_qty, AVG(o.gloss_qty) avg_gls_qty, AVG(o.poster_qty) avg_pst_qty
FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY a.name

-- For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type.
SELECT a.name, AVG(o.standard_amt_usd) avg_std_usd, AVG(o.gloss_amt_usd) avg_gls_usd, AVG(o.poster_amt_usd) avg_pst_usd
FROM orders o
    JOIN accounts a
    ON a.id = o.account_id
GROUP BY a.id, a.name
ORDER BY a.name

-- Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
SELECT s.name, w.channel, COUNT(*) occurrences
FROM sales_reps s
    JOIN accounts a
    ON a.sales_rep_id = s.id
    JOIN web_events w
    ON w.account_id = a.id
GROUP BY s.name, w.channel
ORDER BY s.name, occurrences DESC;

-- Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first.
SELECT r.name, w.channel, COUNT(*) occurrences
FROM region r
    JOIN sales_reps s
    ON s.region_id = r.id
    JOIN accounts a
    ON a.sales_rep_id = s.id
    JOIN web_events w
    ON w.account_id = a.id
GROUP BY r.name, w.channel
ORDER BY r.name, occurrences DESC;