select CAR_TYPE, count(CAR_ID) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like "%통풍시트%" or OPTIONS like "%가죽시트%" or OPTIONS like "%열선시트%"
group by 1
order by 1;