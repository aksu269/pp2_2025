import psycopg2
from config import load_config


def update_number(phone_id, first_name):
    """ Update vendor name based on the vendor id """

    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET first_name = %s
                WHERE phone_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (first_name, phone_id))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_number(2, "Aksu")