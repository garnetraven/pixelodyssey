import pygame
from pygame.math import Vector2
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((32,64))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.pos = Vector2(self.rect.center)
        self.vel = Vector2(0,0)
        self.speed = 5
        self.gravity = 10  
        self.jump_strength = -50
        self.grounded = False
        self.acceleration = 1  # Acceleration factor
        self.friction = 0.9  # Friction factor

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.vel.x -= self.acceleration
        if keys[pygame.K_d]:
            self.vel.x += self.acceleration
        if keys[pygame.K_SPACE] and self.grounded:
            self.jump()

    def apply_gravity(self):
        self.vel.y += self.gravity
        self.vel.y = min(self.vel.y, 10) # Terminal Velocity
    
    def jump(self):
        self.vel.y = self.jump_strength
        self.grounded = False

    def move(self):
        # Apply friction
        self.vel.x *= self.friction
        self.pos += self.vel
        self.rect.center = self.pos

    def check_collisions(self):
        if self.rect.bottom > SCREENHEIGHT:
            self.rect.bottom = SCREENHEIGHT
            self.pos.y = self.rect.centery
            self.vel.y = 0
            self.grounded = True
        else:
            self.grounded = False

    def update(self):
        self.input()
        self.apply_gravity()
        self.move()
        self.check_collisions()

