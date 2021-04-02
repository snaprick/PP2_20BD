import pygame
import math
from pygame.locals import *

pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TSIS-7")
font = pygame.font.SysFont('times-new-roman', 20)
icon = pygame.image.load('server-icon.png')
pygame.display.set_icon(icon)

showSine = True
showCosine = True
FPS = 160

FPSCLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PI = math.pi

drawSin = font.render('Q - sin', True, BLACK, WHITE)
SinRect = drawSin.get_rect()
SinRect.left = 735
SinRect.bottom = 30
drawCos = font.render('W - cos', True, BLACK, WHITE)
CosRect = drawSin.get_rect()
CosRect.left = 735
CosRect.bottom = 50

x_axis_points = ['-3п', ' 5п', '-2п', ' 3п', '-п ', ' п ', ' 0 ', ' п ', ' п ', ' 3п', ' 2п', ' 5п', ' 3п']
x_axis_points_extra1 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
x_axis_points_extra2 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
y_axis_points = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']

while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_q:
                showSine = not showSine
            elif event.key == K_w:
                showCosine = not showCosine
    screen.fill(WHITE)
    screen.blit(drawSin, SinRect)
    screen.blit(drawCos, CosRect)
    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)  
    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3)  
    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3)  
    pygame.draw.line(screen, BLACK, (70, 40), (730, 40))  
    pygame.draw.line(screen, BLACK, (70, 520), (730, 520))  
    pygame.draw.line(screen, BLACK, (100, 10), (100, 550))
    pygame.draw.line(screen, BLACK, (700, 10), (700, 550))
    if showSine:
        pygame.draw.line(screen, RED, (530, 60), (570, 60))
    if showCosine:
        for x in range(530, 570, 7):
            pygame.draw.line(screen, BLUE, (x, 90), (x + 3, 90))

    for x in range(100, 701, 100):
        if x != 500:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 550))
        else:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 40))
            pygame.draw.line(screen, BLACK, (x, 100), (x, 550))
    for x in range(100, 701, 50):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 530))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 550), (x, 540))

    for y in range(40, 521, 60):
        pygame.draw.line(screen, BLACK, (70, y), (730, y))
    for y in range(40, 521, 30):
        pygame.draw.line(screen, BLACK, (70, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(screen, BLACK, (70, y), (80, y))
        pygame.draw.line(screen, BLACK, (720, y), (730, y))
    if showSine:
        for x in range(100, 700):
            sin_y1 = 240 * math.sin((x - 100) / 100 * PI)
            sin_y2 = 240 * math.sin((x - 99) / 100 * PI)
            pygame.draw.aalines(screen, RED, False, [(x, 280 + sin_y1), ((x + 1), 280 + sin_y2)])
    if showCosine:
        for x in range(100, 700, 3):
            cos_y1 = 240 * math.cos((x - 100) / 100 * PI)
            cos_y2 = 240 * math.cos((x - 99) / 100 * PI)
            pygame.draw.aalines(screen, BLUE, False, [(x, 280 + cos_y1), ((x + 1), 280 + cos_y2)])
    if showSine:
        screen.blit(font.render('sin(x)', False, BLACK), (475, 45))
    if showCosine:
        screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
    screen.blit(font.render('X', False, BLACK), (393, 575))

    for x in range(100, 701, 50):
        screen.blit(font.render(x_axis_points[(x - 100) // 50], False, BLACK), (x - 10, 550))
        screen.blit(font.render(x_axis_points_extra1[(x - 100) // 50], False, BLACK), (x - 20, 550))
        screen.blit(font.render(x_axis_points_extra2[(x - 100) // 50], False, BLACK), (x - 10, 570))
    for y in range(40, 521, 60):
        screen.blit(font.render(y_axis_points[(y - 40) // 60], False, BLACK), (25, (y - 10)))

    pygame.display.flip()
    pygame.display.update()
    FPSCLOCK.tick(FPS)
pygame.quit()
