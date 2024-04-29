select 
    USER_ID, NICKNAME, 
    concat(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as '전체주소',
    concat(substring(TLNO, 1, 3), '-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4)) as '전화번호'
from USED_GOODS_USER 
where USER_ID in 
        (select WRITER_ID from USED_GOODS_BOARD group by WRITER_ID having count(BOARD_ID) >= 3)
order by 1 desc;


/*
select 
    a.WRITER_ID, b.NICKNAME, 
    concat(CITY, '', STREET_ADDRESS1, '', STREET_ADDRESS2) as '전체주소',
    concat(substring(TLNO, 1, 3), '-', substring(TLNO, 4, 4), '-', substring(TLNO, 8, 4))as '전화번호'
from USED_GOODS_BOARD as a
left join USED_GOODS_USER as b
on a.WRITER_ID = b.USER_ID
group by a.WRITER_ID
having count(BOARD_ID) >= 3
order by 1 desc;
*/