select PRODUCT_CODE, sum(a.PRICE * b.SALES_AMOUNT) as SALES
from PRODUCT as a
JOIN OFFLINE_SALE as b
on a.PRODUCT_ID = b.PRODUCT_ID
group by 1
order by 2 desc, a.PRODUCT_CODE;