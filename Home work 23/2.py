"""1. Напишите программу, которая считывает информацию из
таблицы book и печатает ее в виде таблицы, соответствующей
таблице из базы данных.
2. Более сложный вариант составить DataFrame на основании
считанной информации, соответствующий таблице из базы
данных."""

import psycopg2

con = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='    ',
    host='127.0.0.1',
    port='5432'
)
cur = con.cursor()

cur.execute("""
select * 
from book
""")

j = 1
for i in cur:
    print(f"{j:3} {'' if i[0] is None else i[0]:10} {i[1]:25} {i[2]:25} {i[3]:25} {i[4]:25} {i[5]:25}")
    j += 1
con.close()
