select i.REST_ID, i.REST_NAME, i.FOOD_TYPE, i.FAVORITES, i.ADDRESS, round(avg(r.REVIEW_SCORE), 2) as SCORE
from REST_INFO as i
left join REST_REVIEW as r
on i.REST_ID = r.REST_ID
where i.ADDRESS like '서울%' and r.REVIEW_SCORE is not null
group by REST_ID
order by SCORE desc, FAVORITES desc;

