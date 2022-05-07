from config import config
import psycopg2

def pattern():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phonebook")
        for contacts in cursor.fetchall():
            print(f'user_name: {contacts[0]}; tel_number: {contacts[1]}; tel_connection: {contacts[2]}')

    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


pattern()