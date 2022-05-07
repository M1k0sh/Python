import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="E#)fzAka"
)

sql = """
create or replace function output(lim integer, simcard varchar)
    returns table(
        user_name varchar,
        tel_number varchar,
        tel_connection varchar
                )
AS
$$
begin
    return query
        select phonebook.user_name, phonebook.tel_number, phonebook.tel_connection from phonebook as phonebook
        where phonebook.tel_connection = $2
        ORDER BY phonebook.user_name
        limit $1;
end
$$ language plpgsql;

select * from output(%s, %s)
"""

simcard = input('Which telephone connection?\n')
limit = input('How many people?\n')

cur = conn.cursor()

cur.execute(sql, (limit,simcard))

contacts = cur.fetchall()

for contact in contacts:
    print(contact)

conn.commit()
cur.close()
conn.close()