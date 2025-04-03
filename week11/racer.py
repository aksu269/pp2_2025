import pygame, sys
from pygame.locals import *
import random, time
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()
SPEED = 5
SCORE = 0
COINS = 0
last_coin_time = 0
COIN_DELAY = 300

BLUE  = (0, 0, 255)
RED   = (184, 15, 10)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.mixer.Sound('background.wav').play()
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1= pygame.image.load("gold_coin.png")
        self.image2 = pygame.image.load("silver_coin.png")
        self.rect = self.image1.get_rect()
        self.respawn()
    def respawn(self):
        self.rect.center = (random.randint(30, 370), 520)
        self.is_gold= random.choice([True, False])
    def appear(self, surface):
        if self.is_gold:
            surface.blit(self.image1, self.rect)
        else:
            surface.blit(self.image2, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)
P1 = Player()
E1 = Enemy()
C1 = Coins()
coins_group = pygame.sprite.Group()
coins_group.add(C1)

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(f"Score: {SCORE}", True, BLACK)
    coins = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins, (300, 10))
    

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    current_time = pygame.time.get_ticks()
    C1.appear(DISPLAYSURF)
    if pygame.sprite.spritecollideany(P1, coins_group):
        if current_time - last_coin_time > COIN_DELAY: 
            if C1.is_gold:
                COINS += 3
                SPEED += 1
            else:
                COINS += 1
                SPEED += 0.5
            last_coin_time = current_time 
            C1.respawn()
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit() 
    pygame.display.update()
    FramePerSec.tick(FPS)