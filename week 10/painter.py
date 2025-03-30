import pygame
def main():
    pygame.init()
    screen =  pygame.display.set_mode((500, 500))
    canvas = pygame.Surface((500, 500))
    clock = pygame.time.Clock()
    color = 'blue'
    mode = 'circle'
    points = []
    r_start_pos = None
    r_end_pos = None
    c_start_pos = None
    c_end_pos = None
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
                if event.key == pygame.K_e:
                    mode = 'erase'
            if mode == 'rectangle':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        r_start_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        r_end_pos = event.pos
                        draw_rect(canvas, r_start_pos, r_end_pos, color)
                        r_start_pos = None
            elif mode == 'circle':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        c_start_pos = event.pos
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        c_end_pos = event.pos
                        draw_circ(canvas, c_start_pos, c_end_pos, color)
                        c_start_pos = None
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
def erase(screen, pos):
    pygame.draw.circle(screen, (0, 0, 0), pos, 20)
main()
