import pygame
import random

def start_game():
    pygame.init()

    X = 400
    Y = 400
    
    white = (255, 255, 255)
    green = (0, 255, 0) 
    blue = (255, 0,0)
    font = pygame.font.Font('freesansbold.ttf', 32) 
    text = font.render('input', True, blue, green)
    textRect = text.get_rect()  
    textRect.center = (X/2, Y/2)

    done = False
    screen = pygame.display.set_mode((X, Y))

    while not done:
        screen.fill(white) 
        screen.blit(text, textRect) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(30, 30, 60, 60))
            
            pygame.display.flip()



def inputs() -> (int, int, int):
    age = int(input("Age (1-100):   "))
    diet = int(input("Diet (0-10):   "))
    coding_skill = int(input("Coding skill:  "))
    return age,diet,coding_skill



# font = pygame.font.Font('freesansbold.ttf', 32) 
# text = font.render('good job today', True, blue, green)
 

def main():
    start_game()
    age,diet,coding_skill = inputs() 

main()
