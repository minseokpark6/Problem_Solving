select ITEM_ID, ITEM_NAME, RARITY
from ITEM_INFO
where ITEM_ID not in (select distinct parent_item_id from ITEM_TREE where parent_item_id is not null)
order by 1 desc;
