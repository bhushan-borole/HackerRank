https://www.hackerrank.com/challenges/weather-observation-station-11/problem

select DISTINCT city from (SELECT T1.city FROM station T1 WHERE lower(SUBSTR(T1.city, -1)) not IN ('a', 'e', 'i', 'o', 'u') union all SELECT T1.city FROM station T1 WHERE lower(SUBSTR(T1.city, 0, 1)) not IN ('a', 'e', 'i', 'o', 'u'));