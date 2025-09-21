import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Cool PyGame Window")

#colors
white = (255,255,255)
red = (255, 3, 3)
blue = (3, 3, 255)

x,y = 400,300


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] : x = x - 5
    if keys[pygame.K_RIGHT] : x += 5
    if keys[pygame.K_UP] : x = x - 5
    if keys[pygame.K_DOWN] : x += 5

    screen.fill(white)
    pygame.draw.rect(screen, red, (50, 50, 100, 50))
    # pygame.draw.circle(screen, blue, (250, 200), 50)
    pygame.display.update()

pygame.quit()
