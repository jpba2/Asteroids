import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        rand_angle = random.uniform(20, 50)
        sub_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid_1.velocity = self.velocity.rotate(rand_angle) * 1.2
        sub_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        sub_asteroid_2.velocity = self.velocity.rotate(-rand_angle) * 1.2
