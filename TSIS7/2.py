import pygame
import math
from pygame.locals import *

pygame.init()
size = width, height = (800, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TSIS-7")
font = pygame.font.SysFont('comicsansms', 17)
icon = pygame.image.load('server-icon.png')
pygame.display.set_icon(icon)

# pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play()

showSine = True
showCosine = True
DoneSin = False
DoneCos = False
FPS = 160

FPSCLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
PI = math.pi

slash = font.render("__", True, BLACK)
two = font.render("2", True, BLACK)
drawWaves = font.render('Toggle waves Q - sin, W - cos', True, BLACK, WHITE)
drawnRect = drawWaves.get_rect()
drawnRect.left = 10
drawnRect.bottom = 630

pos = {'sin': [], 'cos': []}
prevpos = {'sin': [], 'cos': []}
rad = ["-3π", "-5π", "-2π", "-3π", "-π", "-π", "  0", " π", "  π", "3π", "2π", "5π", "3π"]
nums = ['- 3', '- 2', '- 1', ' 0 ', '1', '2']
num = [' 1.00', ' 0.75', ' 0.50', ' 0.25', ' 0.00', '-0.25', '-0.50', '-0.75', '-1.00']


def draw_lines():
    pygame.draw.rect(screen, BLACK, (75, 15, 650, 530), 2)
    for x in range(100, 701, 100):
        if x == 400:
            pygame.draw.line(screen, BLACK, (x, 15), (x, 545), 2)
            continue
        if x != 500:
            pygame.draw.line(screen, BLACK, (x, 15), (x, 545))
        else:
            pygame.draw.line(screen, BLACK, (x, 15), (x, 40))
            pygame.draw.line(screen, BLACK, (x, 100), (x, 545))

    for y in range(40, 521, 60):
        if y == 280:
            pygame.draw.line(screen, BLACK, (75, y), (725, y), 2)
        else:
            pygame.draw.line(screen, BLACK, (75, y), (725, y))


def draw_hatches():
    for x in range(150, 651, 100):
        pygame.draw.line(screen, BLACK, (x, 15), (x, 35))
        pygame.draw.line(screen, BLACK, (x, 525), (x, 545))
    for x in range(125, 701, 50):
        pygame.draw.line(screen, BLACK, (x, 15), (x, 25), 2)
        pygame.draw.line(screen, BLACK, (x, 535), (x, 545), 2)
    for y in range(70, 521, 60):
        pygame.draw.line(screen, BLACK, (75, y), (90, y))
        pygame.draw.line(screen, BLACK, (710, y), (725, y))
    for y in range(55, 521, 30):
        pygame.draw.line(screen, BLACK, (75, y), (85, y))
        pygame.draw.line(screen, BLACK, (715, y), (725, y))
    for x in range(112, 701, 25):
        pygame.draw.line(screen, BLACK, (x, 15), (x, 20))
        pygame.draw.line(screen, BLACK, (x, 540), (x, 545))

def draw_Nums():
    for x, i in zip(range(85, 686, 50), range(13)):
        screen.blit(font.render(rad[i], True, BLACK), (x, 545))
        if i % 2 == 1:
            screen.blit(slash, (x+2, 545))
            screen.blit(two, (x + 8, 564))
    for y, y1 in zip(range(25, 509, 60), num):
        screen.blit(font.render(y1, False, BLACK), (30, y))
    for i, x in zip(nums, range(110, 710, 100)):
        screen.blit(font.render(i, False, BLACK), (x, 280))


# precalc
for x, x1 in zip(range(100, 700), range(101, 701)):
    y1 = 240 * math.sin((x - 100) / 100 * PI) + 280
    y2 = 240 * math.sin((x1 - 100) / 100 * PI) + 280
    prevpos['sin'].append((x, y1))
    pos['sin'].append((x1, y2))
for x, x1 in zip(range(100, 700), range(101, 701)):
    y1 = 240 * math.cos((x - 100) / 100 * PI) + 280
    y2 = 240 * math.cos((x1 - 100) / 100 * PI) + 280
    prevpos['cos'].append((x, y1))
    pos['cos'].append((x1, y2))
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
    # screen.blit(drawSin, SinRect)
    # screen.blit(drawCos, CosRect)
    draw_lines()
    draw_hatches()
    draw_Nums()
    screen.blit(font.render('X', False, BLACK), (393, 575))

    if showSine:
        pygame.draw.line(screen, RED, (530, 60), (570, 60))
        screen.blit(font.render('sin(x)', False, BLACK), (475, 45))
        if showCosine and DoneCos:
            for x in range(530, 570, 11):
                pygame.draw.line(screen, BLUE, (x, 90), (x + 6, 90))
            screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
            i = 0
            for x, y in zip(pos['cos'], prevpos['cos']):
                if i % 3 != 0:
                    pygame.draw.line(screen, BLUE, (x[0], x[1]), (y[0], y[1]))
                i += 1
        for x, y in zip(pos['sin'], prevpos['sin']):
            pygame.draw.aalines(screen, RED, False, [(x[0], x[1]), (y[0], y[1])])
            if not DoneSin:
                pygame.display.update()
                pygame.time.delay(3)
        DoneSin = True
    else:
        DoneSin = False
    if showCosine:
        for x in range(530, 570, 11):
            pygame.draw.line(screen, BLUE, (x, 90), (x + 6, 90))
        screen.blit(font.render('cos(x)', False, BLACK), (475, 75))
        i = 0
        for x, y in zip(pos['cos'], prevpos['cos']):
            if i % 3 != 0:
                pygame.draw.line(screen, BLUE, (x[0], x[1]), (y[0], y[1]))
            if not DoneCos:
                pygame.display.update()
                pygame.time.delay(3)
            i += 1
        DoneCos = True
    else:
        DoneCos = False
    pygame.display.flip()
    pygame.display.update()
    FPSCLOCK.tick(FPS)
