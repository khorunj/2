--Отримати всі завдання певного користувача.
select *
from tasks
where user_id = 1;

--Вибрати завдання за певним статусом
select * from tasks 
where status_id = (select id from status where name = 'new');

--Оновити статус конкретного завдання
update tasks 
set status_id = 2
where status_id = 1 and user_id = 7;

--Отримати список користувачів, які не мають жодного завдання
select * from users
where id not in (select user_id from tasks);

--Додати нове завдання для конкретного користувача
insert into tasks(title, description, status_id, user_id)
values('Do your homework', 'There is two tasks', 1, 2);

--Отримати всі завдання, які ще не завершено
select * from tasks 
where status_id != 3;

--Видалити конкретне завдання
delete from tasks 
where id = 5;

--Знайти користувачів з певною електронною поштою
SELECT * FROM users
where email like '%dennis%';

--Оновити ім'я користувача
update users 
set fullname = 'Vasiliy'
where fullname = 'Paul Oneal';

--Отримати кількість завдань для кожного статусу
select status_id 
	,Count(status_id)
from tasks
group by 1
order by 1;

--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
select title, description, status_id, fullname, email 
from tasks t 
join users u  on u.id = t.user_id 
where email like '%example.net%';

--Отримати список завдань, що не мають опису
select * from tasks t 
where description = '';

--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
select fullname, title, description, name
from tasks t 
join users u on u.id = t.user_id 
join status s on s.id = t.status_id 
where status_id = 2;

--Отримати користувачів та кількість їхніх завдань
--Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
select fullname
	, count(title) as quantity_t
from tasks t 
join users u on u.id = t.user_id 
group by 1
order by 2 desc;


