import psycopg2
from config_s import load_config

def create_tables():
    """Create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(user_id) ON DELETE CASCADE,
            level INTEGER NOT NULL,
            score INTEGER NOT NULL,
            game_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Tables created successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error creating table:", error)

if __name__ == '__main__':
    create_tables()
