--https://www.hackerrank.com/challenges/weather-observation-station-3/problem

select distinct city from STATION
where  id % 2 = 0;