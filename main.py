import pygame
from pygame.color import THECOLORS
import sys
import asyncio
from random import randint
pygame.init()
screen = pygame.display.set_mode((1000,700))
screen.fill(THECOLORS['white'])
lifecells = []
class Cell:
    def __init__(self, x, y):
        self.x = x*25
        self.y = y*25
        self.cell = pygame.Rect(self.x, self.y, 25, 25)
        pygame.draw.rect(screen, (192,192,192), self.cell, width=1)
    def lifecell(x,y):
        cell = pygame.Rect(x, y, 25, 25)
        pygame.draw.rect(screen, (0,255,0), cell)
        return cell
    def allcells():
        allcells = []
        for x in range(40):
            for y in range(28):
                cell = pygame.Rect(x*25,y*25,25,25)
                allcells.append(cell)
        return allcells 
    def diecell(x,y):
        cell =pygame.Rect(x,y,25,25)
        pygame.draw.rect(screen, (192,192,192), cell, width=1)
        return cell

async def Draw():
    for x in range(40):
        for y in range(28):
            Cell(x,y)
            pygame.display.flip()

    for randcell in range(100):
        x = randint(0,40)*25
        y = randint(0,28)*25
        lifecell = Cell.lifecell(x,y)
        lifecells.append(lifecell)
    pygame.display.flip()

    
async def game_of_life():
    while True:
        a = 0
        a+=1
        x = 0
        y = 0
        neighbours = 0
        
        allcells = Cell.allcells()
        for cell in allcells:
            conditions = [pygame.Rect(x+25,y,25,25),pygame.Rect(x-25,y,25,25),pygame.Rect(x,y+25,25,25), pygame.Rect(x,y-25,25,25),
                    pygame.Rect(x+25,y+25,25,25),pygame.Rect(x-25,y-25,25,25),pygame.Rect(x-25,y+25,25,25),pygame.Rect(x+25,y-25,25,25)]
            x = cell.x
            y = cell.y
            rect = pygame.Rect(x,y,25,25)
            pygame.draw.rect(screen,(255,0,0),rect, width=1)
            pygame.display.flip()
            for condition in conditions:
                x = cell.x
                y = cell.y
                pygame.draw.rect(screen,(0,0,255), condition, width=1)
                pygame.display.flip()
                for lifecell in lifecells:
                    if condition.colliderect(lifecell.x, lifecell.y, 25,25):
                        neighbours+=1
                    else:
                        pass
                    if neighbours == 2 or neighbours == 3: 
                        print(neighbours)
                        lifecells.append(Cell.lifecell(x,y))
                    else:
                        try:
                            lifecells.remove(pygame.Rect(x,y,25,25))
                        except:
                            pass
                        Cell.diecell(x,y)
                    pygame.display.flip()
                                    
async def checkQUIT():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        await asyncio.sleep(0.01)
async def main():
    await asyncio.gather(Draw(), checkQUIT(), game_of_life())
asyncio.run(main())