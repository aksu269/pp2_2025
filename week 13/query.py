import psycopg2
from config import load_config


def query():
    filter_type = input('Select filter type (f, l, p):')
    search = input('Enter the value for the search:')
    config = load_config()
    if filter_type == 'f':
        sql = """SELECT * FROM phonebook WHERE first_name = %s"""
    elif filter_type == 'l':
        sql = """SELECT * FROM phonebook WHERE last_name = %s"""
    else:
        sql = """SELECT * FROM phonebook WHERE phone = %s"""
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (search,))
                results = cur.fetchall()

                if results:
                    print("\nResults:")
                    for row in results:
                        print(row)
                else:
                    print("No data.")
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    query()