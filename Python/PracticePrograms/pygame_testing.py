import pygame

def start_game():
    pygame.init()

    X = 400
    Y = 400
    white = (255, 255, 255) 
    # green = (0, 255, 0) 
    # blue = (255, 0,0) 
    done = False
    screen = pygame.display.set_mode((X, Y))

    while not done:
        screen.fill(white) 
        # screen.blit(text, textRect) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(30, 30, 60, 60))
            
            pygame.display.flip()






# font = pygame.font.Font('freesansbold.ttf', 32) 
# text = font.render('good job today', True, blue, green)
# textRect = text.get_rect()  
# textRect.center = (X - 125 , Y - 50) 

def main():
    start_game()

main()