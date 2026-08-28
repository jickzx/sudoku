import pygame


# Window settings
WIDTH = 600
HEIGHT = 700
FPS = 60
TITLE = "Sudoku"

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "menu":
                    play_button, settings_button = get_menu_buttons(screen)

                    if play_button.collidepoint(event.pos):
                        current_screen = "game"
                    elif settings_button.collidepoint(event.pos):
                        current_screen = "settings"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_screen = "menu"

        if current_screen == "menu":
            draw_menu(screen)
        elif current_screen == "game":
            draw_placeholder_screen(screen, "Game")
        elif current_screen == "settings":
            draw_placeholder_screen(screen, "Settings")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
