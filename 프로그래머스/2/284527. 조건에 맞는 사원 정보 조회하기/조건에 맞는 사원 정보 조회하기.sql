select SCORE, a.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES as a
left join (select emp_no, sum(score) as SCORE from hr_grade where year like "2022%" group by emp_no) as b
on a.EMP_NO = b.EMP_NO
order by 1 desc
limit 1;




/*
select 
    (select sum(score) from hr_grade where year like "2022%" group by emp_no) as SCORE, 
    a.EMP_NO, EMP_NAME, POSITION, EMAIL
from HR_EMPLOYEES as a
left join HR_GRADE as b
on a.EMP_NO = b.EMP_NO
order by 1 desc
limit 1;
*/