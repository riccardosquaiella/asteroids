import pygame
from circleshape import CircleShape
from pygame import Surface


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: Surface):
        pygame.draw.circle(
            screen, (255, 255, 255), self.position, self.radius, int(self.radius)
        )

    def update(self, dt: float):
        self.move(dt)

    def move(self, dt: float):
        movement = pygame.Vector2(0, 1) + (self.velocity * dt)
        self.position += movement
