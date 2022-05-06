import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "E#)fzAka",
    host = "localhost",
    port = "5432"
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute("CREATE TABLE PhoneBook(user_name VARCHAR(50), tel_number VARCHAR(20), tel_connection VARCHAR(50))")

print("Table created")