import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Cool PyGame Window")

#colors
white = (255,255,255)
red = (255, 3, 3)
blue = (3, 3, 255)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space Key pressed!")

    screen.fill(white)

    pygame.display.update()

pygame.quit()