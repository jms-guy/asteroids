#Class for asteroids

from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = (random.uniform(20, 50))
            vector_one = self.velocity.rotate(rand_angle)
            vector_two = self.velocity.rotate(-rand_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_one.velocity = vector_one * 1.2
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two.velocity = vector_two * 1.2

