select hour(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
group by 1
having HOUR between 9 and 19
order by 1;