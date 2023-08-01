import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Character dimensions
CHAR_WIDTH, CHAR_HEIGHT = 50, 50

# Block dimensions
BLOCK_WIDTH, BLOCK_HEIGHT = 50, 50

# Character position
character_x = WIDTH // 2
character_y = HEIGHT - CHAR_HEIGHT - 10

# Block variables
block_x = random.randint(0, WIDTH - BLOCK_WIDTH)
block_y = 0
block_speed = 5

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blocks")

# Clock to control frame rate
clock = pygame.time.Clock()

def draw_character(x, y):
    pygame.draw.rect(screen, RED, (x, y, CHAR_WIDTH, CHAR_HEIGHT))

def draw_block(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, BLACK)
    screen.blit(text, (WIDTH//2 - 140, HEIGHT//2 - 40))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

def game_loop():
    global character_x, block_x, block_y, block_speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            character_x -= 5
        if keys[pygame.K_RIGHT]:
            character_x += 5

        # Check if the character collides with the block
        if character_x < block_x + BLOCK_WIDTH and character_x + CHAR_WIDTH > block_x and character_y < block_y + BLOCK_HEIGHT and character_y + CHAR_HEIGHT > block_y:
            game_over()

        # Update the block's position
        block_y += block_speed

        # If the block is off the screen, reset its position
        if block_y > HEIGHT:
            block_x = random.randint(0, WIDTH - BLOCK_WIDTH)
            block_y = 0
            block_speed += 1

        # Clear the screen
        screen.fill(WHITE)

        # Draw the character and block
        draw_character(character_x, character_y)
        draw_block(block_x, block_y)

        # Update the display
        pygame.display.update()

        # Limit frames per second
        clock.tick(60)

if __name__ == "__main__":
    game_loop()
