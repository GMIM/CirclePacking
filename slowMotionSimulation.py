from random import *
from math import hypot
from math import *
import pygame, sys, pygame.locals
# this function will return 0 if the value is not decreased and if the current result was less than the previous
# result it will return 1
def evaluate(current, previous):
    if current >= previous:
        return 0
    else:
        return 1


# circle overlapping detection
def overlapped(x1, y1, x2, y2, r1, r2):
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
    radSumSq = (r1 + r2) * (r1 + r2);
    if (distSq == radSumSq):
        return 1
    elif (distSq > radSumSq):
        return -1
    else:
        return 0


# this class is used to jold data about the circle to have it is radius weight and index
class Circle:
    Radius = 0.0
    Index = 0.0
    Weight = 0.0
    connectedTo = []
    x = 0.0
    y = 0.0
    color = (0, 0, 0)

    def __init__(self):
        self.Index = 0.0
        self.Radius = 0.0
        self.Weight = 0.0
        self.x = 0.0
        self.color = (0, 0, 0)

    def setWeight(self, w):
        self.Weight = w

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def setIndex(self, i):
        self.Index = i

    def setRadius(self, r):
        self.Radius = r

    def __repr__(self):
        return str(self.__dict__)

    def addConnetedTo(self, connectedCircle):
        self.connectedTo.append(connectedCircle)

    def getConnections(self):
        return self.connectedTo

    def getx(self):
        return self.x

    def gety(self):
        return self.y


BLACK = (0, 0, 0)
OTHER = (12, 123, 3)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
colors = [BLACK, OTHER, BLUE, GREEN, RED]
circlesList = []
randomizedCircleList = []
minAreaRecoded = 0;
overAllMinDist=-1
numberOfCircles = int(input("Please enter the number of circles "))
radii = [int(x) for x in input("Please enter the radii of each of them: ").split()]
for i in range(numberOfCircles):
    c = Circle()
    cc = Circle()
    c.setIndex(i)
    cc.setIndex(i)
    c.setRadius(radii.__getitem__(i))
    cc.setRadius(radii.__getitem__(i))
    colorr = colors[randint(0, 4)]
    c.color = colorr
    circlesList.append(c)
    cc.color = colorr
    cc.x = randint(100, 1100)
    cc.y = randint(100, 700)
    randomizedCircleList.append(cc)
print(circlesList)

# Agent creating the initial state.
def overLappedForALL():
    overlapping = 0
    for i in range(0,numberOfCircles):
        for j in range(0,numberOfCircles):
            if i!=j:
                x1=randomizedCircleList.__getitem__(i).x
                y1 = randomizedCircleList.__getitem__(i).y
                r1 = randomizedCircleList.__getitem__(i).Radius
                x2 = randomizedCircleList.__getitem__(j).x
                y2 = randomizedCircleList.__getitem__(j).y
                r2 = randomizedCircleList.__getitem__(j).Radius
                if overlapped(x1,y1,x2,y2,r1,r2)==0:
                    overlapping = 1
                    break
    return overlapping

def draw():
    for i in range(numberOfCircles):
        pygame.draw.circle(screen, randomizedCircleList.__getitem__(i).color,
                           [randomizedCircleList.__getitem__(i).x, randomizedCircleList.__getitem__(i).y],
                           randomizedCircleList.__getitem__(i).Radius)
        pygame.display.update()
        screen.unlock()
def calculateMaxDistance():
    maxDist = -1
    for i in range(0, numberOfCircles):
        for j in range(0, numberOfCircles):
            if i != j:
               curDist = sqrt((pow(randomizedCircleList.__getitem__(i).x-randomizedCircleList.__getitem__(j).x,2))+(pow(randomizedCircleList.__getitem__(i).y-randomizedCircleList.__getitem__(j).y,2)))
               if maxDist<curDist or maxDist ==-1:
                   maxDist=curDist

    return maxDist

for j in range(numberOfCircles):
    r2 = circlesList.__getitem__(j).Radius
    overlapping = 1
    while overlapping == 1:
        overlapping = 0
        x2 = randint(100, 1100)
        y2 = randint(100, 700)
        for i in range(0, j):
            x1 = circlesList.__getitem__(i).x
            y1 = circlesList.__getitem__(i).y
            r1 = circlesList.__getitem__(i).Radius
            if overlapped(x1, y1, x2, y2, r1, r2) == 0:
                overlapping = 1
                break
        if overlapping == 0:
            circlesList.__getitem__(j).x = x2
            circlesList.__getitem__(j).y = y2
            break
print(circlesList)
# drawing the list
import pygame

from random import *
import math
import pygame

pygame.init()
size = [1000, 600]
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("AI Circle Packing")
done = False
clock = pygame.time.Clock()
screen.fill(WHITE)
draw()
done = False
run = True
while run:
    # clock.tick(10)

    done = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False
    for i in range(0, numberOfCircles):
        while randomizedCircleList.__getitem__(i).x != circlesList.__getitem__(i).x:
            if randomizedCircleList.__getitem__(i).x < circlesList.__getitem__(i).x:
                randomizedCircleList.__getitem__(i).x += 1;
                done = False
                draw()
            else:
                randomizedCircleList.__getitem__(i).x -= 1;
                done = False
                draw()
        if not done:
            screen.fill(WHITE)
            draw()
    for i in range(0, numberOfCircles):
        while randomizedCircleList.__getitem__(i).y != circlesList.__getitem__(i).y:
            if randomizedCircleList.__getitem__(i).y < circlesList.__getitem__(i).y:
                randomizedCircleList.__getitem__(i).y += 1;
                done = False
                draw()
            else:
                randomizedCircleList.__getitem__(i).y -= 1;
                done = False
                draw()
        if not done:
            screen.fill(WHITE)
            draw()
    ref = 0;
    min = -1
    if done:
        screen.fill(WHITE)
        for k in range(0,numberOfCircles):
            cur = sqrt((pow(randomizedCircleList.__getitem__(k).x-500,2))+(pow(randomizedCircleList.__getitem__(k).y-300,2)))
            if cur<=min or min==-1:
                min = cur
                ref = k
        for k in range(0,numberOfCircles):
            if k != ref:
                x2 = randomizedCircleList.__getitem__(ref).x
                y2 = randomizedCircleList.__getitem__(ref).y
                r2 = randomizedCircleList.__getitem__(ref).Radius
                while True:
                    if randomizedCircleList.__getitem__(k).x>x2:
                        randomizedCircleList.__getitem__(k).x-=1
                        if overLappedForALL()==1:
                            randomizedCircleList.__getitem__(k).x +=1
                            break
                        draw()
                    elif randomizedCircleList.__getitem__(k).x==x2:
                        break
                    else:
                        if randomizedCircleList.__getitem__(k).x < x2:
                            randomizedCircleList.__getitem__(k).x += 1
                            if overLappedForALL() == 1:
                                randomizedCircleList.__getitem__(k).x -= 1
                                break
                            draw()
                screen.fill(WHITE)
                draw()
                while True:
                    if randomizedCircleList.__getitem__(k).y>y2:
                        randomizedCircleList.__getitem__(k).y-=1
                        if overLappedForALL()==1:
                            randomizedCircleList.__getitem__(k).y +=1
                            break
                        draw()
                    elif randomizedCircleList.__getitem__(k).y==y2:
                        break
                    else:
                        if randomizedCircleList.__getitem__(k).y < y2:
                            randomizedCircleList.__getitem__(k).y += 1
                            if overLappedForALL() == 1:
                                randomizedCircleList.__getitem__(k).y -= 1
                                break
                            draw()
                screen.fill(WHITE)
                draw()
                curOverAllMinDist=calculateMaxDistance()
                if curOverAllMinDist<overAllMinDist or overAllMinDist ==-1:
                    overAllMinDist = curOverAllMinDist
                print(overAllMinDist)
    pygame.time.Clock().tick(10)
    pygame.display.update()


print(overAllMinDist)