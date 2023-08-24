import pygame
pygame.init()

screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Sketch")
icon = pygame.image.load('practice/img/etch-a-sketch.png')
pygame.display.set_icon(icon)

x = 80
y = 80
width = 2
height = 2
vel = 1

# colors
lightgray = (224, 224, 224)
gray = (80, 88, 88)
red = (240,0,0)
white = (255,255,255)

# build screen background and red and white shapes 
screen.fill(lightgray)
pygame.draw.rect(screen, red, (0, 0, 50, 500)) 
pygame.draw.rect(screen, red, (0, 0, 600, 50))   
pygame.draw.rect(screen, red, (550, 0, 50, 600))   
pygame.draw.rect(screen, red, (0, 400, 600, 100))   
pygame.draw.circle(screen, white, (50,450), 35)
pygame.draw.circle(screen, white, (550,450), 35)

pygame.display.update() 

# capture screen
def save_drawing():
    pygame.image.save(screen,"saved_drawing.jpg")

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    pygame.draw.rect(screen, gray, (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()