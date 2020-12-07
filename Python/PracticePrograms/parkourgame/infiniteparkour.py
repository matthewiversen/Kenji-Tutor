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




def imageload(x,y,cloudtype):
    screen.blit(cloudtype,(x,y))
    

def moveingplatforms(platformx, platformspeed):
    platformx += platformspeed
    return platformx

# imageload(-70,1,cloud1)
# imageload(350,100,cloud2)
# imageload(50,600,cloud3)

while not done:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # imageload(-70,1,cloud1)
        # imageload(350,100,cloud2)
        # imageload(50,600,cloud3)
    x1 = moveingplatforms(x1, 5)
    screen.fill((0,255,255))
    pygame.draw.rect(screen, (246,215,21), (x1,y1,width,height))
        # # x2 = moveingplatforms(x2, 1)
        # # x3 = moveingplatforms(x3, 1)
        # # x4 = moveingplatforms(x4, 1)
        # # x5 = moveingplatforms(x5, 1)

    pygame.display.flip()


# platform1 = pygame.transform.scale(platform1,(150,150))
# platform2 = pygame.image.load('parkourgameplatform.png').convert()
# platform2 = pygame.transform.scale(platform2,(150,150))
# platform3 = pygame.image.load('parkourgameplatform.png').convert()
# platform3 = pygame.transform.scale(platform3,(150,150))
# platform4 = pygame.image.load('parkourgameplatform.png').convert()
# platform4 = pygame.transform.scale(platform4,(150,150))
# platform5 = pygame.image.load('parkourgameplatform.png').convert()
# platform5 = pygame.transform.scale(platform5,(150,150))


