# psql
# \l - list all databases
# \c - database_name - connect to database 
# \dt - list off all tables 
# \q - quit

from unittest import result
import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='E#)fzAka',
    host='localhost',
    port='5432'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM PhoneBook")

#results = cursor.fetchall()
results = cursor.fetchone()
print(results)