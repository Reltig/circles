import pygame
import sys
from config import *
from Point import Point

clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT),)
isRunning = True


def pointsFabric(count, center, r, width):
    points = []
    step = r / count
    x0, y0 = center[0], center[1]
    ANGLE_VELOCITY = LINEAR_SPEED/step
    points.append(Point(cord = (x0 + step, y0),center =  (x0, y0),
                        width = width, track_radius = step,
                        angle_velocty = ANGLE_VELOCITY))

    for i in range(2, count + 1):
        print(ANGLE_VELOCITY)
        ANGLE_VELOCITY = LINEAR_SPEED/(i * step)
        points.append(Point(cord = (x0 + step * i, y0),
                            center = (x0, y0),track_radius= i * step,width= width,
                            color= WHITE, connectedPoint= points[i - 2], angle_velocty= ANGLE_VELOCITY))

    return points


points = pointsFabric(POINTS_COUNT, (WIN_HEIGHT // 2, WIN_HEIGHT // 2), RADIUS, WIDTH)
clock.tick(FPS)
while isRunning:
    sc.fill(BLACK)
    pygame.draw.circle(sc,WHITE, (WIN_HEIGHT // 2, WIN_HEIGHT // 2), WIDTH)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            isRunning = False
            sys.exit()
    for point in points:
        point.draw(sc)

        point.move(clock.tick(FPS))

    pygame.display.flip()
    clock.tick(FPS)
