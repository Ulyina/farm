#main.py
import pygame
import time
from player import Player
from plants import Corn, Potato, Carrot
from shop import Shop
from animals import Chicken, Cow
from inventory import draw_inventory  # Импорт функции для отображения инвентаря

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("mus.ogg")
pygame.mixer.music.play(-1)

# Настройки экрана
screen_width = 830  # Ширина экрана
screen_height = 600  # Высота экрана
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Farm Game")

# Цвета
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
well_image = pygame.image.load("well.png").convert_alpha()
well_image = pygame.transform.scale(well_image, (100, 100))
well_rect = well_image.get_rect(topleft=(680, 20))

# Загрузка изображения для курсора
cursor_image = pygame.image.load("cursor.png").convert_alpha()
cursor_image = pygame.transform.scale(cursor_image, (50, 50))  # Измените размер при необходимости

# Прячем системный курсор
pygame.mouse.set_visible(False)

dirt_image = pygame.image.load("dirt.png").convert_alpha()
dirt_image = pygame.transform.scale(dirt_image, (60, 60))

grass_image = pygame.image.load("grass.png").convert_alpha()
grass_image = pygame.transform.scale(grass_image, (60, 60))

shop_button_image = pygame.image.load("shop_button.png").convert_alpha()
shop_button_image = pygame.transform.scale(shop_button_image, (100, 100))

corn_image = pygame.image.load("grown_corn.png").convert_alpha()
corn_image = pygame.transform.scale(corn_image, (60, 60))

potato_image = pygame.image.load("grown_potato.png").convert_alpha()
potato_image = pygame.transform.scale(potato_image, (60, 60))

carrot_image = pygame.image.load("grown_carrot.png").convert_alpha()
carrot_image = pygame.transform.scale(carrot_image, (60, 60))

# Кнопки
shop_button = pygame.Rect(680, 150, 120, 40)
inventory_button = pygame.Rect(670, 260, 120, 40)

# Игрок
player = Player(screen_height)  # Передаем высоту экрана

# Шрифт
font = pygame.font.Font(None, 36)

# Кнопки для выбора растений
corn_button = pygame.Rect(50, 540, 100, 40)
potato_button = pygame.Rect(200, 540, 100, 40)
carrot_button = pygame.Rect(350, 540, 100, 40)

# Инициализация инвентаря
inventory_visible = False  # Флаг для отображения инвентаря

# Создание магазина
shop = Shop(player)

# Игровой цикл
running = True
while running:
    screen.fill(LIGHT_GREEN)

    # Рисуем рамки
    pygame.draw.rect(screen, WHITE, (660, 0, 170, screen_height))  # Правая панель
    pygame.draw.rect(screen, WHITE, (0, 520, screen_width, 80))  # Нижняя панель
    pygame.draw.rect(screen, WHITE, inventory_button)  # Кнопка инвентаря

    # Рисуем сетку
    for x in range(0, 660, 60):
        for y in range(0, 520, 60):
            pygame.draw.rect(screen, WHITE, (x, y, 60, 60), 1)
            if (x // 60) % 2 == 1 and (y // 60) % 2 == 1:
                screen.blit(dirt_image, (x, y))
            else:
                screen.blit(grass_image, (x, y))

    # Отображаем магазин и колодец
    pygame.draw.rect(screen, WHITE, shop_button)
    shop_text = font.render("Магазин", True, BLACK)
    inventory_text = font.render("Инвентарь", True, BLACK)
    screen.blit(inventory_text, (670, 260))
    screen.blit(shop_button_image, (shop_button.x, shop_button.y))
    screen.blit(well_image, well_rect)

    # Логика отображения инвентаря
    if inventory_visible:
        draw_inventory(screen, player.inventory, font, inventory_button)

    # Отображаем кнопки для выбора растений с изображениями
    screen.blit(corn_image, (corn_button.x, corn_button.y))
    screen.blit(potato_image, (potato_button.x, potato_button.y))
    screen.blit(carrot_image, (carrot_button.x, carrot_button.y))

    # Логика событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if shop_button.collidepoint(mouse_x, mouse_y):
                shop.open_shop(screen)  # Открытие магазина
            elif well_rect.collidepoint(mouse_x, mouse_y):
                player.collect_water()  # Сбор воды
            elif corn_button.collidepoint(mouse_x, mouse_y):
                player.selected_crop = 'Кукуруза'  # Выбор кукурузы
            elif potato_button.collidepoint(mouse_x, mouse_y):
                player.selected_crop = 'Картошка'  # Выбор картошки
            elif carrot_button.collidepoint(mouse_x, mouse_y):
                player.selected_crop = 'Морковка'  # Выбор морковки
            elif inventory_button.collidepoint(mouse_x, mouse_y):
                inventory_visible = not inventory_visible  # Переключение видимости инвентаря
            else:
                player.plant(mouse_x, mouse_y)  # Посадка растения

        # Полив при нажатии кнопки W
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            player.water_plant(mouse_x, mouse_y)

        # Сбор урожая при нажатии кнопки H
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            player.harvest_plant(mouse_x, mouse_y)

    player.draw(screen)  # Рисуем растения игрока

    # Отображение инвентаря
    player.draw_inventory(screen)

    # Отображение курсора мыши
    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.blit(cursor_image, (mouse_x, mouse_y))

    pygame.display.flip()  # Обновляем экран

pygame.quit()
