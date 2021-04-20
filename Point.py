import pygame
from config import WHITE, LINEAR_SPEED
from math import cos, sin

class Point(object):
    def __init__(self, cord, center, width, track_radius, color=WHITE, connectedPoint=None, angle_velocty=0):
        self.track_radius = None
        self.cord = cord
        self.angle_velocity = angle_velocty
        self.center = center
        self.width = width
        self.color = color
        self.connectedPoint = connectedPoint
        self.track_radius = track_radius
        self.t = 0
    def move(self, deltaTime):
        self.t += deltaTime
        self.cord = (self.center[0] + self.track_radius * cos(self.angle_velocity*self.t),
                     self.center[1] + self.track_radius * sin(self.angle_velocity*self.t))



    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.cord, self.width)
        if self.connectedPoint is not None:
            pygame.draw.aaline(screen, WHITE, self.cord, self.connectedPoint.cord,2)
