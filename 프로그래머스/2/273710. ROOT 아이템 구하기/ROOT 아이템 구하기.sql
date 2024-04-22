select a.item_id, item_name
from item_info as a
left join item_tree as b
on a.item_id = b.item_id 
where b.parent_item_id is null
order by 1;

