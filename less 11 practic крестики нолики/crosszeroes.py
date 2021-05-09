# игра крестики нолики

from enum import Enum

import pygame

FPS = 60
CELL_SIZE = 50  # размер кристиков и ноликов

class Cell(Enum):
    """
    класс клетки для простоты наследуемся от Enum
    """
    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Класс игрока, содержащий тип значков и имя
    """

    def __init__(self, name, cell_type):
        self._name = name
        self._cell_type = cell_type


class GameField:
    def __init__(self):
        self._height = 3
        self._width = 3
        self.cells = [[Cell.VOID] * self._width for i in range(self._height)]


class GameFieldView:
    """
    виджет игрового поля, который отображает его на экране, а также выясняет место клика
    """

    def __init__(self, field_to_observe):
        # загразить картинки значков клеток
        # отобразить первичное сосотояние поля
        self._field = field_to_observe
        # размеры поля
        self._height = field_to_observe.height * CELL_SIZE
        self._width = field_to_observe.width * CELL_SIZE

        pass

    def draw(self):  # рисуем поле
        pass

    def check_coords_correct(self, x, y):  # проверяем правильность координат
        return True  # TODO: self._height учесть

    def get_coords(self, x, y):  # вычислить координаты
        return 0, 0  # TODO: реально вычислить

class GameRoundManager:
    """
    Менеджер игры,запускающий все процессы
    """

    def __init__(self, player1: Player, player2: Player):
        self._player = [player1, player2]
        self._current_player = 0
        self.field = GameField()  # создаем поле

    def handle_click(self, i, j):
        player = self._player[self._current_player]  # взять текущего игрока
        print("clock_handler", i, j)


class GameWindow:
    """
    содержит виджет поля, а также менежера игрорового раунда
    """

    def __init__(self):
        #  иницилизацпия pygame
        pygame.init()
        #  Window
        self._height = 800
        self._width = 600
        self._title = "Crosses and Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)

        player1 = Player(str(input()), Cell.CROSS)  # создаем игроков
        player2 = Player(str(input()), Cell.ZERO)  # создаем игроков
        self._game_manager = GameRoundManager(player1, player2)  # создаем менедженра раундов
        self._field_widget = GameFieldView(self._game_manager.field)  # вещи для создание поля

    def main_loop(self):  # главный цикл программы
        finished = False
        clock = pygame.time.Clock()  # пишем время до цикла
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:  # клик по полю
                    mouse_pos = pygame.mouse.get_pos()  # сохроняем координаты клика
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct(x, y):  # если координаты корретны
                        i, j = self._field_widget.get_coords(x, y)  # передаем их и вытаскиваем их в массиве
                        self._game_manager.handle_click(i, j)  # передаем это событие гейм менеджеру
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.main_loop()
    print("Game over!")


if __name__ == "__main__":
    main()
