import pygame
from pygame.math import Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((32,32))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = Vector2(self.rect.center)
        self.vel = Vector2(0,0)
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        self.vel = Vector2(0,0)

        if keys[pygame.K_a]:
            self.vel.x = -self.speed
        if keys[pygame.K_d]:
            self.vel.x = self.speed

        if self.vel.length() > 0:
            self.vel = self.vel.normalize()

    def move(self):
        self.vel *= self.speed
        self.pos += self.vel
        self.rect.center = self.pos

    def update(self):
        self.input()
        self.move()

