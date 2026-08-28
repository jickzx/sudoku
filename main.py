import pygame
import random

#############
# Constants
#############

# Window settings
WIDTH = 600
HEIGHT = 700
FPS = 60
TITLE = "Sudoku"

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

SOLVED_BOARD = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]

def create_starting_board(empty_cells=40):
    original_numbers = list(range(1, 10))
    shuffled_numbers = original_numbers.copy()
    random.shuffle(shuffled_numbers)

    number_changes = dict(zip(original_numbers, shuffled_numbers))

    board = []

    for row in SOLVED_BOARD:
        new_row = []

        for number in row:
            new_row.append(number_changes[number])

        board.append(new_row)

    positions = []

    for row in range(9):
        for column in range(9):
            positions.append((row, column))

    random.shuffle(positions)

    for row, column in positions[:empty_cells]:
        board[row][column] = 0

    return board

def draw_game(screen, board):
    screen.fill(WHITE)

    grid_size = min(screen.get_width() - 40, screen.get_height() - 140)
    cell_size = grid_size // 9
    grid_size = cell_size * 9

    grid_x = (screen.get_width() - grid_size) // 2
    grid_y = 40

    number_font = pygame.font.SysFont(None, int(cell_size * 0.7))

    # Draw the numbers
    for row in range(9):
        for column in range(9):
            number = board[row][column]

            if number != 0:
                number_text = number_font.render(str(number), True, BLACK)

                cell_centre = (
                    grid_x + column * cell_size + cell_size // 2,
                    grid_y + row * cell_size + cell_size // 2,
                )

                number_rect = number_text.get_rect(center=cell_centre)
                screen.blit(number_text, number_rect)

    # Draw the grid lines
    for line in range(10):
        line_width = 4 if line % 3 == 0 else 1

        x = grid_x + line * cell_size
        pygame.draw.line(
            screen,
            BLACK,
            (x, grid_y),
            (x, grid_y + grid_size),
            line_width,
        )

        y = grid_y + line * cell_size
        pygame.draw.line(
            screen,
            BLACK,
            (grid_x, y),
            (grid_x + grid_size, y),
            line_width,
        )

def get_menu_buttons(screen):
    """Return menu button rectangles centred in the current window."""
    centre_x = screen.get_width() // 2
    play_button = pygame.Rect(0, 0, 200, 60)
    settings_button = pygame.Rect(0, 0, 200, 60)
    play_button.center = (centre_x, 280)
    settings_button.center = (centre_x, 370)
    return play_button, settings_button


def draw_menu(screen):
    screen.fill(WHITE)

    title_font = pygame.font.SysFont(None, 72)
    button_font = pygame.font.SysFont(None, 44)

    title_text = title_font.render(TITLE, True, BLACK)
    play_text = button_font.render("Play Game", True, BLACK)
    settings_text = button_font.render("Settings", True, BLACK)

    title_rect = title_text.get_rect(
        center=(screen.get_width() // 2, 120)
    )
    play_button, settings_button = get_menu_buttons(screen)

    pygame.draw.rect(screen, GRAY, play_button)
    pygame.draw.rect(screen, GRAY, settings_button)

    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_text.get_rect(center=play_button.center))
    screen.blit(
        settings_text,
        settings_text.get_rect(center=settings_button.center),
    )


def draw_placeholder_screen(screen, heading):
    """Temporary screen used until the game and settings UI are built."""
    screen.fill(WHITE)
    heading_font = pygame.font.SysFont(None, 64)
    help_font = pygame.font.SysFont(None, 30)

    heading_text = heading_font.render(heading, True, BLACK)
    help_text = help_font.render("Press Escape to return", True, BLACK)

    screen.blit(
        heading_text,
        heading_text.get_rect(center=(screen.get_width() // 2, 160)),
    )
    screen.blit(
        help_text,
        help_text.get_rect(center=(screen.get_width() // 2, 230)),
    )


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption(TITLE)

    clock = pygame.time.Clock()
    running = True
    current_screen = "menu"
    starting_board = None
    board = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "menu":
                    play_button, settings_button = get_menu_buttons(screen)

                    if play_button.collidepoint(event.pos):
                        starting_board = create_starting_board()
                        board = [row.copy() for row in starting_board]
                        current_screen = "game"
                    elif settings_button.collidepoint(event.pos):
                        current_screen = "settings"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = "menu"

        if current_screen == "menu":
            draw_menu(screen)
        elif current_screen == "game":
            draw_game(screen, board)
        elif current_screen == "settings":
            draw_placeholder_screen(screen, "Settings")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
