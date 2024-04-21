select USER_ID, PRODUCT_ID
from online_sale
group by user_id, product_id
having count(product_id) > 1
order by 1, 2 desc;

