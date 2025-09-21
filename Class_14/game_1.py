import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pygame Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)

# Player settings
player_size = 40
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_speed = 5

# Goal settings
goal_size = 40
goal_x = random.randint(0, WIDTH - goal_size)
goal_y = random.randint(0, HEIGHT - goal_size)

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Handle user input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player inside window
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    # --- Collision detection ---
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    goal_rect = pygame.Rect(goal_x, goal_y, goal_size, goal_size)

    if player_rect.colliderect(goal_rect):
        # Reset goal to a new random position
        goal_x = random.randint(0, WIDTH - goal_size)
        goal_y = random.randint(0, HEIGHT - goal_size)

    # --- Drawing ---
    screen.fill(WHITE)  # clear screen
    pygame.draw.rect(screen, BLUE, player_rect)  # player
    pygame.draw.rect(screen, RED, goal_rect)     # goal

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
