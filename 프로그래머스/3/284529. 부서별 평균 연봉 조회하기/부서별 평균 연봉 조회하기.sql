select a.DEPT_ID, 
        DEPT_NAME_EN,
        round(avg(SAL), 0) as AVG_SAL
from HR_EMPLOYEES as a
left join HR_DEPARTMENT as b
on a.DEPT_ID = b.DEPT_ID
group by a.DEPT_ID
order by 3 desc;

