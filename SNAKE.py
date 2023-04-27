#SNAKE
#May 11th, 2016
#Aman Braich
import pygame
import sys
import random

pygame.init()

screenSize = (800,600)
displayScreen = pygame.display.set_mode((screenSize),0)

pygame.display.set_caption("Snake")
#Colors
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
ORANGE = (255,165,0)

displayScreen.fill(BLACK)
pygame.display.update()
#Fonts
fontScore = pygame.font.SysFont("Arial", 50)
fontTitle = pygame.font.SysFont("comicsans", 100)
fontSub = pygame.font.SysFont("comicsans", 48)

#Variables
game = False
main = False
gameover = True
x = 400
y = 300
dx = 0
dy = 0
oldx = 0
oldy = 0
score = 0
r = 10
direction = 0
#Main Loop
while not main:
    while not game:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                game = True
                main = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    direction = "left"
                    dx = -2
                    dy = 0
                elif event.key == pygame.K_d:
                    direction = "right"
                    dx = 2
                    dy = 0
                elif event.key == pygame.K_w:
                    direction = "up"
                    dy = -2
                    dx = 0
                elif event.key == pygame.K_s:
                    direction = "down"
                    dy = 2
                    dx = 0

        #OLD AND NEW SNAKE POSTIONS
        oldx = x
        oldy = y
        x = x + dx
        y = y + dy
        #SCORE UPDATE
        if direction == "up" or direction == "left" or direction == "right" or direction == "down":
            score += 1
        #DRAWS SCORE
        pygame.draw.rect(displayScreen, BLACK, (0, 0, 600, 49), 0)
        gamescore = fontScore.render(str(score), True, WHITE)
        displayScreen.blit(gamescore, (0,0))
        #CHECKS IF IT HITS WINDOW BORDERS IF SO ENDEDS GAME
        if direction == "up":
            if displayScreen.get_at((x, y-r)) == WHITE:
                game = True
                gameover = False
        if direction == "down":
            if displayScreen.get_at((x, y+r)) == WHITE:
                game = True
                gameover = False
        if direction == "left":
            if displayScreen.get_at((x-r, y)) == WHITE:
                game = True
                gameover = False
        if direction == "right":
            if displayScreen.get_at((x+r, y)) == WHITE:
                game = True
                gameover = False
        

        if (x>=(790-(r+1)) or x<(10+(r+1))):
            game = True
            gameover = False
        if (y<=(50+(r+1)) or y>=(600-(r+1))):
            game = True
            gameover = False

        #DRAWS GAME LINES AND SNAKE
        pygame.draw.circle(displayScreen, WHITE,(x,y), r, 0)
        pygame.draw.line(displayScreen, WHITE, (0,50), (800,50), 1)
        pygame.time.delay(15)
        pygame.display.update()
            
    while not gameover:
        
        displayScreen.fill(BLACK)
        #TEXT INPUT 
        GAMEOVER = fontTitle.render("Game Over", True, WHITE)
        scoretitle = fontSub.render("Your Final Score is:", True, WHITE)
        Exit = fontSub.render("Press Q to exit", True, WHITE)
        REPLAY = fontSub.render("Press R to Replay", True, WHITE)
        finalscore = fontSub.render(str(score), True, WHITE)
        #PLACEMENT OF TEXT
        displayScreen.blit(GAMEOVER,(60, 125))
        displayScreen.blit(scoretitle,(60,275))
        displayScreen.blit(finalscore, (575, 275))
        displayScreen.blit(Exit,(60,350))
        displayScreen.blit(REPLAY,(60,450))
        #SCREEN UPDATE 
        pygame.display.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = True
                gameover = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameover = True
                    main = True
                if event.key == pygame.K_r:
                    score = 0
                    main = False
                    game = False
                    gameover = True
                    displayScreen.fill(BLACK)
                    
        




pygame.quit()
sys.exit()

