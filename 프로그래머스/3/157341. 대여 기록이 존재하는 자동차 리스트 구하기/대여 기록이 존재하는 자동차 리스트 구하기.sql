select distinct a.CAR_ID
from CAR_RENTAL_COMPANY_CAR a
left join CAR_RENTAL_COMPANY_RENTAL_HISTORY b
on a.CAR_ID = B.CAR_ID
where CAR_TYPE = '세단' and month(START_DATE) = 10
order by 1 desc;