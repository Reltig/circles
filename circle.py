import pygame
import sys
from config import *
import Point

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
isRunning = True


def pointsFabric(count, center, r):
    points = []
    step = r / count
    x0, y0 = center[0], center[1]
    points.append(Point(x0 + step, y0, ))
    for i in range(2, count + 1):
        points.append(Point(x, y, ))
    return points


points = pointsFabric(POINTS_COUNT, (WIN_HEIGHT // 2, WIN_HEIGHT // 2), RADIUS)
while isRunning:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            isRunning = False
            sys.exit()
    sc.fill(BLACK)
    clock.tick(FPS)
