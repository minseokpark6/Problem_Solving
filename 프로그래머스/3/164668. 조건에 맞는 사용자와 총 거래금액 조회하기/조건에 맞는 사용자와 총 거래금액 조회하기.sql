select b.USER_ID, b.NICKNAME, sum(PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as a
left join USED_GOODS_USER as b
on a.WRITER_ID = b.USER_ID
where STATUS = 'DONE'
group by b.USER_ID
having TOTAL_SALES >= 700000
order by 3;