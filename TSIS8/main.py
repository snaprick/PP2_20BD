import pygame, random, time, math, sys
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
COIN_SCORE = 0

bulletImg = pygame.image.load('Images/bullet.png')
bulletX = 0
bulletY = 455
bulletDy = 6
bullet_state = "ready"

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("Images/bg.png")
gameover = pygame.image.load("Images/gameover.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

heart = pygame.image.load("Images/hp.png")
noheart = pygame.image.load("Images/nohp.png")

health = 3

bg_sound = pygame.mixer.Sound('Music/bg_music.mp3')
bg_sound.play()

#строка хп
def health_bar():
    cnt = health
    for i in range(155, 251, 32):
        if cnt > 0:
            DISPLAYSURF.blit(heart, (i, 0))
            cnt -= 1
        else:
            DISPLAYSURF.blit(noheart, (i, 0))


# Отрисовка пули
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    DISPLAYSURF.blit(bulletImg, (x + 16, y + 10))


# Проверка попадания
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 50:
        return True
    else:
        return False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/player.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(center=(160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Enemy(pygame.sprite.Sprite):
    def get_random_speed(self):
        speed = random.randint(1, 5)
        return speed

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/enemy.png")
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(center=(random.randint(40, 360), 0))
        self.speed = self.get_random_speed()

    def move(self):
        global SCORE, bullet_state, bulletY
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600 or isCollision(self.rect.x, self.rect.y, bulletX, bulletY)):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)
            self.speed = self.get_random_speed()
            bullet_state = "ready"
            bulletY = 455


# Класс для монетки
class Coin(pygame.sprite.Sprite):
    def get_random_speed(self):
        speed = random.randint(1, 3)
        return speed

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/coin.png")
        self.surf = pygame.Surface((32, 32))
        self.rect = self.surf.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
        self.speed = self.get_random_speed()

    def move(self):
        global COIN_SCORE
        self.rect.move_ip(0, self.speed)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()
        if pygame.sprite.spritecollideany(P1, coins):
            COIN_SCORE += 1
            pygame.mixer.Sound('Music/coin-sound.mp3').play()
            coins.remove(C1)
            all_sprites.remove(C1)
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            self.speed = self.get_random_speed()


P1 = Player()
E1 = Enemy()
E2 = Enemy()
C1 = Coin()
players = pygame.sprite.Group()
players.add(P1)
enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(E2)

# Монетка каждые 10 сек
COIN_TIME = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_TIME, 10000)

while True:
    for entity in players:
        playerX = entity.rect.x
    for event in pygame.event.get():
        if event.type == COIN_TIME:
            coins.add(C1)
            all_sprites.add(C1)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, WHITE)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_scores = font_small.render(str(COIN_SCORE), True, WHITE)
    DISPLAYSURF.blit(coin_scores, (370, 10))
    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    for entity in enemies:
        if isCollision(entity.rect.x, entity.rect.y, playerX, 480):
            health -= 1
            pygame.mixer.Sound('Music/crash.mp3').play()
            entity.rect = entity.surf.get_rect(center=(random.randint(40, 360), 0))
            entity.speed = entity.get_random_speed()
    if health == 0:
        bg_sound.stop()
        time.sleep(1)
        pygame.mixer.Sound('Music/game_over.mp3').play()
        DISPLAYSURF.blit(gameover, (0, 0))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 455
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletDy
    health_bar()
    pygame.display.update()
    FramePerSec.tick(FPS)
