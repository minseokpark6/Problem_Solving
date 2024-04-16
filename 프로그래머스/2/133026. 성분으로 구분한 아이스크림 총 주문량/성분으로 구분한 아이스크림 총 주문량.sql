select INGREDIENT_TYPE, sum(TOTAL_ORDER) as TOTAL_ORDER
from FIRST_HALF
left join ICECREAM_INFO using (FLAVOR)
group by 1
order by 2;

