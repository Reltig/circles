import pygame
import sys

FPS = 60
WIN_WIDTH = 960
WIN_HEIGHT = 960
WHITE = (255, 255, 255)
BLACK = (0,0,0)
clock = pygame.time.Clock()
LINEAR_SPEED = 20
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
isRunning = True

class Point(object):
    def __init__(self, x, y, velocity, center, connectedPoint, color,radius):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.center = center
        self.connectedPoint = connectedPoint
        self.color = color
        self.radius = radius

    def move(self, deltaTime):
        pass

    def draw(self):
        pygame.draw.circle(sc, WHITE,(self.x,self.y),self.radius)
        pygame.draw.aaline(sc, WHITE, (self.x, self.y), (connectedPoint.x, connectedPoint.y))




def pointsFabric(count, r, center):
    points = []
    points.append(Point(center[0]+r/count, center[1], ))
    for i in range(1, count+1):
        points.append(Point(x, y, ))



while isRunning:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            isRunning = False
            sys.exit()
    sc.fill(BLACK)
    clock.tick(FPS)