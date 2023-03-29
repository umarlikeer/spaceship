from random import randint
from time import sleep

import pygame

window = pygame.display.set_mode((700, 500))
background = pygame.image.load('ggg (1).jpg')
background = pygame.transform.scale(background, (700, 500))
clock = pygame.time.Clock()

hp_list = ['hp1.png', 'hp2.png', 'hp3.png', 'hp4.png', 'hp5.png', 'hp6.png', 'hp7.png', 'hp8.png', 'hp9.png',
           'hp10.png', 'hp11.png']
explosion_list = ['exp00.png', 'exp01.png', 'exp02.png', 'exp03.png', 'exp04.png', 'exp05.png', 'exp06.png',
                  'exp07.png', 'exp08.png']
hp_image = pygame.transform.scale(pygame.image.load(hp_list[0]), (150, 50))

pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
laser = pygame.mixer.Sound('blaster.mp3')
explosion = pygame.mixer.Sound('explosion.mp3')
class Gamesprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(player_image), (player_width, player_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

    def show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(Gamesprite):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 550:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

    def fire(self):
        bullet = Bullets('laser.png', self.rect.centerx - 13, self.rect.y - 10, 20, 60, 20)
        bullet1 = Bullets('laser1.png', self.rect.centerx + 10, self.rect.y - 10, 20, 60, 10)
        bullet2 = Bullets('laser1.png', self.rect.centerx - 30, self.rect.y - 10, 20, 60, 10)
        bullets.add(bullet)
        bullets.add(bullet1)
        bullets.add(bullet2)


class Enemy(Gamesprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(5, 600)

    def fire(self):
        bullet = Bulletss('laser1 - Copy.png', self.rect.x+45, self.rect.y+60, 10, 30, 20)
        bulletss.add(bullet)

class Bullets(Gamesprite):
    def update(self):
        self.rect.y -= self.speed

class Bulletss(Gamesprite):
    def update(self):
        self.rect.y += self.speed

spaceship = Hero('spaceship1.png', 275, 350, 150, 150, 15)

y = 0
y1 = -500
bullets = pygame.sprite.Group()
bulletss = pygame.sprite.Group()

enemies = pygame.sprite.Group()
# for i in range(20):
#     enemy = Enemy('eee-min.png', randint(5, 600), -100, 100, 100, randint(2, 10))
#     enemies.add(enemy)

pygame.font.init()
font1 = pygame.font.SysFont('Callibean', 40)
kills = 0


game = True
hp_counter = 0
w = 0
e_number = 0
exp_counter = 0
finish = False
def gaming(game, finish, e_number, y, y1, hp_image, w, exp_counter, hp_counter, kills):
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         spaceship.fire()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                spaceship.fire()
                laser.play()

        if finish != True:
            y += 5
            window.blit(background, (0, y))
            y1 += 5
            window.blit(background, (0, y1))
            if y > 500:
                y = -500
            if y1 > 500:
                y1 = -500
            spaceship.show()
            spaceship.move()
            text_kills = font1.render('Score: ' + str(kills), True, (255, 255, 255))
            window.blit(text_kills, (5,80))
            if e_number == 0:
                e_number = 20
                enemy = Enemy('eee-min.png', randint(5, 600), -100, 100, 100, randint(2, 10))
                enemies.add(enemy)
            else:
                e_number -= 1
            enemies.draw(window)
            enemies.update()

            bullets.draw(window)
            bullets.update()
            bulletss.update()
            bulletss.draw(window)
            window.blit(hp_image, (5, 5))

            for e in enemies:
                if w == 0:
                    w = 40
                    e.fire()
                else:
                    w -= 1

            collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
            for collide in collisions:
                exp_image = pygame.transform.scale(pygame.image.load(explosion_list[2]), (100, 100))
                window.blit(exp_image, (collide.rect.x, collide.rect.y))

                kills += 1
            if kills >= 10:
                finish = True

            if pygame.sprite.spritecollide(spaceship, enemies, True) or pygame.sprite.spritecollide(spaceship, bulletss, True):
                hp_image = pygame.transform.scale(pygame.image.load(hp_list[hp_counter]), (150, 50))
                exp_image = pygame.transform.scale(pygame.image.load(explosion_list[exp_counter]), (100, 100))
                window.blit(exp_image, (spaceship.rect.x + 20, spaceship.rect.y))
                exp_counter += 1
                if exp_counter >= 8:
                    exp_counter = 0

                explosion.play()
                hp_counter += 1
            window.blit(hp_image, (5, 5))
            if hp_counter >= 11:
                finish = True
        pygame.display.update()
        clock.tick(60)

background1 = pygame.image.load('ggg (1).jpg')
background1 = pygame.transform.scale(background, (700, 500))
clock1 = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            run = False
            gaming(game, finish, e_number, y, y1, hp_image, w, exp_counter, hp_counter, kills)

    menu = font1.render('Press any key', True, (255, 255, 255))
    window.blit(background1, (0,0))
    window.blit(menu, (260, 200))
    pygame.display.update()
    clock1.tick(60)

