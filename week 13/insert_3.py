import psycopg2
from config import load_config
import csv
d = {
    'Marina': '+77072076323',
    'Tamilana': '+77472046424'
}
def insert_many_numbers(d):
    sql = "INSERT INTO phonebook(first_name, last_name, phone) VALUES(%s, %s, %s) "
    config = load_config()
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                for i in d:
                    phone = d[i]
                    if phone[0] == '+' and phone[1:].isdigit():
                        cur.execute(sql, (i, ' ', phone))
                    else:
                        print('Phone number is incorrect.')
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    insert_many_numbers(d)

