select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME 
from FOOD_PRODUCT as a
where PRICE = (select max(price) from FOOD_PRODUCT as b where a.CATEGORY = b.CATEGORY) and CATEGORY in ('과자', '국', '김치', '식용유')
order by MAX_PRICE desc;



/*
select CATEGORY, PRICE as MAX_PRICE, PRODUCT_NAME 
from (select CATEGORY, max(PRICE) as PRICE, PRODUCT_NAME 
      from FOOD_PRODUCT
      group by CATEGORY) as a
where CATEGORY in ('과자', '국', '김치', '식용유')
order by 2 desc;
*/