import pygame
import sys # interacts directly with the interpreter
import settings
import menu

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT, pygame.RESIZABLE)) # screen for sudoku

menu.draw_menu(screen)