from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        velocity_a = self.velocity.rotate(angle) * 1.2
        velocity_b = self.velocity.rotate(-angle) * 1.2

        Asteroid(self.position.x, self.position.y, new_radius, velocity_a)
        Asteroid(self.position.x, self.position.y, new_radius, velocity_b)
