import pygame
import sys
import os
from pygame.locals import *
from random import randint
from time import sleep

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60
ok = False

car_width, car_length = 40, 80
speed = 5

score = 0
temp_cnt = 0

font = pygame.font.SysFont('Calibri', 60)
font_score = pygame.font.SysFont('Calibri', 20)
game_over = font.render('Game Over!', True, black)

bg = pygame.image.load(r'images\street.png')

pygame.mixer.music.load(r'musics\background.wav')
pygame.mixer.music.play(-1)


class Player(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(os.path.join(r'images\4.png'))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 - car_width/2, HEIGHT - car_length)

    def move(self):
        pressed = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed[K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < WIDTH:
            if pressed[K_RIGHT]:
                self.rect.move_ip(10, 0)


class Enemy(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.image = pygame.image.load(r'images\1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (randint(car_width, WIDTH-car_width), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (randint(30, 370), 0)
            score += 1


coin_cnt = 0
font_coin = pygame.font.SysFont('Calibri', 20)


class Coin(pygame.sprite.Sprite):
    def init(self):
        super().init()
        self.type = randint(1, 10)
        if 1 <= self.type <= 3:
            self.letter = '10'
            self.cost = 10
        elif 4 <= self.type <= 6:
            self.letter = '5'
            self.cost = 5
        else:
            self.letter = '2'
            self.cost = 2

        self.image = pygame.transform.scale(pygame.image.load('images/coin_'+self.letter+'.png'), (50, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, WIDTH-50), 0)

        self.disappear()

    def move(self):
        self.rect.move_ip(0, 3)
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (randint(50, WIDTH-50), 0)

    def disappear(self):
        self.rect.top = 0
        self.rect.center = (randint(40, WIDTH-50), 0)

        self.type = randint(1, 10)
        if self.type == 1:
            self.letter = '10'
            self.cost = 10
        elif 2 <= self.type <= 4:
            self.letter = '5'
            self.cost = 5
        else:
            self.letter = '2'
            self.cost = 2

        self.image = pygame.transform.scale(pygame.image.load('images/coin_'+self.letter+'.png'), (50, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, WIDTH-50), 0)


p = Player()
e = Enemy()
c = Coin()


enemies = pygame.sprite.Group()
enemies.add(e)

all_sprites = pygame.sprite.Group()
all_sprites.add(p)
all_sprites.add(e)
all_sprites.add(c)

coins = pygame.sprite.Group()
coins.add(c)
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 5000)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == inc_speed:
            if ok:
                speed += 1
                ok = False

    screen.blit(bg, (0, 0))

    show = font_score.render(f'P:{str(score)}', True, black)
    screen.blit(show, (WIDTH-38, 20))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    coin_show = font_coin.render(f'$:{str(coin_cnt)}', True, black)
    screen.blit(coin_show, (WIDTH-38, 50))

    if pygame.sprite.spritecollideany(p, coins):
        pygame.mixer.Soundr('musics\collect.mp3').play()
        coin_cnt += c.cost
        temp_cnt += c.cost
        if temp_cnt > 15:
            ok = True
            temp_cnt = 0
        c.disappear()

    if pygame.sprite.spritecollideany(p, enemies):
        screen.fill(red)

        pygame.mixer.music.stop()
        pygame.mixer.Sound(r'musics\crash.wav').play()

        screen.blit(game_over, (35, 250))

        font = pygame.font.SysFont('Calibri', 30)
        total = font.render(f'Total score: {str(score)}', True, black)
        screen.blit(total, (100, 350))

        font = pygame.font.SysFont('Calibri', 30)
        total = font.render(f'Total money: {str(coin_cnt)}', True, black)
        screen.blit(total, (100, 400))

        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
