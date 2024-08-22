import pygame
from Config import WIDTH, HEIGHT, up, left, down, right

class Player(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 5

    def update(self, keys):
        if keys[getattr(pygame, f'K_{up}')]:
            self.rect.y -= self.speed
        if keys[getattr(pygame, f'K_{left}')]:
            self.rect.x -= self.speed
        if keys[getattr(pygame, f'K_{down}')]:
            self.rect.y += self.speed
        if keys[getattr(pygame, f'K_{right}')]:
            self.rect.x += self.speed

        # Ограничиваем передвижение игрока границами экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self, screen, camera):
        # Смещение изображения игрока относительно камеры
        screen.blit(self.image, (self.rect.x - camera.x, self.rect.y - camera.y))
