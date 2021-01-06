# #https://www.bing.com/search?q=pygame+display+image&cvid=373d38b5ce2349928011b22d495e8576&pglt=547&FORM=ANNTA1&PC=NMTS&adlt=strict

import pygame
import random
pygame.init()


X=1000
Y=1000
x1 = 100
x2 = 200
x3 = 300
x4 = 400
x5 = 500
y1 = 100
y2 = 200
y3 = 300
y4 = 400
y5 = 500
width = 23
height = 123

done = False
screen = pygame.display.set_mode((X, Y))
cloud1 = pygame.image.load('cloud1.png')
cloud1 = pygame.transform.scale(cloud1,(450,450))
cloud2 = pygame.image.load('cloud2.png')
cloud2 = pygame.transform.scale(cloud2,(600,600))
cloud3 = pygame.image.load('cloud3.png')
cloud3 = pygame.transform.scale(cloud3,(600,600))
platform1 = pygame.image.load('parkourgameplatform.png')
platform1 = pygame.transform.scale(platform1,(150,150))
platform2 = pygame.image.load('parkourgameplatform.png')
platform2 = pygame.transform.scale(platform2,(150,150))
platform3 = pygame.image.load('parkourgameplatform.png')
platform3 = pygame.transform.scale(platform3,(150,150))
platform4 = pygame.image.load('parkourgameplatform.png')
platform4 = pygame.transform.scale(platform4,(150,150))
platform5 = pygame.image.load('parkourgameplatform.png')
platform5 = pygame.transform.scale(platform5,(150,150))



def imageload(x,y,cloudtype):
    screen.blit(cloudtype,(x,y))
    

def moveingplatforms(platformx, platformspeed):
    platformx += platformspeed
    return platformx

def offscreen(x1,x2,x3,x4,x5):
    if x1 >= 1000: 
        x1 = -150
    if x2 >= 1000: 
        x2 = -150
    if x3 >= 1000: 
        x3 = -150
    if x4 >= 1000: 
        x4 = -150
    if x5 >= 1000: 
        x5 = -150
    return x1,x2,x3,x4,x5

# imageload(-70,1,cloud1)
# imageload(350,100,cloud2)
# imageload(50,600,cloud3)

while not done:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    screen.fill((0,255,255))

    imageload(-70,1,cloud1)
    imageload(350,100,cloud2)
    imageload(50,600,cloud3)
    x1 = moveingplatforms(x1, 5)
    x2 = moveingplatforms(x2, 5)
    x3 = moveingplatforms(x3, 5)
    x4 = moveingplatforms(x4, 5)
    x5 = moveingplatforms(x5, 5)
    # pygame.draw.rect(screen, (246,215,21), (x1,y1,height,width))

    x1,x2,x3,x4,x5 = offscreen(x1,x2,x3,x4,x5)
    

    imageload(x1,100,platform1)
    imageload(x2,200,platform2)
    imageload(x3,300,platform3)
    imageload(x4,400,platform4)
    imageload(x5,500,platform5)
    
    pygame.display.flip()




