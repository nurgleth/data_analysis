# игра крестики нолики

from enum import Enum


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

    def main_loop(self):  # главный цикл программы
        while not game_over:
            player = self._player[self._current_player]  # взять текущего игрока


class GameWindow:
    """
    содержит виджет поля, а также менежера игрорового раунда
    """
    def __init__(self):
        #  иницилизацпия pygame
        pass
