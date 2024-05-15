select case 
        when MONTH(DIFFERENTIATION_DATE) < 4 then '1Q'
        when MONTH(DIFFERENTIATION_DATE) < 7 then '2Q'
        when MONTH(DIFFERENTIATION_DATE) < 10 then '3Q'
        else '4Q'
        end as QUARTER, 
        count(ID) as ECOLI_COUNT
from ECOLI_DATA
group by QUARTER
order by QUARTER;