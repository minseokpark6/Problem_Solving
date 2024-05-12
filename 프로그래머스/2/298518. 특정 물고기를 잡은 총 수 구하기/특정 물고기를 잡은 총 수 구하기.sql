select count(ID) as FISH_COUNT
from FISH_INFO 
where FISH_TYPE in 
    (select FISH_TYPE from FISH_NAME_INFO where FISH_NAME in ('BASS', 'SNAPPER'));


/*
select (count((select FISH_TYPE from FISH_INFO where b.FISH_NAME = 'BASS')) + count((select FISH_TYPE from FISH_INFO where b.FISH_NAME = 'SNAPPER'))) as FISH_COUNT
from FISH_INFO as a
left join FISH_NAME_INFO as b
on a.FISH_TYPE = b.FISH_TYPE;
*/