select MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' and month(DATE_Of_BIRTH) = 3 and TLNO is not NULL
order by 1;