select ANIMAL_ID, NAME, date_format(DATETIME, "%Y-%m-%d") as DATE
from ANIMAL_INS
order by 1;