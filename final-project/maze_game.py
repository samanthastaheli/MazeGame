import pygame
import numpy as np

# inialize the pygame
pygame.init()

# inialize font module
# pygame.font.init()

# create the screen
# (width, height)
screen_width = 850
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

screen_array = np.asarray(screen)
print(screen_array)

# caption and icon
pygame.display.set_caption("Maze Game")
icon = pygame.image.load('img/red.png')
pygame.display.set_icon(icon)

# VARIABLES
playerImg = pygame.image.load('img/pacman.png')
playerX = 160
playerY = 620
playerR_change = 5
playerL_change = -5
playerU_change = -5
playerD_change = 5

# colors
black = (0,0,0)
blue = ('#2335C1')
dark_blue = ('#0F1A59')
yellow = ('#FEF851')
red = ('#ED3833')
orange = ('#F7B846')
pink = ('#F5BCDD')
teal = ('#6FF9DE')
peach = ('#F6B897')
lightgray = (224, 224, 224)

# text
title_font = pygame.font.Font('font/Oswald.ttf', 60)
reg_font = pygame.font.Font('font/OpenSans-Regular.ttf', 32)
cel_font = pygame.font.Font('font/Oswald.ttf', 100)


# FUNCTIONS
def player():
    screen.blit(playerImg, (playerX, playerY))

def create_background(background_color):
    # build screen background
    screen.fill(background_color)

def create_maze(maze_color):
    # build maze
    # maze varibles 
    barrier = 10 # this is how thick the maze walls will be
    player_space = 50 # this is how much space is needed for player to move through 

    side = 100
    top_side = 150
    bottom = screen_height - side
    maze_width = screen_width - side * 2
    maze_height = 450

    top_leftX = side
    top_leftY = top_side
    top_rightX = screen_width - side
    top_rightY = top_leftY
    bot_leftX = top_leftX
    bot_leftY = maze_height + top_side

    # paramerters = screen, color, (x, y, width, height)
    #borders
    pygame.draw.rect(screen, maze_color, (top_leftX, top_leftY, barrier, maze_height)) # left border
    pygame.draw.rect(screen, maze_color, (top_rightX, top_rightY, barrier, maze_height)) # right border 
    pygame.draw.rect(screen, maze_color, (top_leftX, top_leftY, (maze_width-100), barrier)) # top border left
    pygame.draw.rect(screen, maze_color, ((screen_width-150), 150, player_space, barrier)) # top border right
    pygame.draw.rect(screen, maze_color, (bot_leftX, bot_leftY, player_space, barrier)) # bottom border left
    pygame.draw.rect(screen, maze_color, ((bot_leftX+player_space*2), bot_leftY, (maze_width-player_space*2+barrier), barrier)) # bottom border right
    # size 250px (orange)
    pygame.draw.rect(screen, maze_color, ((side+550), (bottom-400), barrier, 250))
    # size 200px (green)
    pygame.draw.rect(screen, maze_color, (side, (bottom-200), 200, barrier))
    pygame.draw.rect(screen, maze_color, ((side + 100), (bottom-300), 200, barrier))
    # size 150px (purple)
    # horizontal
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-50), 150, barrier))
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-50), 150, barrier))
    pygame.draw.rect(screen, maze_color, ((side+150), (bottom-150), 150, barrier))
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-250), 150, barrier))
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-200), (150+barrier), barrier))
    # vertical 
    pygame.draw.rect(screen, maze_color, ((side+200), (bottom-400), barrier, 150))
    pygame.draw.rect(screen, maze_color, ((side+450), (bottom-400), barrier, 150))
    pygame.draw.rect(screen, maze_color, ((side+600), (bottom-400), barrier, 150))
    pygame.draw.rect(screen, maze_color, ((side+450), (bottom-200), barrier, 150))

    # size 100px (teal)
    # horizontal
    pygame.draw.rect(screen, maze_color, ((side+300), (bottom-100), 100, barrier)) #1
    pygame.draw.rect(screen, maze_color, ((side+350), (bottom-150), 100, barrier)) #2
    pygame.draw.rect(screen, maze_color, ((side+450), (bottom-50), 100, barrier)) #3
    pygame.draw.rect(screen, maze_color, ((side+350), (bottom-300), 100, barrier)) #4
    pygame.draw.rect(screen, maze_color, ((side+300), (bottom-350), 100, barrier)) #5
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-400), 100, barrier)) #6
    pygame.draw.rect(screen, maze_color, ((side + 400), (bottom-400), 100, barrier)) #7
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-400), 100, barrier)) #8
    # vertical
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-150), barrier, 100)) #1
    pygame.draw.rect(screen, maze_color, ((side+200), (bottom-100), barrier, 100)) #2
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-150), barrier, 100)) #3
    pygame.draw.rect(screen, maze_color, ((side+400), (bottom-150), barrier, (100+barrier))) #4 
    pygame.draw.rect(screen, maze_color, ((side+500), (bottom-200), barrier, 100)) #5
    pygame.draw.rect(screen, maze_color, ((side+600), (bottom-200), barrier, 100)) #6
    pygame.draw.rect(screen, maze_color, ((side+500), (bottom-350), barrier, 100)) #7
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-400), barrier, 100)) #8
    pygame.draw.rect(screen, maze_color, ((side+100), (bottom-350), barrier, 100)) #9
    pygame.draw.rect(screen, maze_color, ((side+150), (bottom-450), barrier, 100)) #10

    # size 50px (pink)
    # horizontal
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-150), 50, barrier)) #1
    pygame.draw.rect(screen, maze_color, ((side+150), (bottom-250), (50+barrier), barrier)) #2
    pygame.draw.rect(screen, maze_color, ((side+200), (bottom-350), 50, barrier)) #3
    pygame.draw.rect(screen, maze_color, ((side+500), (bottom-350), 50, barrier)) #4
    pygame.draw.rect(screen, maze_color, ((side+600), (bottom-350), 50, barrier)) #5
    pygame.draw.rect(screen, maze_color, ((side+500), (bottom-150), (50+barrier), barrier)) #6
    pygame.draw.rect(screen, maze_color, ((side+600), (bottom-150), 50, barrier)) #7
    pygame.draw.rect(screen, maze_color, ((side+600), (bottom-50), 50, barrier)) #8
    pygame.draw.rect(screen, maze_color, ((side + 550), (bottom-400), 50, barrier)) #9
    # pygame.draw.rect(screen, maze_color, ((side+250), (bottom-250), 50, barrier)) #10
    # pygame.draw.rect(screen, maze_color, ((side+350), (bottom-250), 50, barrier)) #11
    # vertical
    pygame.draw.rect(screen, maze_color, ((side+50), (bottom-250), barrier, 50)) #1
    pygame.draw.rect(screen, maze_color, ((side+100), (bottom-150), barrier, 50)) #2
    pygame.draw.rect(screen, maze_color, ((side+150), (bottom-100), barrier, 50)) #3
    pygame.draw.rect(screen, maze_color, ((side+300), (bottom-maze_height), barrier, 50)) #4
    pygame.draw.rect(screen, maze_color, ((side+400), (bottom-maze_height+50), barrier, (50+barrier))) #5
    pygame.draw.rect(screen, maze_color, ((side+550), (bottom-100), barrier, (50+barrier))) #6
    pygame.draw.rect(screen, maze_color, ((side+250), (bottom-250), barrier, 50)) #7
    pygame.draw.rect(screen, maze_color, ((side+400), (bottom-250), barrier, 50)) #8

def get_barrier(x, y):
    pixel_color = pygame.Surface.get_at(screen, (x,y))
    if pixel_color == (35, 53, 193, 255):
        return True

def create_ghost(redImgUrl, orangeImgUrl, pinkImgUrl, tealImgUrl):
    # images
    red = pygame.image.load(redImgUrl)
    orange = pygame.image.load(orangeImgUrl)
    pink = pygame.image.load(pinkImgUrl)
    teal = pygame.image.load(tealImgUrl)
    # coordinates
    redX = 362
    redY = 318
    orangeX = 462
    orangeY = 418
    pinkX = 610
    pinkY = 218
    tealX = 218
    tealY = 265
    # add image to screen
    screen.blit(red, (redX, redY))
    screen.blit(orange, (orangeX, orangeY))
    screen.blit(pink, (pinkX, pinkY))
    screen.blit(teal, (tealX, tealY))

def display_text(text, font, color, posX, posY):
    # diplay title 'The Maze'
    # display instructions
    # display Tip: don't hit the ghost
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.center = (posX, posY)
    screen.blit(text, textRect)

def draw_grid(screen, color):
    # vertical lines
    pygame.draw.rect(screen, color, (0, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (50, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (100, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (150, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (200, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (250, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (300, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (350, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (400, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (450, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (500, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (550, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (600, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (650, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (700, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (750, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (800, 0, 1, screen_height))
    pygame.draw.rect(screen, color, (850, 0, 1, screen_height))

    # horizontal lines
    pygame.draw.rect(screen, color, (0, 0, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 50, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 100, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 150, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 200, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 250, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 300, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 350, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 400, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 450, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 500, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 550, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 600, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 650, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 700, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 750, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 800, screen_width, 1))
    pygame.draw.rect(screen, color, (0, 850, screen_width, 1))

run = True

while run:
    pygame.time.delay(50)

    create_background(black)
    draw_grid(screen, dark_blue)
    display_text('The Maze', title_font, orange, (screen_width/2), 50)
    create_maze(blue)
    create_ghost('img/red.png', 'img/orange.png', 'img/pink.png', 'img/teal.png')
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # give keys function
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        if get_barrier(playerX, playerY) == True:
            playerL_change = 5
        else:
            playerL_change = -5
        playerX += playerL_change

    if keys[pygame.K_RIGHT]:
        if get_barrier(playerX, playerY) == True:
            playerR_change = -30
        else:
            playerR_change = 5
        playerX += playerR_change

    if keys[pygame.K_UP]:
        if get_barrier(playerX, playerY) == True:
            playerU_change = 5
        else:
            playerU_change = -5
        playerY += playerU_change
        
    if keys[pygame.K_DOWN]:
        if get_barrier(playerX, playerY) == True:
            playerD_change = -30
        else:
            playerD_change = 5
        playerY += playerD_change

    # build and update player position 
    player()
    pygame.display.update() 

    # game boundry 
    if playerX <= 50:
        playerX = 50
    elif playerX >= 750:
        playerX = 750
    if playerY <= 100:
        playerY = 100
    elif playerY >= 660:
        playerY = 660

    # player exits
    if playerY < 150:
        display_text('You Did It!', cel_font, orange, (screen_width/2), (screen_height/2))
        print('Exit Susessful!')


pygame.quit()