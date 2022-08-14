import pygame 
import numpy as np
from xadrez.pecas import Pecas

pygame.init()
display = pygame.display.set_mode([640, 640])
pygame.display.set_caption("Xadrez")

load_bg = pygame.image.load("xadrez/tabuleiro.jpg")
bg = pygame.transform.scale(load_bg,[640,640]) 
gameLoop = True

t1 = Pecas("torre","branca",[1,1])
c1 = Pecas("cavalo","branca",[1,2])
b1 = Pecas("bispo","branca",[1,3])
k1 = Pecas("rei","branca",[1,4])
q1 = Pecas("rainha","branca",[1,5])
b2 = Pecas("bispo","branca",[1,6])
c2 = Pecas("cavalo","branca",[1,7])
t2 = Pecas("torre","branca",[1,8])

t3 = Pecas("torre","preta",[1,1])
c3 = Pecas("cavalo","preta",[1,2])
b3 = Pecas("bispo","preta",[1,3])
k2 = Pecas("rei","preta",[1,4])
q2 = Pecas("rainha","preta",[1,5])
b4 = Pecas("bispo","preta",[1,6])
c4 = Pecas("cavalo","preta",[1,7])
t4 = Pecas("torre","preta",[1,8])

p = []
for i in range(1,17):
    if i < 9:
        p.append(Pecas("peao","branca",[2,i]))
    else:
        p.append(Pecas("peao","preta",[7,i]))

(p1,p2,p3,p4,p5,p6,p7,p8,
p9,p10,p11,p12,p13,p14,p15,p16) = p.copy()


tabuleiro = [[t3,c3,b3,k2,q2,b4,c4,t4],
            [p9,p10,p10,p11,p12,p13,p14,p15,p16],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [p1,p2,p3,p4,p5,p6,p7,p8],
            [t1,c1,b1,k1,q1,b2,c2,t2]
            ]


while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False

    display.blit(bg,(0,0))
    pygame.display.update()

