import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, LINE_WIDTH)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass