import random
from typing import override

import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
from pygame import Surface


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: Surface):
        _ = pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, int(self.radius)
        )

    @override
    def update(self, dt: float):
        self.move(dt)

    def move(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_a = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        asteroid_b = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        asteroid_a.velocity = self.velocity.rotate(random_angle) * 1.2
        asteroid_b.velocity = self.velocity.rotate(random_angle * -1) * 1.2
