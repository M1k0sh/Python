import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "E#)fzAka"
)

# cursor = conn.cursor()

# copyy = """
#     COPY phonebook(user_name, tel_number, tel_connection)
#     FROM \'C:\Users\PK\python1\Python\Lab10\contacts.csv\'
#     DELIMITER \',\'
#     CSV HEADER;
# """

# cursor.execute(copyy)
# conn.commit()
# cursor.close()
# conn.close()

# second part
name = input()
tel_number = input()
tel_connection = input()

cur = conn.cursor()

paste = 'INSERT INTO phonebook(user_name, tel_number, tel_connection) VALUES(%s, %s, %s)'

cur.execute(paste, (name, tel_number, tel_connection))

conn.commit()
cur.close()
conn.close()
