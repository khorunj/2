--1.Отримати всі завдання певного користувача.
select *
from tasks
where user_id = 1;

--2.Вибрати завдання за певним статусом
select * from tasks 
where status_id = (select id from status where name = 'new');

--3.Оновити статус конкретного завдання
update tasks 
set status_id = (select id from status where name = 'in progress')
where id = 6;

--4.Отримати список користувачів, які не мають жодного завдання
select * from users
where id not in (select user_id from tasks);

--5.Додати нове завдання для конкретного користувача
insert into tasks(title, description, status_id, user_id)
values('Do your homework', 'There is two tasks', 1, 2);

--6.Отримати всі завдання, які ще не завершено
select * from tasks 
where status_id != (select id from status where name = 'completed');

--7.Видалити конкретне завдання
delete from tasks 
where id = 5;

--8.Знайти користувачів з певною електронною поштою
SELECT * FROM users
where email like '%dennis%';

--9.Оновити ім'я користувача
update users 
set fullname = 'Vasiliy'
where fullname = 'Paul Oneal';

--10.Отримати кількість завдань для кожного статусу
select status_id 
	,Count(status_id)
from tasks
group by 1
order by 1;

--11.Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
select title, description, status_id, fullname, email 
from tasks t 
join users u  on u.id = t.user_id 
where email like '%example.net%';

--12.Отримати список завдань, що не мають опису
select * from tasks t 
where description = '' or description isnull;

--13.Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
select fullname, title, description, name
from tasks t 
join users u on u.id = t.user_id 
join status s on s.id = t.status_id 
where status_id = 2;

--14.Отримати користувачів та кількість їхніх завдань

select fullname
	, count(title) as quantity_t
from tasks t 
join users u on u.id = t.user_id 
group by u.id
order by 2 desc;



