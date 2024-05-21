select p.PRODUCT_ID, p.PRODUCT_NAME, 
        (p.PRICE * sum(o.AMOUNT)) as TOTAL_SALES
from FOOD_PRODUCT as p
join FOOD_ORDER as o
on p.PRODUCT_ID = o.PRODUCT_ID 
where date_format(PRODUCE_DATE, '%Y-%m') = '2022-05'
group by 1
order by 3 desc, 1;