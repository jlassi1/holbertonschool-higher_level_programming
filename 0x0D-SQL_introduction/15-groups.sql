-- lists the nSELECT score, count(score) as number 
SELECT score, count(score) as number 
FROM second_table
group by score
ORDER BY number DESC;
