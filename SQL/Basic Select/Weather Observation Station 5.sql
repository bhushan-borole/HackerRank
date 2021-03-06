--https://www.hackerrank.com/challenges/weather-observation-station-5/problem

select
    CITY,
    char_length(CITY)
from STATION
where CITY = (
    select
        min(CITY)
    from STATION
    where char_length(CITY) = (
        select
            min(char_length(CITY))
        from STATION
    )
)
OR CITY = (
    select
        min(CITY)
    from STATION
    where char_length(CITY) = (
        select
            max(char_length(CITY))
        from STATION
    )
);