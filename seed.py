from faker import Faker
import psycopg2
import random

fake = Faker()

create_table_users = """
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);
"""
create_table_status = """
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);
"""
create_table_tasks = """
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
"""

# Підключення до бази даних
conn = psycopg2.connect(
    dbname='',
    user='postgres',
    password='password',
    host='localhost'
)

cur = conn.cursor()
# Створення таблиць
cur.execute(create_table_users)
cur.execute(create_table_status)
cur.execute(create_table_tasks)
# Вставка даних у таблицю 'status'
statuses = ['new', 'in progress', 'completed']
for status in statuses:
    cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING;", (status,))

# Вставка даних у таблицю 'users'
for _ in range(10):  # Генерувати 10 користувачів
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s);", (fake.name(), fake.email()))

# Вставка даних у таблицю 'tasks'
for _ in range(20):  # Генерувати 20 завдань
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s);",
                (fake.sentence(), fake.text(), random.randint(1, len(statuses)), random.randint(1, 10)))

conn.commit()

cur.close()
conn.close()
