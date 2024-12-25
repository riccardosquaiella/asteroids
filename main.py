import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt: float = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables,)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, (0, 0, 0))

        for updatable in updatables:
            updatable.update(dt)

        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game over!")
                exit()

        pygame.display.flip()
        dt = clock.tick(240) / 1000


if __name__ == "__main__":
    main()
