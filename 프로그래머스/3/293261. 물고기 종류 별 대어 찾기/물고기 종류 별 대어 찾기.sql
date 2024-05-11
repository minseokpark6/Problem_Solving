select ID, FISH_NAME, LENGTH
from FISH_INFO as a
left join FISH_NAME_INFO as b
on a.FISH_TYPE = b.FISH_TYPE
where (a.fish_type, length) in 
(select fish_type, max(length) as length 
from FISH_INFO 
group by fish_type)
order by 1;

/*
select ID, FISH_NAME, LENGTH
from FISH_INFO as a
left join FISH_NAME_INFO as b
on a.FISH_TYPE = b.FISH_TYPE
where length is not null 
group by a.FISH_TYPE
having LENGTH in (select max(length) from FISH_INFO)
order by 1;
*/