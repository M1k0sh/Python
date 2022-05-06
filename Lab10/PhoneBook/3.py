import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "E#)fzAka"
)

name = input()
tel_number = input()
tel_connection = input()

cur = conn.cursor()

paste = 'UPDATE phonebook SET tel_number=%s, tel_connection=%s WHERE user_name=%s;'

cur.execute(paste, (name, tel_number, tel_connection))

conn.commit()
cur.close()
conn.close()
