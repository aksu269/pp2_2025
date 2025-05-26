import psycopg2
from config import load_config


def find_pattern():
    filter_type = input('Select filter type (f, l, p):')
    pattern = input('Enter the pattern for the search:')
    config = load_config()
    if filter_type == 'f':
        sql = """SELECT * FROM phonebook WHERE first_name LIKE %s;"""
    elif filter_type == 'l':
        sql = """SELECT * FROM phonebook WHERE last_name like %s"""
    else:
        sql = """SELECT * FROM phonebook WHERE phone like %s"""
    pattern_like = f"%{pattern}%"
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (pattern_like,))
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
    find_pattern()