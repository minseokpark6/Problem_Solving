select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS as a
join ANIMAL_OUTS as b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_INTAKE like "Intact%" and b.SEX_UPON_OUTCOME not like "Intact%" 
order by 1;
