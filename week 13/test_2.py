import psycopg2
from config import load_config


def replace_number(min_dig, new_phone):

    updated_row_count = 0
    sql_1 = '''select phone_id, phone from phonebook'''
    sql_2 = """ UPDATE phonebook SET phone = %s WHERE phone_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql_1)
                rows = cur.fetchall()
                for row in rows:
                    phone_id = row[0]
                    phone = row[1]
                    digits = ''.join(c for c in phone if c.isdigit())
                    if len(digits) < min_dig:
                        cur.execute(sql_2, (new_phone, phone_id))
                    
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    replace_number(5, '8887666')