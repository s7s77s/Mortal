import pygame
import os
import sys
from random import randint

pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 600
FPS = 60
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Mortal')

from loader import *


class Player1(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = "rigth"
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center = (200, 380)
        self.hp_bar = "blue"
        self.key = pygame.key.get_pressed()

    def move(self):
        if self.key[pygame.K_d]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        elif self.key[pygame.K_a]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True

        else:
            if not self.anime_atk:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_SPACE]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

    def attack(self):
        if self.key[pygame.K_e] and not self.anime_atk:
            self.frame = 0
            self.anime_atk = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True

    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_atk:
                    self.current_list_image = player1_image_idle
                    self.anime_atk = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
        elif self.anime_atk:
            self.current_list_image = self.image_lists['atk']
        try:
            if self.dir == "rigth":
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0

    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (0, 0, 600 * self.hp / 100, 50))

    def update(self):
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]
            pygame.draw.circle(sc, 'blue', (x, y), 3)
        if len(set(self.mask_list) & set(player2.mask_list))  > 0 and self.anime_atk and self.flag_damage:
            player2.hp -= 10
            self.flag_damage = False


class Player2(pygame.sprite.Sprite):
    def __init__(self, image_lists):
        pygame.sprite.Sprite.__init__(self)
        self.image_lists = image_lists
        self.image = self.image_lists['idle'][0]
        self.current_list_image = self.image_lists['idle']
        self.rect = self.image.get_rect()
        self.anime_idle = True
        self.anime_run = False
        self.anime_atk = False
        self.frame = 0
        self.timer_anime = 0
        self.dir = "left"
        self.hp = 100
        self.jump_step = -20
        self.jump = False
        self.flag_damage = False
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        self.rect.center = (1000, 380)
        self.hp_bar = "red"
        self.key = pygame.key.get_pressed()

    def move(self):
        if self.key[pygame.K_RIGHT]:
            self.rect.x += 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True
        elif self.key[pygame.K_LEFT]:
            self.rect.x -= 2
            self.anime_idle = False
            if not self.anime_atk:
                self.anime_run = True

        else:
            if not self.anime_atk:
                self.anime_idle = True
            self.anime_run = False

    def jumps(self):
        if self.key[pygame.K_UP]:
            self.jump = True
        if self.jump:
            if self.jump_step <= 20:
                self.rect.y += self.jump_step
                self.jump_step += 1
            else:
                self.jump = False
                self.jump_step = -20

    def attack(self):
        if self.key[pygame.K_q] and not self.anime_atk:
            self.frame = 0
            self.anime_atk = True
            self.anime_idle = False
            self.anime_run = False
            self.flag_damage = True

    def animation(self):
        self.timer_anime += 2
        if self.timer_anime / FPS > 0.1:
            if self.frame == len(self.current_list_image) - 1:
                self.frame = 0
                if self.anime_atk:
                    self.current_list_image = player1_image_idle
                    self.anime_atk = False
                    self.anime_idle = True
            else:
                self.frame += 1
            self.timer_anime = 0
        if self.anime_idle:
            self.current_list_image = self.image_lists['idle']
        elif self.anime_run:
            self.current_list_image = self.image_lists['run']
        elif self.anime_atk:
            self.current_list_image = self.image_lists['atk']
        try:
            if self.dir == "rigth":
                self.image = self.current_list_image[self.frame]
            else:
                self.image = pygame.transform.flip(self.current_list_image[self.frame], True, False)
        except:
            self.frame = 0

    def draw_hp_bar(self):
        pygame.draw.rect(sc, self.hp_bar, (600, 0, 600 * self.hp / 100, 50))

    def update(self):
        self.key = pygame.key.get_pressed()
        self.move()
        self.animation()
        self.attack()
        self.jumps()
        self.draw_hp_bar()
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_outline = self.mask.outline()
        self.mask_list = []
        for i in self.mask_outline:
            self.mask_list.append((i[0] + self.rect.x, i[1] + self.rect.y))
        for point in self.mask_list:
            x = point[0]
            y = point[1]
            pygame.draw.circle(sc, 'red', (x, y), 3)
        if len(set(self.mask_list) & set(player_1.mask_list))  > 0 and self.anime_atk and self.flag_damage:
            player_1.hp -= 10
            self.flag_damage = False


class FON:
    def __init__(self):
        self.timer = 0
        self.frame = 0
        self.image = fon_image

    def update(self):
        self.timer += 2
        sc.blit(self.image[self.frame], (0, 0))
        if self.timer / FPS > 0.1:
            if self.frame == len(self.image) - 1:
                self.frame = 0
            else:
                self.frame += 1
            self.timer = 0


def restart():
    global fon, player_1, player2, player1_group, player2_group
    fon = FON()
    player1_group = pygame.sprite.Group()
    player_1 = Player1({'idle': player1_image_idle, 'run': player1_image_run, 'atk': player1_image_attack})
    player1_group.add(player_1)
    player2_group = pygame.sprite.Group()
    player2 = Player2({'idle': player2_image_idle, 'run': player2_image_run, 'atk': player2_image_attack})
    player2_group.add(player2)


def lvl_game():
    sc.fill('gray')
    fon.update()
    player1_group.update()
    player1_group.draw(sc)
    player2_group.update()
    player2_group.draw(sc)
    pygame.display.update()


restart()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    lvl_game()
    clock.tick(FPS)
