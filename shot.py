from typing import override

import pygame
from circleshape import CircleShape
from pygame import Surface


class Shot(CircleShape):

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: Surface):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, int(self.radius)
        )

    @override
    def update(self, dt: float):
        self.move(dt)

    def move(self, dt: float):
        self.position += self.velocity * dt
