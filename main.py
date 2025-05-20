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
    def __init__(self,x,y):
            self.x = x*25
            self.y = y*25
            self.r = pygame.Rect(self.x,self.y,25,25)
            pygame.draw.rect(screen, (0,255,0), self.r)
            pygame.display.flip()
    def CheckCells(self):
        conditions = [[self.x+10, self.y+10], [self.x, self.y+10]]
        nearly = 0
        for i in range(8):
            if pygame.Rect.collidepoint(conditions[i]) == True:
                nearly+=1
                print(f'колво клеток hzlkv {nearly}')
        return nearly


            




async def Draw():
    cells=[]
    for i in range(1000):
        one = Cell(randint(0,40), randint(0,28)).r
        Cell.CheckCells
        cells.append(one)
        if pygame.Rect.colliderect(one, cells[i]):
            one
        else:
           one = Cell(randint(0,40), randint(0,28)).r 
           i-=1
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