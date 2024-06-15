select year(o.sales_date) as YEAR, month(o.sales_date) as MONTH, i.gender, count(distinct o.user_id) as USERS
from ONLINE_SALE as o
join USER_INFO as i
on o.user_id = i.user_id
where gender is not null
group by YEAR, MONTH, i.gender
order by 1, 2, 3;
