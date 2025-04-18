import pygame, sys
from game_object import GameObject 
import time
import psycopg2
from config_s import load_config

from worm import Worm
from food import Food
from wall import Wall
from login import user_login

def create_background(screen, width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(screen, colors[(row + col) % 2],pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width

done = False
def check_collision(worm, wall):
        if worm.points[0].X > 380 or worm.points[0].X < 0 or worm.points[0].Y > 280 or worm.points[0].Y < 0:
                return True
        for wall_point in wall.points:
                if wall_point.X == worm.points[0].X and wall_point.Y == worm.points[0].Y:
                        return True
        for worm_point in worm.points[1:]:
                if worm.points[0] == worm_point:
                        return True
        return False
pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

font = pygame.font.SysFont("dejavusans", 60)
font_small = pygame.font.SysFont("dejavusans", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

SPEED = 4
SCORE = 0
LEVEL = 1


worm = Worm(20)
food = Food(20)
wall = Wall(20)
config = load_config()
user_id, level = user_login(config)


while not done:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            else:
                filtered_events.append(event)

        worm.process_input(filtered_events)
        worm.move()
        pos = food.can_eat(worm.points[0])
        if(pos != None):
            worm.increase(pos)
            SCORE += food.weight 
            SPEED += 0.5
            food.respawn(wall, worm)
            if len(worm.points) % 3 == 0:
                wall.next_level()
                LEVEL += 1
        create_background(screen, 400, 300)
        score = font_small.render(f"Score: {SCORE}", True, (0, 0, 0))
        level = font_small.render(f"Level: {LEVEL}", True, (0, 0, 0))
        screen.blit(score,(10, 0))
        screen.blit(level, (10, 20))
        food.update(wall, worm)
        food.draw(screen)
        wall.draw(screen)
        worm.draw(screen)
        if check_collision(worm, wall):
                try:
                        with psycopg2.connect(**config) as conn:
                                with conn.cursor() as cur:
                                        cur.execute("""
                                                INSERT INTO user_score (user_id, score, level, game_date) 
                                                VALUES (%s, %s, %s, CURRENT_TIMESTAMP) RETURNING score_id;
                                        """, (user_id, SCORE, LEVEL))  
                                        conn.commit()

                        screen.fill((255, 0, 0))
                        screen.blit(game_over, (65, 110))
                        pygame.display.update()
                        time.sleep(1)
                        pygame.quit()
                        sys.exit()

                except (Exception, psycopg2.DatabaseError) as error:
                        print("Error while saving score:", error)

        pygame.display.flip()
        clock.tick(SPEED)