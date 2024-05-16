select b.year as YEAR,
         (b.maxone - a.SIZE_OF_COLONY) as YEAR_DEV,
        ID
from ECOLI_DATA as a
left join (select YEAR(DIFFERENTIATION_DATE) as YEAR, max(SIZE_OF_COLONY) as maxone from ECOLI_DATA group by 1) as b
on YEAR(a.DIFFERENTIATION_DATE) = b.year
order by 1, 2;