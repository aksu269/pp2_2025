import psycopg2
from config import load_config


def delete_number(first_name):

    sql = """ DELETE FROM phonebook where first_name = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                cur.execute(sql, (first_name,))

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    delete_number("Axu")