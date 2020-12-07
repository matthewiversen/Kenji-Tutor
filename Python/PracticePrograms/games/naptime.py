#spleef hitball
#hitballs get bigger

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("meow")

A = random.randrange(0, 1140)
B = -30
C = random.randrange(0, 1140)
D = -90
E = random.randrange(0, 1140)
F = -30
# G = random.randrange(0, 1140, 30)
# H = random.randrange(0, 1140, 30)
# I = random.randrange(0, 1140, 30)
# J = random.randrange(0, 1140, 30)
# K = random.randrange(0, 1140, 30)
# L = random.randrange(0, 1140, 30)
# M = random.randrange(0, 1140, 30)
# N = random.randrange(0, 1140, 30)
green = (0,255,0) 
blue =  (0,0,255) 
red =  (255,0,0) 







# text = font.render('Hits', True,(0,100,100) , (255,0 ,0))
Bottom = 0
Bottom2 = 0
X = 570
Y = 1170
Width = 30
Height = 30
Speed = 8
matthew_exists = True
WHY = 1.0

# def LOSE():
#     screen.fill((0,0,0))
#     font = pygame.font.SysFont('comicsans', 100, False, False)
#     text = font.render('YOU LOSE! Score: ' + str(Bottom2), 1, green)
#     screen.blit(text, (400,50))
#     pygame.time.delay(1000)
#     pygame.quit()

def if_hit(playerX:int, playerY:int, dodgeballX:int, dodgeballY:int) -> (None):
    if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Score()
    
    if playerX+30 >= dodgeballX and playerX+30 <= dodgeballX+30 and playerY <= dodgeballY and playerY >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Score()
    

    if playerX >= dodgeballX and playerX <= dodgeballX+30 and playerY-30 <= dodgeballY and playerY-30 >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Score()
    

    if playerX+30 >= dodgeballX and playerX+30 <= dodgeballX+30 and playerY-30 <= dodgeballY and playerY-30 >= dodgeballY-30:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Score()

    return dodgeballX, dodgeballY

def if_hit_bottom(dodgeballX:int, dodgeballY:int) -> (None):
    if dodgeballY >= 1200:
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Num_of_hit_bottom()
        
    return dodgeballX, dodgeballY



def Speedy() -> (None):
    global WHY
    WHY += 0.03

def Score() ->(None):
    global Bottom2
    Bottom2 += 1
    Speedy()

def Num_of_hit_bottom() -> (None):
    global Bottom
    Bottom += 1
    Speedy()

def move(dodgeballspeed:int) -> (int):
    dodgeballspeed += WHY

    return dodgeballspeed

while matthew_exists:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    A,B  = if_hit(X,Y,A,B)
    C,D  = if_hit(X,Y,C,D)
    E,F  = if_hit(X,Y,E,F)
    A,B = if_hit_bottom(A,B)
    C,D = if_hit_bottom(C,D)
    E,F = if_hit_bottom(E,F)
    B = move(B)
    D = move(D)
    F = move(F)




    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and 599 <= Y:
        Y -= Speed
    if keys[pygame.K_DOWN] and Y <= 1200 - Speed - Height:
        Y += Speed
    if keys[pygame.K_LEFT] and X >= Speed:
        X -= Speed
    if keys[pygame.K_RIGHT] and X <= 1200 - Speed - Width:
        X += Speed

    screen.fill((0, 0, 0))    

    font = pygame.font.SysFont('comicsans', 100, False, False)
    text = font.render('Score: ' + str(Bottom2), 1, green)
    screen.blit(text, (400,50))

    text2 = font.render('Misses: ' + str(Bottom), 1, green)
    screen.blit(text2, (400,100))



    pygame.draw.rect(screen, (255,255,255), (0, 570, 1200, Height))
    pygame.draw.rect(screen, (0,255,0), (X, Y, Width, Height))
    pygame.draw.rect(screen, (255,0,0), (int(A), int(B), Width, Height))
    pygame.draw.rect(screen, (0,225,255), (int(C), int(D), Width, Height))
    pygame.draw.rect(screen, (255,0, 98), (int(E), int(F), Width, Height))
    # pygame.draw.rect(screen, (255,247,0), (G, H, Width, Height))
    # pygame.draw.rect(screen, (255,0, 255), (I, J, Width, Height))
    # pygame.draw.rect(screen, (0,255,0), (K, L, Width, Height))
    # pygame.draw.rect(screen, (0,255,0), (M, N, Width, Height))

    pygame.display.update()
    
    if Bottom == 3:
        break