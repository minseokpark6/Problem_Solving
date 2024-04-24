/*
SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM REST_INFO A
WHERE (FOOD_TYPE,FAVORITES) 
IN 
(
    SELECT FOOD_TYPE, MAX(FAVORITES) 
    FROM REST_INFO B
    WHERE A.FOOD_TYPE = B.FOOD_TYPE
)
ORDER BY FOOD_TYPE DESC; 
*/


select food_type, rest_id, rest_name, favorites
from rest_info
where (food_type, favorites) in (select food_type, max(favorites) from rest_info group by food_type)
order by food_type desc;


/*
select food_type, rest_id, rest_name, favorites
from rest_info
group by food_type
having (food_type, favorites) in (select food_type, max(favorites) from rest_info)
order by 1 desc;
*/

/*
select food_type, rest_id, rest_name, favorites
from rest_info
group by food_type
having favorites = max(favorites)
order by 1 desc;
*/
