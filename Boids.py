import pygame
import random
import math
from copy import deepcopy
from operator import attrgetter

pygame.init()

width = 800
height = 800
numBoids = 100

visualRange = 30
boids = []

class Boid:
    def __init__(self, number):
        self.number = number
        self.x = random.randint(-width-100, width+100)
        self.y = random.randint(-height-100, height+100)
        self.dx = (random.random() * 10) - 5
        self.dy = (random.random() * 10) - 5
        self.history = []
        self.distanceFrom = 0
        self.color = randomColor()

    def coords(self):
        return (self.x, self.y)

def initPositions ():
    for i in range(numBoids):
        boids.append(Boid(i))

def distance (boidA, boidB):
    return math.sqrt(((boidA.x - boidB.x)**2) + ((boidA.y - boidB.y)**2))

def nClosest (currBoid, n):
    for boid in boids:
        boid.distanceFrom = distance(currBoid, boid)
    closest = sorted(boids, key=lambda allBoid: allBoid.distanceFrom)
    return closest[1:n+1]

def keepWithinBounds (currBoid):
    margin = width-25
    turnFactor = 2

    if currBoid.x < margin:
        currBoid.dx += turnFactor

    if currBoid.x > width-margin:
        currBoid.dx -= turnFactor

    if currBoid.y < margin:
      currBoid.dy += turnFactor

    if currBoid.y > height - margin:
      currBoid.dy -= turnFactor


def flyToCenter (currBoid):
    centeringFactor = 0.005 # Adjust velo here
    centerX = 0
    centerY = 0
    numNeighbors = 0

    for boid in boids:
        if boid != currBoid:
            if distance(currBoid, boid) < visualRange:
                centerX += boid.x
                centerY += boid.y
                numNeighbors += 1

    if numNeighbors != 0:
        centerX = centerX / numNeighbors
        centerY = centerY / numNeighbors

        currBoid.dx += (centerX - currBoid.x) * centeringFactor
        currBoid.dy += (centerY - currBoid.y) * centeringFactor

def avoidOthers (currBoid):
    minDistance = 20
    avoidFactor = 0.05 # Adjust velo here
    moveX = 0
    moveY = 0

    for boid in boids:
        if boid != currBoid:
            if distance(currBoid, boid) < minDistance:
                moveX += currBoid.x - boid.x
                moveY += currBoid.y - boid.y

    currBoid.dx += moveX * avoidFactor
    currBoid.dy += moveY * avoidFactor

def matchVelocity (currBoid):
    matchingFactor = 0.05 # adjust by % of avg velo

    avgDX = 0
    avgDY = 0
    numNeighbors = 0

    for boid in boids:
        if distance(currBoid, boid) < visualRange:
            avgDX += boid.dx
            avgDY += boid.dy
            numNeighbors += 1

    if numNeighbors != 0:
        avgDX = avgDX / numNeighbors
        avgDY = avgDY / numNeighbors

        currBoid.dx += (avgDX - currBoid.dx) * matchingFactor
        currBoid.dy += (avgDY - currBoid.dy) * matchingFactor

def speedLimit (currBoid):
    speedLimit = 10
    speed = math.sqrt((currBoid.dx)**2 + (currBoid.dy)**2)

    if speed > speedLimit:
        (currBoid.dx) = (currBoid.dx / speed) * speedLimit
        (currBoid.dy) = (currBoid.dy / speed) * speedLimit

def randomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

screen = pygame.display.set_mode([width, height])


initPositions()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for boid in boids:
        flyToCenter(boid)
        avoidOthers(boid)
        matchVelocity(boid)
        speedLimit(boid)
        keepWithinBounds(boid)

        boid.x += boid.dx
        boid.y += boid.dy
        boid.history.append([boid.x, boid.y])
        boid.history = boid.history[-50:]

        pygame.draw.circle(screen, boid.color, boid.coords(), 3)

    pygame.display.update()


    pygame.display.flip()


pygame.quit()
