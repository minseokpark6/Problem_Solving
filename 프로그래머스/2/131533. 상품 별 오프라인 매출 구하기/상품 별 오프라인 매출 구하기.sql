select PRODUCT_CODE, sum(o.SALES_AMOUNT * p.PRICE) as SALES
from PRODUCT as p
join OFFLINE_SALE as o
on p.PRODUCT_ID = o.PRODUCT_ID
group by PRODUCT_CODE
order by SALES desc, PRODUCT_CODE; 
