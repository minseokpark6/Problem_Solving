select ID, 
    case when RANK_SIZE <= ((SELECT count(*) FROM ECOLI_DATA) * 0.25) then 'CRITICAL'
         when RANK_SIZE <= ((SELECT count(*) FROM ECOLI_DATA) * 0.50) then 'HIGH'
         when RANK_SIZE <= ((SELECT count(*) FROM ECOLI_DATA) * 0.75) then 'MEDIUM'
         else 'LOW'
    end as COLONY_NAME
from
(
    select ID, RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) as RANK_SIZE
    from ECOLI_DATA
) as a
order by 1;