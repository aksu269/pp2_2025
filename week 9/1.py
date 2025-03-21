import pygame
import datetime
pygame.init()
center = (250, 250)
screen = pygame.display.set_mode((500, 500))

image = pygame.image.load('mickeyclock.png')
image = pygame.transform.scale(image, (500, 500))
left_hand =  pygame.image.load('minute.png')
right_hand =  pygame.image.load('second.png')
done = False
clock = pygame.time.Clock()
def rotate_center(surf, image, angle, pos):
        rotated_image = pygame.transform.rotate(image, -angle)
        rect = rotated_image.get_rect(center = pos)
        surf.blit(rotated_image, rect.topleft)
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        now = datetime.datetime.now()
        second = now.second
        minute = now.minute + second/60
        
        second_angle = second*6
        minute_angle = minute*6

        screen.fill((255, 255, 255))
        screen.blit(image, (0, 0))
        rotate_center(screen, right_hand, second_angle, center)
        rotate_center(screen, left_hand, minute_angle, center)
        pygame.display.flip()
        clock.tick(60)