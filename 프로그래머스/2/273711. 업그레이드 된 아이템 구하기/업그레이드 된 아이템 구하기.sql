select a.item_id, item_name, rarity
from ITEM_INFO as a
left join ITEM_TREE as b
on a.item_id = b.item_id
where b.PARENT_ITEM_ID in (select item_id from item_info where rarity = "RARE")
order by 1 desc;




/*
select a.item_id, item_name, rarity
from ITEM_INFO as a
left join ITEM_TREE as b
on a.item_id = b.item_id
where rarity = "RARE" and parent_item_id is not null
order by 1 desc;
*/