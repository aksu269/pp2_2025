import psycopg2
from config import load_config
import csv
def insert_many_numbers(file_name):
    """ Insert multiple vendors into the vendors table  """
    sql = "INSERT INTO phonebook(first_name, last_name, phone) VALUES(%s, %s, %s) RETURNING *"
    config = load_config()
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            data_list = [(row['first_name'], row['last_name'], row['phone']) for row in csv_reader]
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.executemany(sql, data_list)
            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
if __name__ == '__main__':
    insert_many_numbers('numbers.csv')

