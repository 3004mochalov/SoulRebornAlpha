import pygame
import sys
from Config import WIDTH, HEIGHT

# Initialize Pygame
pygame.init()


class Button:
    # добавил параметр scale к конструктору
    def __init__(self, image, pressed_image, text, font, color, pos, scale=1, action=None):
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.pressed_image = pygame.transform.scale(pressed_image, (int(pressed_image.get_width() * scale),
                                                                    int(pressed_image.get_height() * scale)))
        self.action = action
        self.pos = pos

        self.rect = self.image.get_rect(center=pos)
        self.text = font.render(text, True, color)
        self.text_rect = self.text.get_rect(center=self.rect.center)

        self.pressed = False

    def draw(self, screen):
        if self.pressed:
            screen.blit(self.pressed_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
                self.pressed = True
            elif event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(event.pos):
                if self.pressed:
                    self.pressed = False
                    if self.action:
                        self.action()

    # новый метод для обновления позиции кнопки
    def update_position(self, center_x, center_y):
        self.rect.center = (center_x, center_y)
        self.text_rect = self.text.get_rect(center=self.rect.center)


def new_game_action():
    print("Новая игра начата!")  # Здесь должен быть код для начала новой игры


def load_game_action():
    print("Загрузка предыдущей игры!")  # Здесь должен быть код для загрузки игры


def back_action():
    global running
    running = False


def start_game_menu():
    global running
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    button_scale = 1
    button_spacing = 20

    button_font = pygame.font.Font(None, 18)
    button_color = (0, 0, 0)
    button_image = pygame.image.load('MainMenuSprites/button.png')
    button_pressed_image = pygame.image.load('MainMenuSprites/button_pressed.png')

    new_game_button = Button(button_image, button_pressed_image, 'New Game', button_font, button_color, (0, 0),
                             button_scale, new_game_action)
    load_game_button = Button(button_image, button_pressed_image, 'Load Game', button_font, button_color, (0, 0),
                              button_scale, load_game_action)
    back_button = Button(button_image, button_pressed_image, 'Back', button_font, button_color, (0, 0), button_scale,
                         back_action)

    buttons = [new_game_button, load_game_button, back_button]

    running = True
    while running:
        screen.fill((0, 0, 255))

        current_width, current_height = screen.get_size()

        total_buttons_height = (new_game_button.rect.height +
                                load_game_button.rect.height +
                                back_button.rect.height +
                                button_spacing * 2)
        top_offset = current_height / 2 - total_buttons_height / 2

        new_game_button.update_position(current_width / 2, top_offset)
        load_game_button.update_position(current_width / 2, top_offset + new_game_button.rect.height + button_spacing)
        back_button.update_position(current_width / 2,
                                    top_offset + new_game_button.rect.height +
                                    load_game_button.rect.height + button_spacing * 2)

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        for button in buttons:
            button.update(event_list)
            button.draw(screen)

        pygame.display.flip()
