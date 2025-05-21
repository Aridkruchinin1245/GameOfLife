import pygame
from pygame.color import THECOLORS
import sys
import asyncio
from random import randint

a = -25
b = -25
pygame.init()
screen = pygame.display.set_mode((1000,700))
screen.fill(THECOLORS['white'])
pygame.display.flip()

class Cell:
    # def CheckCells(cell):
    #     rectangles = [pygame.Rect(cell.x+25,cell.y,25,25),pygame.Rect(cell.x-25,cell.y,25,25),pygame.Rect(cell.x,cell.y+25,25,25), pygame.Rect(cell.x,cell.y-25,25,25),
    #                    pygame.Rect(cell.x+25,cell.y+25,25,25),pygame.Rect(cell.x-25,cell.y-25,25,25),pygame.Rect(cell.x-25,cell.y+25,25,25),pygame.Rect(cell.x+25,cell.y-25,25,25)]
    #     for i in rectangles:
    #         pygame.draw.rect(screen, (192,192,192), i, width=1)
        
    def CheckCells(cell):
        x = 0
        y = 0
        neighbours = 0
        rectangles = []
        conditions = [pygame.Rect(x+25,y,25,25),pygame.Rect(x-25,y,25,25),pygame.Rect(x,y+25,25,25), pygame.Rect(x,y-25,25,25),
                       pygame.Rect(x+25,y+25,25,25),pygame.Rect(x-25,y-25,25,25),pygame.Rect(x-25,y+25,25,25),pygame.Rect(x+25,y-25,25,25)]
        for x in range(40):
            for y in range(28):
                rect = pygame.Rect(x*25,y*25,25,25)
                rectangles.append(rect)
        for i in rectangles:
            pygame.draw.rect(screen, (192,192,192), i, width=1)
            for a in conditions: 
                if a.colliderect(cell.x, cell.y, 25,25):
                    neighbours+=1
            if neighbours>0:
                print(neighbours)
                neighbours = 0

        
    def __init__(self,x,y):
        self.x = x*25
        self.y = y*25
        self.Xcenter = self.x + 12.5
        self.Ycenter = self.y + 12.5
        self.r = pygame.Rect(self.x, self.y, 25, 25)
        self.center = pygame.Rect(self.Xcenter-5, self.Ycenter-5, 10, 10)
        pygame.draw.rect(screen, (0,255,0), self.r)
        pygame.draw.rect(screen, (0,0,0), self.center)
    
async def Draw():
    cells = []
    for i in range(1000):
        cell = Cell(randint(0,40), randint(0,28))
        cells.append(cell)
    for i in cells:
        # print(i.x, i.y)
        Cell.CheckCells(i)
        
    pygame.display.update()
async def checkQUIT():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        await asyncio.sleep(0.01)
async def main():
    await asyncio.gather(Draw(), checkQUIT())
asyncio.run(main())