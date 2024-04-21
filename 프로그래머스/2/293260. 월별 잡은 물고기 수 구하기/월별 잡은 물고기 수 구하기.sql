select
    count(FISH_TYPE) as FISH_COUNT,
    month(time) as MONTH
from fish_info
group by MONTH
having FISH_COUNT != 0
order by MONTH;