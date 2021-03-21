import pygame
import random
from math import sqrt

pygame.init()

width = 500
height = 500
numBoids = 2
visualRange = 75.0
boids = []

class Boid:
    def __init__(self, number):
        self.number = number
        self.x = random.randint(width, width+100)
        self.y = random.randint(height, height+100)
        self.dx = (random.random() * 10) - 5
        self.dy = (random.random() * 10) - 5
        self.history = []

    def coords(self):
        return self.x, self.y


def initPositions ():
    for i in range(numBoids):
        boids.append(Boid(i))

def distance (a, b):
    a = a - 1
    b = b - 1
    return sqrt(((boids[a].x - boids[b].x)**2) + ((boids[a].y - boids[b].y)**2))

screen = pygame.display.set_mode([width, height])

initPositions()
print(boids[0].coords(), boids[1].coords())
print(distance(1, 2))
