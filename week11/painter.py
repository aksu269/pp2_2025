import pygame
import math
def main():
    pygame.init()
    screen =  pygame.display.set_mode((500, 500))
    canvas = pygame.Surface((500, 500))
    clock = pygame.time.Clock()
    color = 'blue'
    mode = 'circle'
    points = []
    start_pos = None
    end_pos = None
    while True:
        screen.fill((0, 0, 0))
        screen.blit(canvas, (0, 0)) 
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_p:
                    color = 'pink'
                elif event.key == pygame.K_g:
                    color = 'green'
                elif event.key == pygame.K_b:
                    color = 'blue'
                if event.key == pygame.K_r:
                    mode = 'rectangle'
                if event.key == pygame.K_c:
                    mode = 'circle'
                if event.key == pygame.K_s:
                    mode = 'square'
                if event.key == pygame.K_t:
                    mode = 'right triangle'
                if event.key == pygame.K_e:
                    mode = 'erase'
                if event.key == pygame.K_q:
                    mode = 'equilateral triangle'
                if event.key == pygame.K_h:
                    mode = 'rhombus'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    start_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    end_pos = event.pos
                    if mode == 'rectangle':
                        draw_rect(canvas, start_pos, end_pos, color)
                    elif mode == 'circle':
                        draw_circ(canvas, start_pos, end_pos, color)
                    elif mode == 'square':
                        draw_square(canvas, start_pos, end_pos, color)
                    elif mode == 'right triangle':
                        draw_right_triangle(canvas, start_pos, end_pos, color)
                    elif mode == 'equilateral triangle':
                        draw_equilateral_triangle(canvas, start_pos, end_pos, color)
                    elif mode == 'rhombus':
                        draw_rhombus(canvas, start_pos, end_pos, color)
                    start_pos = None
            
            elif mode == 'erase':
                if event.type == pygame.MOUSEMOTION:
                    erase(canvas, event.pos)
        
        pygame.display.flip()

        clock.tick(60)
    
def draw_rect(screen, start_pos, end_pos, color_mode):
    
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)

    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    height = abs(start_pos[1] - end_pos[1])
    pygame.draw.rect(screen, color, (x, y, width, height), 0)
def draw_circ(screen, start_pos, end_pos, color_mode):
    
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)

    x = (start_pos[0] + end_pos[0]) // 2
    y = (start_pos[1] + end_pos[1]) // 2
    rad = (((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2)**0.5) // 2
    pygame.draw.circle(screen, color, [x, y], rad, 0)

def draw_square(screen, start_pos, end_pos, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)

    x = min(start_pos[0], end_pos[0])
    y = min(start_pos[1], end_pos[1])
    width = abs(start_pos[0] - end_pos[0])
    pygame.draw.rect(screen, color, (x, y, width, width), 0)
#def control_panel(screen):
def draw_right_triangle(screen, start_pos, end_pos, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)

    a = start_pos
    b = (start_pos[0], end_pos[1]) 
    c = end_pos
    pygame.draw.polygon(screen, color, [a, b, c])

def draw_equilateral_triangle(screen, start_pos, end_pos, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)
    a = start_pos
    c = end_pos
    side_length = math.dist(a, c)
    height = (math.sqrt(3) / 2) * side_length
    b = ((end_pos[0] + start_pos[0])/2, start_pos[1] - height)
    pygame.draw.polygon(screen, color, [a, b, c])

def draw_rhombus(screen, start_pos, end_pos, color_mode):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'pink':
        color = (255, 192, 203)
    elif color_mode == 'green':
        color = (0, 255, 0)
    

    center_x = (start_pos[0] + end_pos[0]) / 2
    center_y = (start_pos[1] + end_pos[1]) / 2

    half_width = abs(end_pos[0] - start_pos[0]) / 2
    half_height = abs(end_pos[1] - start_pos[1]) / 2

    top = (center_x, center_y - half_height)
    right = (center_x + half_width, center_y)
    bottom = (center_x, center_y + half_height)
    left = (center_x - half_width, center_y)

    pygame.draw.polygon(screen, color, [top, right, bottom, left])


def erase(screen, pos):
    pygame.draw.circle(screen, (0, 0, 0), pos, 20)
main()