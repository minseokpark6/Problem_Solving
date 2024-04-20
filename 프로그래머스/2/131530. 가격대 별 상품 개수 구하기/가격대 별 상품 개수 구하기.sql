select if (price < 0, 0, price * 10000) as PRICE_GROUP, count(*) as PRODUCTS
from (select floor(price/10000) as price from product) as a
group by 1
order by 1;











# select left(price, 1) * 10000 as PRICE_GROUP, count(*)as PRODUCTS
# from product
# group by PRICE_GROUP
# order by 1;