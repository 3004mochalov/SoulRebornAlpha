import pygame
import sys
import MainMenu
from Config import WIDTH, HEIGHT

# Устанавливаем заголовок и иконку
pygame.display.set_caption('SoulReborn')
icon_image = pygame.image.load('icon.png')
pygame.display.set_icon(icon_image)

def main():
    MainMenu.start_game()  # В MainMenu.py должен быть основной игровой цикл в функции start_game

if __name__ == '__main__':
    pygame.init()  # Эту строчку перенес из MainMenu.py сюда, чтобы инициализировать pygame один раз
    main()

