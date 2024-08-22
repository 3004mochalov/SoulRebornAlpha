import pygame

# Импорт функций генерации массива из модулей (предполагается, что они уже написаны)
from BasicScreenComposition import generate_arrays as generate_basic_arrays
from WideScreenComposition import generate_arrays as generate_wide_arrays

# Инициализация Pygame
pygame.init()

# Создание окна
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Window Composition Grid')

# Переменные состояния
show_grid = False
input_active = False  # Глобальная переменная для контроля состояния ввода


# Функция для отображения сетки
def toggle_grid(show):
    screen.fill((0, 0, 0))
    if show:
        x_values, y_values = generate_basic_arrays() if show == 'basic' else generate_wide_arrays()
        for x in x_values:
            pygame.draw.line(screen, (0, 0, 255), (x * 100, 0), (x * 100, screen_height), 1)
        for y in y_values:
            pygame.draw.line(screen, (255, 0, 0), (0, y * 100), (screen_width, y * 100), 1)
    pygame.display.flip()

# Функция для обработки команды
def process_command(command):
    global show_grid, input_active  # Добавляем running к глобальным переменным
    parts = command.split()
    if parts:  # Проверяем, что список parts не пустой
        if parts[0] == 'grid' and len(parts) > 1:
            if parts[1].lower() == 'true':
                show_grid = 'basic'
            elif parts[1].lower() == 'false':
                show_grid = False
            elif parts[1].lower() == 'wide':
                show_grid = 'wide'
            toggle_grid(show_grid)
        else:
            # Если команда не начинается на 'grid', предположим, что это команда выхода
            input_active = False  # Устанавливаем input_active в False, чтобы выйти из основного цикла

# Функция для рендеринга текстового поля и обработки текстового ввода
def input_loop(surface):
    global input_active
    font = pygame.font.Font(None, 32)
    input_box = pygame.Rect(0, 0, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    clock = pygame.time.Clock()  # Создаем экземпляр часов для контроля частоты кадров

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKQUOTE:  # Нажатие на Backquote
                    input_active = False  # Деактивируем ввод
                    return text if active else None
                if active:
                    if event.key == pygame.K_RETURN:
                        return text if text.strip() else None  # Вернуть текст, только если он не пустой
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        # Отрисовка текстового поля
        surface.fill((30, 30, 30))
        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(surface, color, input_box, 2)

        pygame.display.flip()  # Обновление экрана
        clock.tick(30)  # Ограничение частоты кадров до 30 FPS


# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Добавляем обработчик события, который активирует поля ввода при нажатии 'i'
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:  # Предполагаем, что 'i' - это клавиша для активации ввода
                input_active = not input_active  # Переключаем режим активности ввода

    if input_active:
        command = input_loop(screen)  # Получаем команду из поля ввода
        if command is not None:  # Обработаем команду только если она есть
            process_command(command)
            input_active = False  # Выключаем режим ввода после обработки команды
    else:
        pygame.display.flip()  # Это обновит экран даже когда input_active == True

    pygame.time.Clock().tick(30)  # Ограничение частоты кадров до 30 FPS

# Очистка ресурсов Pygame перед закрытием
pygame.quit()
