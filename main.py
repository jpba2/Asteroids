import pygame
from constants import *
from logger import log_state
from player import *
from circleshape import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroidbelt = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()
