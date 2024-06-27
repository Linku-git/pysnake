import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake properties
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction

# Food
food_pos = [random.randrange(1, (width//10)) * 10, 
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Game settings
score = 0
game_over = False
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    # Validate direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Move the snake
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "RIGHT":
        snake_pos[0] += 10

    # Teleport snake when it reaches the edge
    if snake_pos[0] < 0:
        snake_pos[0] = width - 10
    if snake_pos[0] > width - 10:
        snake_pos[0] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = height - 10
    if snake_pos[1] > height - 10:
        snake_pos[1] = 0

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, 
                    random.randrange(1, (height//10)) * 10]
    food_spawn = True

    # Draw everything
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(15)

pygame.quit()