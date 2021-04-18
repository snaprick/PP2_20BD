import pygame, random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)
C = (100, 100, 100)

color_panel = pygame.image.load("Images/color_panel.png")


def drawRectangle(surface, color, x, y, x1, y1, size):
    pygame.draw.rect(surface, color, [x, y, abs(x1 - x), abs(y - y1)], size)


def drawCircle(surface, color, x, y, x1, y1, size):
    pygame.draw.ellipse(surface, color, [x, y, abs(x1 - x), abs(y - y1)], size)


def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


is_pressed = False
is_rect = True
background = pygame.image.load("Images/bg1.png")


def main(background):
    white_bg = pygame.image.load("Images/bg1.png")
    screen = pygame.display.set_mode((800, 600))
    mode = 'random'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 10
    is_rect = True
    is_circle = True
    is_save = False
    is_clear = False
    is_load = False
    tool = 'kist'
    colors = {
        'red': (255, 0, 0),
        'blue': (0, 0, 255),
        'green': (0, 255, 0),
        'black': (0, 0, 0),
        'eraser': (255, 255, 255)
    }
    screen.blit(background, (0, 0))
    while True:
        screen.blit(color_panel, (0, 550))
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_UP:
                    radius += 1
                if event.key == pygame.K_DOWN:
                    radius -= 1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_rect:
                    prev_pos = pygame.mouse.get_pos()
                    is_rect = False
                if is_circle:
                    prev_pos = pygame.mouse.get_pos()
                    is_circle = False
                if mode == 'random':
                    color = (random.randrange(256), random.randrange(256), random.randrange(256))
                else:
                    color = colors[mode]
                if tool == 'kist':
                    pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
                if 500 <= mouse[1] <= 600:
                    if 0 <= mouse[0] <= 50:
                        mode = 'red'
                    if 51 <= mouse[0] <= 100:
                        mode = 'green'
                    if 101 <= mouse[0] <= 150:
                        mode = 'blue'
                    if 151 <= mouse[0] <= 200:
                        mode = 'black'
                    if 201 <= mouse[0] <= 250:
                        mode = 'eraser'
                    if 251 <= mouse[0] <= 291:
                        radius = 5
                    if 292 <= mouse[0] <= 320:
                        radius = 10
                    if 321 <= mouse[0] <= 360:
                        radius = 15
                    if 441 <= mouse[0] <= 500:
                        tool = 'kist'
                    if 351 <= mouse[0] <= 441:
                        tool = 'rectangle'
                    if 500 <= mouse[0] <= 540:
                        tool = 'circle'
                    if 550 <= mouse[0] <= 595:
                        is_save = True
                    if 596 <= mouse[0] <= 640:
                        is_load = True
                    if 640 <= mouse[0] <= 680:
                        is_clear = True
            if event.type == pygame.MOUSEBUTTONUP:
                eventx = pygame.mouse.get_pos()
                if tool == 'rectangle':
                    drawRectangle(screen, color, prev_pos[0], prev_pos[1], eventx[0], eventx[1], radius)
                    is_rect = True
                if tool == 'circle':
                    drawCircle(screen, color, prev_pos[0], prev_pos[1], eventx[0], eventx[1], radius)
                    is_circle = True
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on and (tool != 'rectangle' and tool != 'circle'):
                    drawLine(screen, last_pos, event.pos, radius, color)
                last_pos = event.pos
        # print(last_pos)
        if is_save:
            pygame.image.save(screen, 'Images/saved_bg.png')
            is_save = False
        if is_clear:
            break
        if is_load:
            save_background = pygame.image.load('Images/saved_bg.png')
            break

        pygame.display.flip()

    if is_clear:
        main(white_bg)
    if is_load:
        main(save_background)
    pygame.quit()


main(background)
