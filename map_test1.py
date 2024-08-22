import pygame
from Config import WIDTH, HEIGHT

def initialize_map():
    # Загрузка изображения карты и создание его прямоугольника
    map_image = pygame.image.load('Maps/MapSprites/layoutTest.png')
    map_rect = map_image.get_rect()

    return map_image, map_rect