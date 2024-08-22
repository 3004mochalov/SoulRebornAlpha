import pygame
import sys
from StartGame import start_game_menu
from Config import WIDTH, HEIGHT
# Инициализация Pygame
pygame.init()


class Button:
    def __init__(self, image, pressed_image, text, font, color, scale=1, action=None):
        # Масштабирование изображений
        self.original_image = image
        self.original_pressed_image = pressed_image

        # Получение новых размеров с применением масштаба
        width = int(self.original_image.get_width() * scale)
        height = int(self.original_image.get_height() * scale)

        # Применение масштабирования к изображениям
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.pressed_image = pygame.transform.scale(self.original_pressed_image, (width, height))
        self.rect = self.image.get_rect()
        self.pressed = False
        self.action = action

        # Создаем текстовую метку и её прямоугольник
        self.text_surface = font.render(text, True, color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def update_position(self, center_x, center_y):
        self.rect.center = (center_x, center_y)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        if self.pressed:
            screen.blit(self.pressed_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.pressed = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos) and self.pressed:
                    self.pressed = False
                    if self.action:  # Если кнопка была нажата, выполнить действие
                        self.action()
            elif event.type == pygame.MOUSEMOTION:
                if not self.rect.collidepoint(event.pos):
                    self.pressed = False

    def on_click(self):
        if self.action:  # Вызывать действие кнопки также здесь, если нужно
            self.action()




start_game_selected = False # Добавьте эту переменную в начале
# Здесь должна быть реализация функции start_game
def start_game():
    global running, start_game_selected
    running = True
    start_game_selected = True  # Устанавливаем этот флаг когда пользователь выбирает начать игру
    start_game_menu()


# Здесь должна быть реализация функции settings
def settings():
    print("Настройки игры!")  # Здесь можно вызвать меню настроек


# Функция выхода из игры
def quit_game():
    pygame.quit()
    sys.exit()


# Указание размеров окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SoulReborn')

# Загрузка изображений для иконки и кнопок
icon_image = pygame.image.load('icon.png')
button_image = pygame.image.load('MainMenuSprites/button.png')
button_pressed_image = pygame.image.load('MainMenuSprites/button_pressed.png')

logo_image = pygame.image.load('MainMenuSprites/logo.png')
# Масштабирование логотипа, если это необходимо (опционально)
# logo_image = pygame.transform.scale(logo_image, (новый_ширину, новая_высоту))
logo_rect = logo_image.get_rect()

# Высота кнопки
button_scale = 1  # Пример высоты кнопки

# Установка иконки окна
pygame.display.set_icon(icon_image)

# Создаем шрифт для текста на кнопках
button_font = pygame.font.Font(None, 18)  # None означает использование шрифта по умолчанию
button_text_color = (0, 0, 0)

# Теперь Button требует дополнительные аргументы: текст для кнопки, шрифт и цвет текста
button1 = Button(button_image, button_pressed_image, 'start game', button_font, button_text_color, button_scale, start_game)
button_settings = Button(button_image, button_pressed_image, 'settings', button_font, button_text_color, button_scale, settings)
button2 = Button(button_image, button_pressed_image, 'quit game', button_font, button_text_color, button_scale, quit_game)


# Определение расстояния между кнопками
button_spacing = 20

top_offset_quantifier = 3
top_offset = HEIGHT - HEIGHT/top_offset_quantifier  # отступ от верхней границы

# Основной цикл игры
running = True
while running:
    # Заливка экрана
    screen.fill((0, 0, 255))

    # Определение текущего размера экрана
    WIDTH, HEIGHT = pygame.display.get_surface().get_size()

    # Расчёт позиций для кнопок
    total_buttons_height = (button1.rect.height +
                            button_settings.rect.height +
                            button2.rect.height +
                            button_spacing * 2)

    # Расчёт позиций для кнопок, начиная с отступа от верхней части окна
    button1_y_position = top_offset
    button_settings_y_position = button1_y_position + button1.rect.height + button_spacing
    button2_y_position = button_settings_y_position + button_settings.rect.height + button_spacing

    button1.update_position(WIDTH / 2, button1_y_position)
    button_settings.update_position(WIDTH / 2, button_settings_y_position)
    button2.update_position(WIDTH / 2, button2_y_position)

    logo_rect.center = (WIDTH / 2, button1_y_position / 2)
    screen.blit(logo_image, logo_rect)

    # Отрисовка кнопок
    button1.draw(screen)
    button_settings.draw(screen)
    button2.draw(screen)

    # Получение списка всех событий
    event_list = pygame.event.get()

    # Обработка событий
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False

    # Обновление состояния кнопок
    button1.update(event_list)
    button_settings.update(event_list)
    button2.update(event_list)

    # Переключение экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
