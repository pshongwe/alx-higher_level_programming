-- update based on name not id
UPDATE second_table
SET score = 10
WHERE name = 'Bob'
ORDER BY score
DESC;
