import psycopg2
from config import load_config


def delete_number():

    sql = r""" DELETE FROM phonebook where length(regexp_replace(phone, '\D', '', 'g')) < 5"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                cur.execute(sql)

            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    delete_number()