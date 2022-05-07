import psycopg2
from config import config

name = input("Enter user name: ")
tel = input("Enter new tel number: ")
connection = input("Enter new tel connection: ")

def insert_update(name, tel, connection):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phonebook")

        contacts = cursor.fetchall()

        for contact in contacts:
            if contact[0] == name:
                update = """
                UPDATE phonebook SET
                tel_number = %s 
                where user_name = %s
                """
                cursor.execute(update, (tel, name))
                conn.commit()
                cursor.close()
                exit()
                
        insert = """
        INSERT INTO 
        phonebook(user_name, tel_number, tel_connection)
        VALUES(%s, %s, %s)
        """
        cursor.execute(insert, (name, tel, connection))
        conn.commit()
        cursor.close()
        
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_update(name, tel, connection)