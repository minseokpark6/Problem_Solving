select count(*) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE 
from (select ID, FISH_TYPE, ifnull(LENGTH, 10) as LENGTH
      from FISH_INFO) as a
Group by FISH_TYPE
having avg(LENGTH) > 32
order by FISH_TYPE;
