select b.ingredient_type, sum(TOTAL_ORDER) as TOTAL_ORDER
from first_half as a
left join icecream_info as b
on a.flavor = b.flavor
group by 1
order by 2;