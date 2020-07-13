-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, avg(value) as avg_temp 
FROM temperatures
GROUP BY city
ORDER BY avg(value) DESC
LIMIT 3;
