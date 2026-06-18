import pygame
import sys # interacts directly with the interpreter
import settings

# menu screen

def draw_menu(screen):
    screen.fill(settings.WHITE)

    title_font = pygame.font.SysFont(None, 72)
    button_font = pygame.font.SysFont(None, 44)

    title_text = title_font.render("Sudoku", True, settings.BLACK)
    play_text = button_font.render("Play Game", True, settings.BLACK)
    settings_text = button_font.render("Settings", True, settings.BLACK)

    title_rect = title_text.get_rect(center=(settings.WIDTH // 2, 120))

    play_button = pygame.Rect(200, 250, 200, 60)
    settings_button = pygame.Rect(200, 340, 200, 60)

    pygame.draw.rect(screen, settings.GRAY, play_button)
    pygame.draw.rect(screen, settings.GRAY, settings_button)

    play_rect = play_text.get_rect(center=play_button.center)
    settings_rect = settings_text.get_rect(center=settings_button.center)

    screen.blit(title_text, title_rect)
    screen.blit(play_text, play_rect)
    screen.blit(settings_text, settings_rect)

    return play_button, settings_button

pygame.init()

screen = pygame.display.set_mode(
    (settings.WIDTH, settings.HEIGHT),
    pygame.RESIZABLE) # screen for sudoku

draw_menu(screen)

def main():
    game = Game(screen)

    while game.running:
        settings.pygame.FPS=60
    
    pygame.quit()

main()