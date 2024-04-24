select a.category, sum(sales) as TOTAL_SALES
from BOOK as a
left join BOOK_SALES as b
on a.BOOK_ID = b.BOOK_ID
where b.sales_date like "2022-01%"
group by 1
order by 1 ;