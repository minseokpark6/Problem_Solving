select HOUR, count(ANIMAL_ID) as COUNT
from (select (ROW_NUMBER() OVER () - 1) as HOUR
      FROM ANIMAL_OUTS
      LIMIT 24) as 24HOURS_TABLE
      left join ANIMAL_OUTS as b
      on 24HOURS_TABLE.HOUR = HOUR(b.DATETIME)
group by 1
order by 1;


/*
select HOUR, count(ANIMAL_ID) as COUNT
from (select ANIMAL_ID, HOUR(DATETIME) as HOUR
     from ANIMAL_OUTS) as a
group by HOUR
order by HOUR;
*/