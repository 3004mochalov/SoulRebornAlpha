import pygame
from Config import WIDTH, HEIGHT
from PlayerBehavior import Player
from map_test1 import initialize_map

def update_camera(camera, target_rect, map_rect):
    x, y, _, _ = target_rect
    _, _, w, h = camera
    half_width, half_height = WIDTH // 2, HEIGHT // 2

    # Центрирование камеры относительно цели
    camera = pygame.Rect(x - half_width, y - half_height, w, h)

    # Не допускаем выхода за левую и верхнюю границы карты
    camera.x = max(camera.x, 0)
    camera.y = max(camera.y, 0)
    print(camera)
    # Не допускаем выхода за правую и нижнюю границы карты
    camera.x = min(camera.x, map_rect.width - camera.width)
    camera.y = min(camera.y, map_rect.height - camera.height)
    print(camera)
    return camera


# Инициализация Pygame и создание экрана
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Инициализация карты
map_image, map_rect = initialize_map()

# Загрузка спрайта игрока и создание объекта
player = Player('characters/CharactersSprites/TestCharacter/test.png', (WIDTH//2, HEIGHT//2))

# Создание камеры
camera = pygame.Rect(0, 0, WIDTH, HEIGHT)

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление игрока
    keys = pygame.key.get_pressed()
    player.update(keys)

    # Обновление камеры
    camera = update_camera(camera, player.rect, map_rect)
    # Отрисовка карты с учетом камеры
    screen.blit(map_image, (0, 0), camera)
    # Отрисовка игрока относительно камеры
    player.draw(screen, camera)

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)  # ФПС

pygame.quit()
