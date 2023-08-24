import pygame

# inializee the pygame
pygame.init()

# create the screen
# (width, height)
screen = pygame.display.set_mode((800, 600))

# caption and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


def player():
    screen.blit(playerImg, (playerX, playerY))

# game loop
running = True
while running:
    
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # if event.key == pygame.K_SPACE:
            #     if bullet_state is "ready":
            #         bulletSound = mixer.Sound("laser.wav")
            #         bulletSound.play()
            #         # Get the current x cordinate of the spaceship
            #         bulletX = playerX
            #         fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        




    player()
    playerX += playerX_change
    pygame.display.update()

