# import pygame
# # print(pygame.__version__)

# pygame.init()


# screen = pygame.display.set_mode((500, 400))
# pygame.display.set_caption("This is my first PyGame")


# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False


# pygame.quit()



# import pygame
# pygame.init()
# screen=pygame.display.set_mode((333,555))
# pygame.display.set_caption("PYGAME... :)")
# running=True
# while running:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             running=False
# pygame.quit()



import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Cool PyGame Window")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()