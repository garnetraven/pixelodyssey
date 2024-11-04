import pygame
from pygame.math import Vector2
from globals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, block_group):
        super().__init__()
        self.image = pygame.Surface((TILESIZE * 2, TILESIZE * 3))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.pos = Vector2(self.rect.center)
        self.gravity = 10
        self.speed = 5
        self.jump_strength = -50
        self.mass = 1
        self.velocity = Vector2(0, 0)
        self.grounded = False
        self.block_group = block_group
        self.acceleration = 1
        self.friction = 0.9

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.velocity.x -= self.acceleration
        if keys[pygame.K_d]:
            self.velocity.x += self.acceleration
        if keys[pygame.K_SPACE] and self.grounded:
            self.jump()

    def apply_gravity(self):
        if not self.grounded:  # Only apply gravity if not grounded
            self.velocity.y += self.gravity * self.mass
            if self.velocity.y > 10:  # Terminal velocity
                self.velocity.y = 10

    def jump(self):
        self.velocity.y = self.jump_strength  # Set jump velocity
        self.grounded = False

    def move(self):
        # Apply friction to horizontal movement
        self.velocity.x *= self.friction

        # Applying velocity
        self.rect.x += self.velocity.x
        self.check_collisions('horizontal')
        self.rect.y += self.velocity.y
        self.check_collisions('vertical')

    def check_collisions(self, dir: str):
        if dir == "horizontal":
            # Block group collision
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.x > 0:  # Moving right
                        self.rect.right = block.rect.left
                    elif self.velocity.x < 0:  # Moving left
                        self.rect.left = block.rect.right
        elif dir == "vertical":
            collisions = 0
            # Block group collision
            for block in self.block_group:
                if block.rect.colliderect(self.rect):
                    if self.velocity.y > 0:  # Moving down
                        self.rect.bottom = block.rect.top
                        collisions += 1
                    elif self.velocity.y < 0:  # Moving up
                        self.rect.top = block.rect.bottom
                        self.velocity.y = 0.1
            
            if collisions > 0:
                self.grounded = True
                self.velocity.y = 0.1  # Small value to keep grounded
            else:
                self.grounded = False

    def update(self):
        self.input()
        self.apply_gravity()
        self.move()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.rect(surface, (255, 0, 0), self.rect, 2)  # Draw the player rect in red for debugging

