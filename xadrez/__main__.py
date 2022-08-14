import pygame 
import numpy as np
from xadrez.pecas import Pecas

pygame.init()
display = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Xadrez")

load_bg = pygame.image.load("xadrez/tabuleiro.jpg")
bg = pygame.transform.scale(load_bg,[640,640]) 
gameLoop = True



tabuleiro = 
    [
        [torre("preta",1,[1,8]),cavalo("preta",1,[2,8]),bispo("preta",1,[3,8]),rei("preta",[4,8]),rainha("preta",[5,8]),bispo("preta",2,[6,8]), cavalo("preta",2,[7,8]),torre("preta",2,[8,8])],
        [peao("preta",1,[1,7]),peao("preta",2,[2,7]),peao("preta",3,[3,7]),peao("preta",4,[4,7]),peao("preta",5,[5,7]),peao("preta",6,[6,7]),peao("preta",7,[7,7]),peao("preta",8,[8,7])],
        [nula([1,6]),nula([2,6]),nula([3,6]),nula([4,6]),nula([5,6]),nula([6,6]),nula([7,6]),nula([8,6])],
        [nula([1,5]),nula([2,5]),nula([3,5]),nula([4,5]),nula([5,5]),nula([6,5]),nula([7,5]),nula([8,5])],
        [nula([1,4]),nula([2,4]),nula([3,4]),nula([4,4]),nula([5,4]),nula([6,4]),nula([7,4]),nula([8,4])],
        [nula([1,3]),nula([2,3]),nula([3,3]),nula([4,3]),nula([5,3]),nula([6,3]),nula([7,3]),nula([8,3])]     
        [peao("branca",1,[1,2]),peao("branca",2,[2,2]),peao("branca",3,[3,2]),peao("branca",4,[4,2]),peao("branca",5,[5,2]),peao("branca",6,[6,2]),peao("branca",7,[7,2]),peao("branca",8,[8,2])],
        [torre("branca",1,[1,1]),cavalo("branca",1,[2,1]),bispo("branca",1,[3,1]),rei("branca",[4,1]),rainha("branca",[5,1]),bispo("branca",2,[6,1]), cavalo("branca",2,[7,1]),torre("branca",2,[8,1])],
    ]




while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    display.blit(bg,(0,0))
    pygame.display.update()

