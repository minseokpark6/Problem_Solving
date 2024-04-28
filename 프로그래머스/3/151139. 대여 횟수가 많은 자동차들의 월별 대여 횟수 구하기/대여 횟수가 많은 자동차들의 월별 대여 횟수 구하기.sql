select 
    month(start_date) as MONTH,
    CAR_ID,
    count(car_id) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where (START_DATE between "2022-08-01" and "2022-10-31") and 
CAR_ID in
(select CAR_ID
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where (START_DATE between "2022-08-01" and "2022-10-31")
group by CAR_ID
having (count(HISTORY_ID) >= 5))
group by 1, 2
having RECORDS != 0
order by 1, 2 desc;