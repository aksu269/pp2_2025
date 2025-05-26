import psycopg2
from config import load_config


def query():
    
    config = load_config()
    sql = 'select * from phonebook where first_name like %s and phone like %s'
    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, ('A%', '%3%'))
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
    · AI Basics: Overview of AI (English) - Eg0YnF