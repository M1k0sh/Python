import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "E#)fzAka",
    host = "localhost",
    port = "5432"
)

s = input()

conn.autocommit = True

cursor = conn.cursor()

paste = "DELETE FROM phonebook WHERE user_name=%s"

cursor.execute(paste, (s,))

conn.commit()
cursor.close()
conn.close()