from typing import Self

import pygame
from pygame.sprite import Group


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: tuple[Group, ...] = ()

    def __init__(self, x: float, y: float, radius: float):

        super().__init__(*self.containers)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def colliding(self, entity: Self) -> bool:
        return self.position.distance_to(entity.position) <= self.radius + entity.radius
