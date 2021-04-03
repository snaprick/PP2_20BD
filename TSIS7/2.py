import pygame
import math
from pygame.locals import *

pygame.init()
size = width, height = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TSIS-7")
font = pygame.font.SysFont('times-new-roman', 20)
icon = pygame.image.load('server-icon.png')
pygame.display.set_icon(icon)

showSine = True
showCosine = True
DoneSin = False
DoneCos = False
FPS = 160

FPSCLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PI = math.pi

drawWaves = font.render('Toggle waves', True, BLACK, WHITE)
drawnRect = drawWaves.get_rect()
drawnRect.left = 735
drawnRect.bottom = 30
drawSin = font.render('Q - sin', True, BLACK, WHITE)
SinRect = drawSin.get_rect()
SinRect.left = 735
SinRect.bottom = 55
drawCos = font.render('W - cos', True, BLACK, WHITE)
CosRect = drawSin.get_rect()
CosRect.left = 735
CosRect.bottom = 75

pos = {'sin': [], 'cos': []}
prevpos = {'sin': [], 'cos': []}
dx1 = ['-3π', ' 5π', '-2π', ' 3π', '-π ', ' π ', ' 0 ', ' π ', ' π ', ' 3π', ' 2π', ' 5π', ' 3π']
dx2 = ['', '_ __', '', '_ __', '', '_ _', '', '   _', '', '   __', '', '   __', '']
dx3 = ['', '  2', '', '  2', '', ' 2', '', ' 2', '', '  2', '', '  2', '']
num = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']


def draw_lines(screen):
    pygame.draw.rect(screen, BLACK, (70, 10, 660, 540), 2)
    pygame.draw.line(screen, BLACK, (70, 280), (730, 280), 3)
    pygame.draw.line(screen, BLACK, (400, 10), (400, 550), 3)
    pygame.draw.line(screen, BLACK, (70, 40), (730, 40))
    pygame.draw.line(screen, BLACK, (70, 520), (730, 520))
    pygame.draw.line(screen, BLACK, (100, 10), (100, 550))
    pygame.draw.line(screen, BLACK, (700, 10), (700, 550))
    for x in range(100, 701, 100):
        if x != 500:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 550))
        else:
            pygame.draw.line(screen, BLACK, (x, 10), (x, 40))
            pygame.draw.line(screen, BLACK, (x, 100), (x, 550))
    for y in range(40, 521, 60):
        pygame.draw.line(screen, BLACK, (70, y), (730, y))

def hatches(screen):
    for x in range(100, 701, 50):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 30))
        pygame.draw.line(screen, BLACK, (x, 530), (x, 550))
    for x in range(100, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 10), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 540), (x, 550))
    for y in range(40, 521, 30):
        pygame.draw.line(screen, BLACK, (70, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (730, y))
    for y in range(40, 521, 15):
        pygame.draw.line(screen, BLACK, (70, y), (80, y))
        pygame.draw.line(screen, BLACK, (720, y), (730, y))


def drawNums():
    for x, x1, x2, x3 in zip(range(90, 691, 50), dx1, dx2, dx3):
        screen.blit(font.render(x1, False, BLACK), (x, 550))
        screen.blit(font.render(x2, False, BLACK), (x - 10, 550))
        screen.blit(font.render(x3, False, BLACK), (x, 570))
    for y, y1 in zip(range(28, 509, 60), num):
        screen.blit(font.render(y1, False, BLACK), (25, y))


# precalc
for x in range(100, 700):
    y1 = 240 * math.sin((x - 100) / 100 * PI)
    y2 = 240 * math.sin((x - 99) / 100 * PI)
    prevpos['sin'].append((x, 280 + y1))
    pos['sin'].append((x + 1, 280 + y2))
for x in range(100, 700, 3):
    y1 = 240 * math.cos((x - 100) / 100 * PI)
    y2 = 240 * math.cos((x - 99) / 100 * PI)
    prevpos['cos'].append((x, 280 + y1))
    pos['cos'].append((x + 1, 280 + y2))
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
    screen.blit(drawWaves, drawnRect)
    screen.blit(drawSin, SinRect)
    screen.blit(drawCos, CosRect)
    draw_lines(screen)
    hatches(screen)
    drawNums()
    screen.blit(font.render('X', False, BLACK), (393, 575))

    if showSine:
        pygame.draw.line(screen, RED, (530, 60), (570, 60))
        screen.blit(font.render('sin(x)', False, BLACK), (475, 45))
        if showCosine and DoneCos:
            for x in range(530, 570, 7):
                pygame.draw.line(screen, BLUE, (x, 90), (x + 3, 90))
            screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
            for x, y in zip(pos['cos'], prevpos['cos']):
                pygame.draw.aalines(screen, BLUE, False, [(x[0], x[1]), (y[0], y[1])])
        for x, y in zip(pos['sin'], prevpos['sin']):
            pygame.draw.aalines(screen, RED, False, [(x[0], x[1]), (y[0], y[1])])
            if not DoneSin:
                pygame.display.update()
                pygame.time.delay(3)
        DoneSin = True
    else:
        DoneSin = False
    if showCosine:
        for x in range(530, 570, 7):
            pygame.draw.line(screen, BLUE, (x, 90), (x + 3, 90))
        screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
        for x, y in zip(pos['cos'], prevpos['cos']):
            pygame.draw.aalines(screen, BLUE, False, [(x[0], x[1]), (y[0], y[1])])
            if not DoneCos:
                pygame.display.update()
                pygame.time.delay(10)
        DoneCos = True
    else:
        DoneCos = False
    pygame.display.flip()
    pygame.display.update()
    FPSCLOCK.tick(FPS)
