import pygame
from config import WHITE


class Point(object):
    def __init__(self, x, y, velocity, center, radius, color, connectedPoint = None):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.center = center
        self.radius = radius
        self.color = color
        self.connectedPoint = connectedPoint

    def move(self, deltaTime):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
        if self.connectedPoint is not None:
            pygame.draw.aaline(screen, WHITE, (self.x, self.y), (self.connectedPoint.x, self.connectedPoint.y))
