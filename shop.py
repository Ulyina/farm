#shop.py
import pygame

class Shop:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.Font(None, 36)
        self.items_to_buy = {
            "Кукуруза": 15,
            "Картошка": 5,
            "Морковка": 10
        }
        self.items_to_sell = {
            "Кукуруза": 20,
            "Картошка": 10,
            "Морковка": 15
        }
        self.money_icon = pygame.image.load("money.png")  # Загружаем иконку монеты
        self.money_icon = pygame.transform.scale(self.money_icon, (20, 20))  # Уменьшаем размер иконки

        # Загружаем изображение для кнопки "Назад"
        self.back_image = pygame.image.load("back.png").convert_alpha()
        self.back_image = pygame.transform.scale(self.back_image, (50, 50))  # Настраиваем размер изображения
        self.back_button_rect = self.back_image.get_rect(topleft=(50, 500))  # Позиция кнопки

    def draw(self, surface):
        # Фон магазина (пастельный желтый)
        surface.fill((255, 255, 204))

        # Заголовок
        title_text = self.font.render("Магазин", True, (0, 0, 0))
        surface.blit(title_text, (300, 50))

        # Отображение денег игрока
        surface.blit(self.money_icon, (300, 100))  # Отображаем иконку денег
        money_text = self.font.render(str(self.player.money), True, (0, 0, 0))
        surface.blit(money_text, (320, 100))  # Сместим текст чуть вправо от иконки

        # Покупка семян
        buy_title_text = self.font.render("Купить семена:", True, (0, 0, 0))
        surface.blit(buy_title_text, (100, 150))
        y_offset = 200
        for item, price in self.items_to_buy.items():
            buy_button = pygame.Rect(100, y_offset, 200, 40)
            pygame.draw.rect(surface, (0, 255, 0), buy_button)
            item_text = self.font.render(f"{item}: {price}", True, (0, 0, 0))
            surface.blit(item_text, (110, y_offset + 10))
            surface.blit(self.money_icon, (290, y_offset + 10))
            y_offset += 50

        # Продажа урожая
        sell_title_text = self.font.render("Продать урожай:", True, (0, 0, 0))
        surface.blit(sell_title_text, (400, 150))
        y_offset = 200
        for item, price in self.items_to_sell.items():
            sell_button = pygame.Rect(400, y_offset, 200, 40)
            pygame.draw.rect(surface, (255, 0, 0), sell_button)
            inventory_count = self.player.inventory.get(item, 0)  # Получаем количество из инвентаря
            item_text = self.font.render(f"{item}: {price}", True, (0, 0, 0))
            surface.blit(item_text, (410, y_offset + 10))
            surface.blit(self.money_icon, (590, y_offset + 10))
            y_offset += 50

        # Кнопка "Назад" (с изображением)
        surface.blit(self.back_image, self.back_button_rect)

    def buy_item(self, item_name):
        if item_name in self.items_to_buy:
            price = self.items_to_buy[item_name]
            if self.player.money >= price:
                self.player.money -= price
                if item_name in self.player.inventory:
                    self.player.inventory[item_name] += 1  # Увеличиваем количество семян
                else:
                    self.player.inventory[item_name] = 1  # Если ключа нет, создаем его

    def sell_item(self, item_name):
        if item_name in self.items_to_sell:
            price = self.items_to_sell[item_name]
            if self.player.inventory.get(item_name, 0) > 0:  # Проверяем наличие в инвентаре
                self.player.money += price
                self.player.inventory[item_name] -= 1

    def open_shop(self, screen):
        clock = pygame.time.Clock()
        running = True

        # Загрузка изображения курсора
        cursor_image = pygame.image.load("cursor.png").convert_alpha()
        cursor_image = pygame.transform.scale(cursor_image, (50, 50))  # Измените размер при необходимости

        pygame.mouse.set_visible(False)  # Скрыть системный курсор

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:  # Выход из магазина по нажатию клавиши B
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Проверяем нажатие на кнопку покупки
                    if pygame.Rect(100, 200, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.buy_item("Кукуруза")
                    elif pygame.Rect(100, 250, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.buy_item("Картошка")
                    elif pygame.Rect(100, 300, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.buy_item("Морковка")
                    # Проверяем нажатие на кнопку продажи
                    elif pygame.Rect(400, 200, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.sell_item("Кукуруза")
                    elif pygame.Rect(400, 250, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.sell_item("Картошка")
                    elif pygame.Rect(400, 300, 200, 40).collidepoint(mouse_x, mouse_y):
                        self.sell_item("Морковка")
                    # Проверяем нажатие на кнопку "Назад" (изображение)
                    elif self.back_button_rect.collidepoint(mouse_x, mouse_y):
                        running = False  # Закрытие магазина и возврат в главное окно

            self.draw(screen)

            # Отображение курсора мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(cursor_image, (mouse_x, mouse_y))  # Отображаем изображение курсора

            pygame.display.flip()
            clock.tick(60)
