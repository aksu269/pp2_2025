import pygame
pygame.init()
done = False
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
x = 25
y = 25
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 45: y -= 20
    elif pressed[pygame.K_DOWN] and y <= 355: y += 20
    elif pressed[pygame.K_RIGHT] and x <= 355: x += 20
    elif pressed[pygame.K_LEFT] and x >= 45: x -= 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)