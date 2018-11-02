-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem

select c.continent,floor(avg(ci.population))
from city ci, country c
where ci.countrycode = c.code
group by c.continent;