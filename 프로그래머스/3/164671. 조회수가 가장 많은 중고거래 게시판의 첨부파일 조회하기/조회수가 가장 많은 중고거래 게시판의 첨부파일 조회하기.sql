select concat('/home/grep/src/', a.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE as a
join USED_GOODS_BOARD as b
on a.BOARD_ID = b.BOARD_ID
where VIEWS =
    (select max(VIEWS)
     from USED_GOODS_BOARD)
order by FILE_ID desc;





/*
select concat('/home/grep/src/', BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE
where BOARD_ID in 
    (select BOARD_ID 
     from USED_GOODS_BOARD 
     order by VIEWS desc 
     limit 1)
order by FILE_ID desc;
*/