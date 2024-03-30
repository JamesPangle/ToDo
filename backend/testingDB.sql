insert into lists(name) values ('listing1');
insert into lists(name) values ('listing2');
insert into lists(name) values ('listing3');
insert into lists(name) values ('listing4');
insert into lists(name) values ('listing5');
insert into items(list_id, descr, completed) values (1, 'laundry', false);
insert into items(list_id, descr, completed) values (2, 'dry', true);
insert into items(list_id, descr, due, completed) values (1, 'clean', '1/20/2024', false);
insert into items(list_id, descr, due, completed) values (2, 'cook', '1/21/2024',  true);
insert into items(list_id, descr, completed) values (1, 'fry', false);
insert into items(list_id, descr, completed) values (2, 'lake', true);
insert into items(list_id, descr, due, completed) values (3, 'eat', '1/22/2024',  false);
insert into items(list_id, descr, due, completed) values (4, 'sleep', '1/23/2024',  true);
insert into items(list_id, descr, completed) values (5, 'dishes', false);
insert into items(list_id, descr, due, completed) values (4, 'drive', '1/24/2024',  true);
insert into items(list_id, descr, completed) values (3, 'fly', false);



