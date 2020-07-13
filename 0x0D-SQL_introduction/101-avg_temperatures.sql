--  lists all rows of thefirst_table table first_table from the database hbtn_0c_0 in your MySQL server.
SELECT city, avg(value) as avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg(value) DESC;
