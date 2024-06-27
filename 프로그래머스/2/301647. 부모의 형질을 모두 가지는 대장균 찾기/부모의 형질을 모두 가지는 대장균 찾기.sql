select origin.ID, origin.GENOTYPE, parent.GENOTYPE as PARENT_GENOTYPE
from ECOLI_DATA as origin 
left join ECOLI_DATA as parent 
on origin.PARENT_ID = parent.ID
where parent.GENOTYPE & origin.GENOTYPE = parent.GENOTYPE
order by 1;