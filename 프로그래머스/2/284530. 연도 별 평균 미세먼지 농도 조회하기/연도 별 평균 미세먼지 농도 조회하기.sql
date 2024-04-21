select year(YM) as 'YEAR', round(avg(pm_val1), 2) as 'PM10', round(avg(pm_val2), 2) as 'PM2.5'
from air_pollution
where LOCATION2 = '수원'
group by 1
order by 1;