-- lists all records of the table second_table with name
-- Records are ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY `score` DESC;
