import pygame

# inialize the pygame
pygame.init()

# create the screen
# (width, height)
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Move Shape")
icon = pygame.image.load('clown-fish.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('clown-fish.png')
playerX = 50
playerY = 500
playerX_change = 0

# wave
waveImg = pygame.image.load('wave.png')
waveX = 700
waveY = 50

def player():
    screen.blit(playerImg, (playerX, playerY))

def wave():
    screen.blit(waveImg, (waveX, waveY))

# game loop
running = True
while running:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

    player()
    wave()
    pygame.display.update()

