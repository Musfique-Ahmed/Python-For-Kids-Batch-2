# import pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("My Cool PyGame Window")

# #colors
# white = (255,255,255)
# red = (255, 3, 3)
# blue = (3, 3, 255)


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill(white)
#     pygame.draw.rect(screen, red, (50, 50, 100, 50))
#     pygame.draw.circle(screen, blue, (250, 200), 50)
#     pygame.display.update()

# pygame.quit()


import pygame

pygame.init()


screen = pygame.display.set_mode((333, 555))
pygame.display.set_caption("PYGAMe window~... :)")


black = (0, 0, 0)
mint = (152, 152, 152)
white = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    screen.fill(mint)

    
    # pygame.draw.rect(screen, black, (50, 50, 100, 50))  # x, y, width, height

    
    pygame.draw.line(screen, white, (10, 10), (200, 200), 3)  # start_pos, end_pos, width
    pygame.draw.polygon(screen, black, [(120,50), (160,50), (140, 70)])
    pygame.display.update()

pygame.quit()