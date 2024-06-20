select AUTHOR_ID, AUTHOR_NAME, CATEGORY, sum(total_sales) as TOTAL_SALES
from (select b.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, s.SALES_DATE, (b.PRICE * s.SALES) as TOTAL_SALES
      from BOOK as b
      left join AUTHOR as a
      on b.AUTHOR_ID = a.AUTHOR_ID 
      join BOOK_SALES as s 
      on b.BOOK_ID = s.BOOK_ID) as f
where month(SALES_DATE) = 01
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID, CATEGORY desc;