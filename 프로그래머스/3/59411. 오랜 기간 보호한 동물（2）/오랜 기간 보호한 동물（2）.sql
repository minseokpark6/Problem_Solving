select a.animal_id, a.name
from animal_ins as a
right join animal_outs as b
on a.animal_id = b.animal_id
where a.animal_id is not null
order by datediff(b.datetime, a.datetime) desc
limit 2;