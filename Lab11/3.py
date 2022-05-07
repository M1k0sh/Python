import psycopg2
from config import config

def insert_list(l):
    insert = """
    INSERT INTO phonebook(user_name, tel_number, tel_connection) VALUES(%s, %s, %s);
    """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany(insert, (l))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

l = [
    ("Adil", "8-707-873-57-48", "Tele2"),
    ("Nurik", "8-775-281-08-22", "Activ"),
    ("Rahat", "8-701-654-85-52", "Activ"),
]

insert_list(l)