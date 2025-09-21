import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Enemy block settings
enemy_size = 50
enemy_list = []
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

# --- Functions ---
def drop_enemies(enemy_list):
    """Add new enemies randomly at the top"""
    delay = random.randint(1, 20)
    if len(enemy_list) < 8 and delay == 1:
        x_pos = random.randint(0, WIDTH - enemy_size)
        enemy_list.append([x_pos, 0])

def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

def update_enemy_positions(enemy_list, score):
    for idx, enemy in enumerate(enemy_list):
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy_list.pop(idx)
            score += 1
    return score

def detect_collision(player_pos, enemy_list):
    px, py = player_pos
    player_rect = pygame.Rect(px, py, player_size, player_size)
    for enemy in enemy_list:
        ex, ey = enemy
        enemy_rect = pygame.Rect(ex, ey, enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            return True
    return False

# --- Main game loop ---
running = True
while running:
    screen.fill(WHITE)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Enemy logic
    drop_enemies(enemy_list)
    score = update_enemy_positions(enemy_list, score)

    # Draw everything
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))  # player
    draw_enemies(enemy_list)

    # Check collisions
    if detect_collision((player_x, player_y), enemy_list):
        screen.fill(BLACK)
        game_over_text = font.render("GAME OVER! Final Score: " + str(score), True, WHITE)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
        pygame.display.flip()
        pygame.time.wait(2000)  # wait before quitting
        running = False

    # Draw score
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
