select count(*) as FISH_COUNT, max(LENGTH) as MAX_LENGTH, FISH_TYPE 
from (select ID, FISH_TYPE, ifnull(LENGTH, 10) as LENGTH
      from FISH_INFO) as a
Group by FISH_TYPE
having avg(LENGTH) >= 33
order by FISH_TYPE;

/*
SELECT COUNT(ID) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG(IFNULL(LENGTH,10)) >= 33
ORDER BY FISH_TYPE ASC;
*/