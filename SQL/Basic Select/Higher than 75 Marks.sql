--https://www.hackerrank.com/challenges/more-than-75-marks/problem

select name from students WHERE marks > 75 order by substr(name,-3), ID ASC;