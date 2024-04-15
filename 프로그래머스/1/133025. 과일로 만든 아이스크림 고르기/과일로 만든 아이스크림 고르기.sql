select a.FLAVOR
from FIRST_HALF as a
where TOTAL_ORDER > 3000 and a.FLAVOR in (select FLAVOR from ICECREAM_INFO where INGREDIENT_TYPE = 'fruit_based')
order by TOTAL_ORDER desc;

