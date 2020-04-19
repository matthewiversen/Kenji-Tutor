import pygame
import random

pygame.init()

screen = pygame.display.set_mode((250, 250))

pygame.display.set_caption("meow")

X = 50
Y = 60
Width = 60
Height = 60
Speed = 5
matthew_exists = True

while matthew_exists:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            matthew_exists = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Y -= Speed
    if keys[pygame.K_DOWN]:
        Y += Speed
    if keys[pygame.K_LEFT]:
        X -= Speed
    if keys[pygame.K_RIGHT]:
        X += Speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255 , 255 , 0), (X, Y, Width, Height))
    pygame.display.update()











































































pygame.quit()