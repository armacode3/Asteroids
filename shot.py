import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, vector, velocity):
        super().__init__(vector.x, vector.y, SHOT_RADIUS)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
