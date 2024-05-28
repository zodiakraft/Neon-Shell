#!/usr/bin/python3

import sys
import random
import pygame
size = width, height = 1600, 900

x1, x2 = 5, width - 5
y1, y2 = 5, height - 150

h_border = pygame.sprite.Group() #группа спрайтов - горизонаьльные препятствия
v_border = pygame.sprite.Group() #группа спрайтов - вертикальные стенки
all_sprites = pygame.sprite.Group() # в эту группу добавляют все спрайты - мячи

# горизонтальная стенка
class Borderh(pygame.sprite.Sprite): # создаем класс Sprite
    def __init__(self, x1, y1, x2, y2):
        super().__init__(h_border)
        self.add(h_border)
        self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

# вертикальная стенка
class Borderv(pygame.sprite.Sprite): # создаем класс Sprite
    def __init__(self, x1, y1, x2, y2):
        super().__init__(v_border)
        self.add(v_border)
        self.rect = pygame.Rect(x1, y1, 1, y2 - y1)

# спрайт - мяч
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image1 = pygame.image.load('tank_exp.png')
        self.w = self.image1.get_width() #// 15
        self.h = self.image1.get_height() #// 15
        self.image = pygame.transform.scale(self.image1, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.vx = 1
        self.vy = 0
        self.angle = 0
# в начале мяч в центре
        self.rect.left = width // 2
        self.rect.top = height // 2

    def blitRotate(self, surf, image, pos, originPos, angle):
    
        # offset from pivot to center
        self.image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - self.image_rect.center
        
        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(image, angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        # rotate and blit the image
        surf.blit(rotated_image, rotated_image_rect)
    
        # draw rectangle around the image
        # pygame.draw.rect(surf, (255, 0, 0), (*rotated_image_rect.topleft, *rotated_image.get_size()),2)

    def update(self):
        keys = pygame.key.get_pressed()
 
        if keys[pygame.K_a]:
            self.angle += 1
            self.w, self.h = self.image.get_size()
            self.blitRotate(sc, self.image, (self.rect.left, self.rect.top), (self.w // 2, self.h // 2), self.angle)
            # print(self.rect.left, self.rect.top)
            # self.image, self.rect = self.rot_center(self.image1, self.angle, self.rect.left, self.rect.top)
            # self.image = pygame.transform.rotate(pygame.transform.scale(self.image1, (self.w, self.h)), self.angle)
            # self.rect = self.image.get_rect(center = image.get_rect(topleft = topleft).center)
        elif keys[pygame.K_d]:
            self.angle -= 1
            # self.image = pygame.transform.rotate(pygame.transform.scale(self.image1, (self.w, self.h)), self.angle)
            # self.rect = self.image.get_rect(center = self.image.get_rect(topleft = topleft).center)
        elif keys[pygame.K_w]:
            # self.rect = self.image.get_rect()
            self.rect = self.rect.move(self.vx, self.vy) #  шаг спрайта
        elif keys[pygame.K_s]:
            # self.rect = self.image.get_rect(center = image.get_rect(topleft = topleft).center)
            self.rect = self.rect.move(self.vx*(-1), self.vy) #  шаг спрайта
        if pygame.sprite.spritecollideany(self, h_border): # проверяем столкновение мяча с группой спрайтов "горизонтальные препятствия"
            self.vy = 0
        if pygame.sprite.spritecollideany(self, v_border): # проверяем столкновение мяча с группой спрайтов "вертикальные стенки"
            self.vx = 0


pygame.init() # инициализация pygame
sc = pygame.display.set_mode(size)
pygame.display.set_caption('Движение спрайтов')

# четыре препятствия (границы -  стены, потолок, пол)
Borderh(x1, y1, x2, y1)
Borderh(x1, y2, x2, y2)
Borderv(x1, y1, x1, y2)
Borderv(x2, y1, x2, y2)

Ball()

running = True
while running:
    sc.fill((0, 0, 0))
    all_sprites.draw(sc)
    all_sprites.update()
    pygame.draw.rect(sc, (200, 200, 200), (x1, y1, x2, y2), 2)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()