select BOOK_ID, AUTHOR_NAME, date_format(PUBLISHED_DATE, "%Y-%m-%d") as PUBLISHED_DATE
from BOOK 
join AUTHOR using (AUTHOR_ID)
where CATEGORY = "경제"
order by 3;