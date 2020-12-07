#spleef hitball
#hitballs get bigger(done)
#blocks dont spawn at very right(fixed)
#if you move you die(bad idea)
#pygame.image.load is lagging game
#add background
#add random background everytime it runs
#add power ups(spped,invincibility)

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1200, 1200))
pygame.display.set_caption("meow")

A = random.randrange(0, 1170)
B = -30
Width1 = 30
Height1 = 30
HIT_BOX1 = 30
C = random.randrange(0, 1200)
D = -240
Width2 = 30
Height2 = 30
HIT_BOX2 = 30
E = random.randrange(0, 1200)
F = -450
Width3 = 30
Height3 = 30
HIT_BOX3 = 30
G = random.randrange(0,1200)
H = -650
Width4 = 30
Height4 = 30
HIT_BOX4 = 30
I = random.randrange(0,1200)
J = -860
Width5 = 30
Height5 = 30
HIT_BOX5 = 30
K = random.randrange(0,1200)
L = -1070
Width6 = 30
Height6 = 30
HIT_BOX6 = 30
M = random.randrange(0,1200)
N = -128
Width7 = 30
Height7 = 30
HIT_BOX7 = 30

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
HIT = 0
dodge = 0
X = 570
Y = 1170
Width = 30
Height = 30
Speed = 8
matthew_exists = True
WHY = 2.0
ghostdude = pygame.image.load('photos/matthews afterlife.png').convert_alpha()
ghostdude = pygame.transform.scale(ghostdude, (28, 37))
dodgball = pygame.image.load('photos/dodgball jpeg.png').convert_alpha()
direction = True


# def LOSE():
#     screen.fill((0,0,0))
#     font = pygame.font.SysFont('comicsans', 100, False, False)
#     text = font.render('YOU LOSE! dodge: ' + str(Dodged), 1, green)
#     screen.blit(text, (400,50))
#     pygame.time.delay(1000)
#     pygame.quit()


def if_hit(playerX:int, playerY:int, dodgeballX:int, dodgeballY:int, HIT_BOX:int) -> (None):

    if playerX  >= dodgeballX and playerX  <= dodgeballX+HIT_BOX:
        if playerY >= dodgeballY and playerY <= dodgeballY+HIT_BOX:
            Dodge()

        
    if playerX +30 >= dodgeballX and playerX  <= dodgeballX + HIT_BOX:
        if playerY >= dodgeballY and playerY <= dodgeballY + HIT_BOX:
            Dodge()


    if playerX  >= dodgeballX and playerX  <= dodgeballX + HIT_BOX:
        if playerY + 30 >= dodgeballY and playerY + 30 <= dodgeballY + HIT_BOX:
            Dodge()


    if playerX  + 30 >= dodgeballX and playerX  + 30 <= dodgeballX + HIT_BOX:
        if playerY+30 >= dodgeballY and playerY + 30 <= dodgeballY + HIT_BOX:
            Dodge()



    return dodgeballX, dodgeballY


def if_hit_bottom(dodgeballX:int, dodgeballY:int, Width_of_dodgeball:int, Height_of_dodgeball:int, HIT_BOX:int) -> (tuple):
    if dodgeballY >= 1200:
        global dodgball
        dodgeballX = random.randrange(0, 1140, 30)
        dodgeballY = random.randrange(-120, -60, 1)
        Num_of_hit_bottom()
        dodgballscale()
        dodgball = pygame.transform.scale(dodgball,(Width1, Height1))
        
        HIT_BOX = random.randrange(30, 120, 1)
        Width_of_dodgeball, Height_of_dodgeball = set_size(Width_of_dodgeball, Height_of_dodgeball, HIT_BOX)



    return dodgeballX, dodgeballY, Width_of_dodgeball, Height_of_dodgeball, HIT_BOX


def Speedy() -> (None):
    global WHY
    WHY += 0.03


def Dodge() ->(None):
    global HIT
    HIT += 1
    Speedy()

def Num_of_hit_bottom() -> (None):
    global dodge
    dodge += 1
    Speedy()



def move(dodgeballspeed:int) -> (int):
    dodgeballspeed += WHY

    return dodgeballspeed


def set_size(Width_of_dodgeball:int, Height_of_dodgeball:int, HIT_BOX:int) -> (tuple):

    Width_of_dodgeball = HIT_BOX
    Height_of_dodgeball = HIT_BOX

    return Width_of_dodgeball, Height_of_dodgeball

def flipimagetoside():
    ghostdude = pygame.transform.flip(ghostdude, True, False)

def dodgballscale():
    dodgball = pygame.image.load('photos/dodgball jpeg.png').convert_alpha()
    dodgball = pygame.transform.scale(dodgball,(Width1, Height1))



while matthew_exists:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    A, B  = if_hit(X, Y, A, B, HIT_BOX1)
    C, D  = if_hit(X, Y, C, D, HIT_BOX2)
    E, F  = if_hit(X, Y, E, F, HIT_BOX3)
    G, H  = if_hit(X, Y, G, H, HIT_BOX4)
    I, J  = if_hit(X, Y, I, J, HIT_BOX5)
    K, L  = if_hit(X, Y, K, L, HIT_BOX6)
    M, N  = if_hit(X, Y, M, N, HIT_BOX7)
    A, B, Width1, Height1, HIT_BOX1 = if_hit_bottom(A, B, Width1, Height1, HIT_BOX1)
    C, D, Width2, Height2, HIT_BOX2 = if_hit_bottom(C, D, Width2, Height2, HIT_BOX2)
    E, F, Width3, Height3, HIT_BOX3 = if_hit_bottom(E, F, Width3, Height3, HIT_BOX3)
    G, H, Width4, Height4, HIT_BOX4 = if_hit_bottom(G, H, Width4, Height4, HIT_BOX4)
    I, J, Width5, Height5, HIT_BOX5 = if_hit_bottom(I, J, Width5, Height5, HIT_BOX5)
    K, L, Width6, Height6, HIT_BOX6 = if_hit_bottom(K, L, Width6, Height6, HIT_BOX6)
    M, N, Width7, Height7, HIT_BOX7 = if_hit_bottom(M, N, Width7, Height7, HIT_BOX7)
    B = move(B)
    D = move(D)
    F = move(F)
    H = move(H)
    J = move(J)
    L = move(L)
    N = move(N)




    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and 599 <= Y:
        Y -= Speed
    if keys[pygame.K_DOWN] and Y <= 1200 - Speed - Height:
        Y += Speed
    if keys[pygame.K_LEFT] and X >= Speed:
        X -= Speed
        direction = False
    if keys[pygame.K_RIGHT] and X <= 1200 - Speed - Width:
        X += Speed
        direction = True
        




    screen.fill((0, 0, 0))    



    font = pygame.font.SysFont('arialblack', 100, False, False)
    text = font.render('HIT: ' + str(HIT), 1, green)
    screen.blit(text, (400,50))

    text2 = font.render('DODGED: ' + str(dodge), 1, green)
    screen.blit(text2, (400,125))




    # pygame.draw.rect(screen, (255,255,255), (0, 570, 1200, 30))
    # pygame.draw.rect(screen, (255,0,0), (int(A), int(B), Width1, Height1))
    # dodgball = pygame.image.load('photos/dodgball jpeg.png').convert_alpha()
    # screen.blit(dodgball, (int(A), int(B)))
    pygame.draw.rect(screen, (0,225,255), (int(C), int(D), Width2, Height2))
    pygame.draw.rect(screen, (255,0,98), (int(E), int(F), Width3, Height3))
    pygame.draw.rect(screen, (255,247,0), (int(G),int(H), Width4, Height4))
    pygame.draw.rect(screen, (255,100,255), (int(I), int(J), Width5, Height5))
    pygame.draw.rect(screen, (48,2,0), (int(K), int(L), Width6, Height6))
    pygame.draw.rect(screen, (0,5,48), (int(M),int(N), Width7, Height7))

    screen.blit(ghostdude, (X,Y))
#GRAY SQUARE AT TOP LEFT CORNER
    # pygame.draw.rect(screen, (100,100,100), (int(A), int(B), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(C), int(D), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(E), int(F), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(G), int(H), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(I), int(J), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(K), int(L), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (int(M), int(N), 5, 5))
    # pygame.draw.rect(screen, (100,100,100), (X , Y, 5, 5))
    

    pygame.display.update()

    if HIT > 0:
        print('You dodged', dodge, 'dodgeballs!')
        break