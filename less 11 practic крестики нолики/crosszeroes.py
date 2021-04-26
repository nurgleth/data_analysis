# игра крестики нолики

from enum import Enum

import pygame


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
    pass


class GameField:
    pass


class GameFieldView:
    pass


class GameRoundManager:
    """
    Менеджер игры,запускающий все процессы
    """

    def __init__(self, player1: Player, player2: Player):
        self._player = [player1, player2]
        self._current_player = 0
        self._field = GameField()  # создаем поле

    def handle_click(self):
        player = self._player[self._current_player]  # взять текущего игрока
        pass


class GameWindow:
    """
    содержит виджет поля, а также менежера игрорового раунда
    """

    def __init__(self):
        #  иницилизацпия pygame
        self._field_widget = GameFieldView  # вещи для создание поля
        player1 = Player(Cell.CROSS)  # создаем игроков
        player2 = Player(Cell.ZERO)  # создаем игроков
        self._game_manager = GameRoundManager(player1, player2)  # создаем менедженра раундов

    def main_loop(self):  # главный цикл программы
        finished = False
        while not finished:
            for event in pygame.ge:
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:  # клик по полю
                    x, y = event.x, event.y  # сохроняем координаты клика

                    if self._field_widget.check_coords_correct(x, y):  # если координаты корретны
                        i, j = self._field_widget(x, y)  # передаем их и вытаскиваем их в массиве
                        self._game_manager.handle_click(i, j)  # передаем это событие гейм менеджеру
