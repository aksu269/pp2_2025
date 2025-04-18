import psycopg2
from config import load_config

def create_tables():
    """Create tables in the PostgreSQL database"""
    command = """
        CREATE TABLE IF NOT EXISTS phonebook (
            phone_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                print("Table 'phonebook' created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating table:", error)

if __name__ == '__main__':
    create_tables()
