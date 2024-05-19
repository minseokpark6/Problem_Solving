select Milk.CART_ID
from (select CART_ID, NAME from CART_PRODUCTS where NAME = 'Milk') as Milk
inner join (select CART_ID, NAME from CART_PRODUCTS where NAME = 'Yogurt') as Yogurt
on Milk.CART_ID = Yogurt.CART_ID
group by 1
order by 1;