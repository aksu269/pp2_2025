import psycopg2
from config import load_config

first_name = input()
last_name = input()
phone = input()


def insert_phone_number(first_name, last_name, phone):
    """ Insert multiple vendors into the vendors table  """

    sql = "INSERT INTO phonebook(first_name, last_name, phone) VALUES(%s, %s, %s) RETURNING *"
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (first_name, last_name, phone))
                phone_id = cur.fetchone()[0]
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)



if __name__ == '__main__':
    insert_phone_number(first_name, last_name, phone)
    