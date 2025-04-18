import psycopg2
from config_s import load_config

def user_login(config):
    user_name = input('Enter your username: ')
    sql = '''SELECT user_id FROM users WHERE username = %s'''
    sql2 = '''SELECT level FROM user_score WHERE user_id = %s ORDER BY game_date DESC LIMIT 1'''
    sql3 = '''INSERT INTO users (username) VALUES (%s) RETURNING user_id'''

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_name,))
                result = cur.fetchone()

                if result:
                    user_id = result[0]
                    cur.execute(sql2, (user_id,))
                    level_row = cur.fetchone()

                    if level_row is not None and level_row[0] is not None:
                        level = level_row[0]


                    print(f'Welcome back, {user_name}! Your current level: {level}')
                else:
                    cur.execute(sql3, (user_name,))
                    user_id = cur.fetchone()[0]
                    conn.commit()
                    level = 1
                    print(f'New user created: {user_name} (Level: {level})')

                return user_id, level

    except Exception as error:
        print("Error during login:", error)
        return None, 1