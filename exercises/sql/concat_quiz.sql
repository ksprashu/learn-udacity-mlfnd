-- Each company in the accounts table wants to create an email address for each primary_poc. The email address should be the first name of the primary_poc . last name primary_poc @ company name .com.
 SELECT name, CONCAT(LOWER(LEFT(primary_poc, POSITION(' ' IN primary_poc)-1)), '.', LOWER(RIGHT(primary_poc, LENGTH(primary_poc)-POSITION(' ' IN primary_poc))), '@', LOWER(name), '.com') email
 FROM accounts;

-- You may have noticed that in the previous solution some of the company names include spaces, which will certainly not work in an email address. See if you can create an email address that will work by removing all of the spaces in the account name, but otherwise your solution should be just as in question 1. Some helpful documentation is here.
 SELECT name, CONCAT(LOWER(LEFT(primary_poc, POSITION(' ' IN primary_poc)-1)), '.', LOWER(RIGHT(primary_poc, LENGTH(primary_poc)-POSITION(' ' IN primary_poc))), '@', REPLACE(name, ' ', ''), '.com') email
 FROM accounts;

-- We would also like to create an initial password, which they will change after their first log in. The first password will be the first letter of the primary_poc's first name (lowercase), then the last letter of their first name (lowercase), the first letter of their last name (lowercase), the last letter of their last name (lowercase), the number of letters in their first name, the number of letters in their last name, and then the name of the company they are working with, all capitalized with no spaces.
 WITH t1 AS
 (SELECT LEFT(LOWER(primary_poc), POSITION(' ' IN primary_poc)-1) first_name, 
 RIGHT(LOWER(primary_poc), LENGTH(primary_poc)-POSITION(' ' IN primary_poc)) last_name,
 name, primary_poc
 FROM accounts)

 SELECT name, primary_poc, CONCAT(LEFT(first_name, 1), RIGHT(first_name, 1), LEFT(last_name, 1), RIGHT(last_name, 1), LENGTH(first_name), LENGTH(last_name), REPLACE(UPPER(name), ' ', '')) pass
 FROM t1;

    