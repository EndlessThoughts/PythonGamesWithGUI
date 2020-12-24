import pygame, sys, random

def ballMovement():
    global bspeedx, bspeedy, opponentScore, playerScore, getReady
    ball.x += bspeedx
    ball.y += bspeedy
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        bspeedy *= -1
    if ball.left <= 0:
        playerScore += 1
        ballrestart()
        getReady = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opponentScore += 1
        ballrestart()
        getReady = pygame.time.get_ticks()
    if ball.colliderect(player) or ball.colliderect(opposition):
        bspeedx *= -1

def playerMovement():
    player.y += playerspeed
    
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def oppositionMovement():
    if opposition.top < ball.y:
        opposition.top += oppositionspeed
    if opposition.bottom > ball.y:
        opposition.bottom -= oppositionspeed
    if opposition.top <= 0:
        opposition.top = 0
    if opposition.bottom >= screen_height:
        opposition.bottom = screen_height

def ballrestart():
    global bspeedx, bspeedy, getReady
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2)
    
    if current_time - getReady < 2100:
        bspeedx, bspeedy = 0,0
    else:
        bspeedy = 7 * random.choice((1,-1))
        bspeedx = 7 * random.choice((1,-1))
        getReady = False

#General Setup
pygame.init()
clock = pygame.time.Clock()

#main window
screen_width = 1000
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opposition = pygame.Rect(10, screen_height/2 - 70,10,140)

bg_color = pygame.Color("grey12")
light_blue = (0,0,255)

bspeedx = 7 * random.choice((1,-1))
bspeedy = 7 * random.choice((1,-1))
playerspeed = 0
oppositionspeed = 7

playerName = "Player"
oppositionName = "Computer"
playerScore = 0
opponentScore = 0
gameFont = pygame.font.Font("freesansbold.ttf", 32)

getReady = True


while True:
    #For input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerspeed += 7
            if event.key == pygame.K_UP:
                playerspeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerspeed -= 7
            if event.key == pygame.K_UP:
                playerspeed += 7
                
    ballMovement()
    playerMovement()
    oppositionMovement()

    #drawing the visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,light_blue, player)
    pygame.draw.rect(screen,light_blue, opposition)
    pygame.draw.ellipse(screen,light_blue,ball)
    pygame.draw.aaline(screen,light_blue,(screen_width/2,0), (screen_width/2,screen_height))
    
    if getReady:
        ballrestart()
        
    playerUsername = gameFont.render(f"{playerName}",False,light_blue)
    screen.blit(playerUsername,(530,200))
    playScore = gameFont.render(f"{playerScore}",False,light_blue)
    screen.blit(playScore,(525,350))
    
    oppsName = gameFont.render(f"{oppositionName}",False,light_blue)
    screen.blit(oppsName,(250,200))
    oppScore = gameFont.render(f"{opponentScore}",False,light_blue)
    screen.blit(oppScore,(455,350))
    
    #Updating the window
    pygame.display.flip()
    clock.tick(60)
