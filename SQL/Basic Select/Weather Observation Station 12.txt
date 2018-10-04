https://www.hackerrank.com/challenges/weather-observation-station-12/problem

SELECT DISTINCT City
FROM Station
WHERE REGEXP_LIKE(City, '^[^AEIOU].*[^aeiou]$');