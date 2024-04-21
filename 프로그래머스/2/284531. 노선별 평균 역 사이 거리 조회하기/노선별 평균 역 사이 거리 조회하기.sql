select 
    ROUTE,
    concat(round(sum(d_between_dist), 1), 'km') as TOTAL_DISTANCE,
    concat(round(avg(d_between_dist), 2), 'km') as AVERAGE_DISTANCE
from subway_distance
group by 1
order by round(sum(d_between_dist), 1) desc;

/*
select 
    ROUTE,
    concat(round(sum(d_between_dist), 1), 'km') as TOTAL_DISTANCE,
    concat(round(avg(d_between_dist), 2), 'km') as AVERAGE_DISTANCE
from subway_distance
group by 1
order by 2 desc;
*/