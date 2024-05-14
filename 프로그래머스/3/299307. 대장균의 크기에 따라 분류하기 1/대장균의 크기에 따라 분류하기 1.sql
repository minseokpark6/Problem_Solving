select ID, SIZE
from (select ID,
     case
     when size_of_colony <= 100 then 'LOW'
     when size_of_colony > 100 and size_of_colony <= 1000 then 'MEDIUM'
     else 'HIGH'
     end as SIZE
     from ECOLI_DATA) as a
order by 1;