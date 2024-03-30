select * from lists l join items i on i.list_id = l.id
group by l.id, i.item_id
order by l.id




