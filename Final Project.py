import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ryan's Final Space Trip")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BUTTON_COLOR = (0, 128, 0)  # Green color for the button

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Load assets
player_img = pygame.image.load("rocket.png")  # Replace with path to image
player_img = pygame.transform.scale(player_img, (50, 50))
meteor_img = pygame.image.load("meteor.png")  # Replace with path to image
meteor_img = pygame.transform.scale(meteor_img, (50, 50))

# Background Music
pygame.mixer.music.load("background_music.mp3")  # Replace with path to music
pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

# Starfield
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_speed = 5
enemies = []

# Score and game state
score = 0
high_score = 0  # Track the highest score
level = 1
running = True
paused = False  # Flag to track if the game is paused

# Sound effects
collision_sound = pygame.mixer.Sound("collision.mp3")  # Replace with path to sound


def spawn_enemy():
    """Create a new enemy at a random x-coordinate."""
    x = random.randint(0, WIDTH - enemy_size)
    y = 0 - enemy_size
    enemies.append({"x": x, "y": y, "speed": random.randint(3, 6)})

def move_enemies():
    """Update the position of all enemies."""
    global score
    for i in range(len(enemies)):
        enemy = enemies[i]
        enemy['y'] += enemy['speed']
        if enemy['y'] > HEIGHT:
            score += 1
            enemies[i] = {'x': -enemy_size, 'y': -enemy_size}  # Remove enemy off-screen

def check_collision(rect1, rect2):
    """Check for collision between two rectangles."""
    return rect1.colliderect(rect2)

def draw_objects():
    """Render all game objects on the screen."""
    screen.fill(BLACK)

    # Draw stars
    for star_x, star_y in stars:
        pygame.draw.circle(screen, WHITE, (star_x, star_y), 2)

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw enemies
    for enemy in enemies:
        screen.blit(meteor_img, (enemy["x"], enemy["y"]))

    # Draw score and level
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, YELLOW)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

def handle_input():
    """Handle player input for movement."""
    keys = pygame.key.get_pressed()
    global player_x
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

def game_over_screen():
    """Display the Game Over screen with the final score and automatically exit after a moment."""
    global high_score
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))

    score_font = pygame.font.SysFont(None, 48)
    score_text = score_font.render(f"Final Score: {score}", True, WHITE)
    high_score_text = score_font.render(f"High Score: {high_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

    # Update high score
    if score > high_score:
        high_score = score

    # Wait for a short moment before exiting
    pygame.time.delay(2000)  # Delay for 2 seconds (adjust as needed)

    pygame.quit()
    exit()

def reset_game():
    """Reset the game state for a new playthrough."""
    global player_x, player_y, player_speed, enemies, score, level, running
    player_x = WIDTH // 2 - player_size // 2
    player_y = HEIGHT - player_size - 10
    player_speed = 5
    enemies = []
    score = 0
    level = 1
    running = True

def update_stars():
    """Move stars downward to simulate space movement."""
    for i in range(len(stars)):
        star_x, star_y = stars[i]
        star_y += 2
        if star_y > HEIGHT:
            star_y = 0
            star_x = random.randint(0, WIDTH)
        stars[i] = (star_x, star_y)

def draw_main_menu():
    """Draw the main menu with start button and volume control."""
    font = pygame.font.SysFont(None, 72)
    title_text = font.render("Ryan's Final Space Trip", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 150))

    # Draw the start button, adjusted position
    button_width = 200
    button_height = 50
    start_button = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 50, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, start_button)

    # Draw the "Start Game" text centered within the button
    start_text = pygame.font.SysFont(None, 48).render("Start Game", True, BLACK)
    screen.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2,
                            start_button.y + (start_button.height - start_text.get_height()) // 2))

    pygame.display.flip()

    return start_button

def draw_pause_screen():
    """Display the pause screen."""
    font = pygame.font.SysFont(None, 72)
    pause_text = font.render("PAUSED", True, RED)
    screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - 100))

    pygame.display.flip()

def main_game_loop():
    """Main game loop."""
    global running, level, paused
    spawn_timer = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Toggle pause with the 'P' key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused  # Toggle the pause state

        if paused:
            draw_pause_screen()
            continue  # Skip the rest of the loop while paused

        handle_input()
        move_enemies()
        update_stars()

        # Check for collisions
        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_size, enemy_size)
            if check_collision(player_rect, enemy_rect):
                collision_sound.play()  # Play collision sound
                running = False
                game_over_screen()  # Automatically exit after the game over screen
                return

        # Spawn new enemies
        spawn_timer += 1
        if spawn_timer > 30:
            spawn_enemy()
            spawn_timer = 0

        # Increase difficulty as score increases
        if score > 20 * level:
            level += 1
            enemy_speed += 1  # Increase enemy speed

        # Clean up enemies that have gone off-screen
        enemies[:] = [enemy for enemy in enemies if enemy['x'] >= 0]

        draw_objects()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

def main():
    """Main function to run the game."""
    start_button = draw_main_menu()

    # Main menu loop to check for start button click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main_game_loop()

if __name__ == "__main__":
    main()
