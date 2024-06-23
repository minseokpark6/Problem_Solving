select FLAVOR
from (select FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER
     from (select *
      from FIRST_HALF
      union
      select * 
      from JULY) as a
     group by FLAVOR) as b
order by TOTAL_ORDER desc
limit 3;