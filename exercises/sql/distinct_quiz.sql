-- Use DISTINCT to test if there are any accounts associated with more than one region.
SELECT DISTINCT a.name account, COUNT(r.name) regions
FROM accounts a
    JOIN sales_reps s
    ON s.id = a.sales_rep_id
    JOIN region r
    ON r.id = s.region_id
GROUP BY a.name
ORDER BY regions DESC


-- Have any sales reps worked on more than one account?
SELECT s.name, COUNT(a.name) accounts
FROM accounts a
    JOIN sales_reps s
    ON s.id = a.sales_rep_id
GROUP BY s.name
ORDER BY accounts DESC
