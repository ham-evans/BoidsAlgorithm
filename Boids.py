import pygame
import random
from math import sqrt
from copy import deepcopy
from operator import attrgetter

#pygame.init()

width = 500
height = 500
numBoids = 3
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
        self.distanceFrom = 0

    def coords(self):
        return self.x, self.y

def initPositions ():
    for i in range(numBoids):
        boids.append(Boid(i))

def distance (a, b):
    a = a - 1
    b = b - 1
    return sqrt(((boids[a].x - boids[b].x)**2) + ((boids[a].y - boids[b].y)**2))

def nClosest (boidNum, n):
    for i in range(len(boids)):
        boids[i].distanceFrom = distance(boidNum, i)
    closest = sorted(boids, key=lambda boid: boid.distanceFrom)
    return closest[1:n+1]

def keepWithinBounds (boidNum):
    margin = 490
    turnFactor = 1

    if boidNum.x < margin:
        boidNum.dx += turnFactor

    if boidNum.x > width-margin:
        boidNum.dx -= turnFactor

    if boidNum.y < margin
      boidNum.dy += turnFactor

    if boidNum.y > height - margin
      boidNum.dy -= turnFactor

def flyToCenter (boidNum):
    centeringFactor = 0.005 # Adjust velo here
    centerX = 0
    centerY = 0
    numNeighbors = 0

    for i in range(numBoids):
        if i != boidNum:
            if distance(boidNum, i) < visualRange:
                centerX += boids[i].x
                centerY += boids[i].y
                numNeighbors += 1

    if numNeighbors != 0:
        centerX = centerX / numNeighbors
        centerY = centerY / numNeighbors

        boids[boidNum].dx += (centerX - boids[boidNum].x) * centeringFactor
        boids[boidNum].dy += (centerY - boids[boidNum].y) * centeringFactor

def avoidOthers (boidNum):
    minDistance = 20
    avoidFactor = 0.05 # Adjust velo here
    moveX = 0
    moveY = 0

    for i in range(numBoids):
        if i != boidNum:
            if distance(boidNum, i) < minDistance:
                moveX += boids[boidNum].x - boids[i].x
                moveY += boids[boidNum].y - boids[i].y

    boids[boidNum].dx += moveX * avoidFactor
    boids[boidNum].dy += moveY * avoidFactor

def matchVelocity (boidNum):
    matchingFactor = 0.05 # adjust by % of avg velo

    avgDX = 0
    avgDY = 0
    numNeighbors = 0

    for i in range(numBoids):
        if distance(boidNum, i) < visualRange:
            avgDX += boids[i].dx
            avgDY += boids[i].dy
            numNeighbors += 1

    if numNeighbors != 0:
        avgDX = avgDX / numNeighbors
        avgDY = avgDY / numNeighbors

        boids[boidNum].dx += (avgDX - boids[boidNum].dx) * matchingFactor
        boids[boidNum].dy += (avgDY - boids[boidNum].dy) * matchingFactor

def speedLimit (boidNum):
    speedLimit = 15
    speed = sqrt((boids[boidNum].dx)**2 + (boids[boidNum].dy)**2)

    if speed > speedLimit:
        (boids[boidNum].dx) = (boids[boidNum].dx / speed) * speedLimit
        (boids[boidNum].dy) = (boids[boidNum].dy / speed) * speedLimit






#screen = pygame.display.set_mode([width, height])

initPositions()
print(nClosest(0,2))
