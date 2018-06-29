from game.core_2048 import GameCore
from game.utils import char_to_direction


def print_2d(arr):
    for i in arr:
        print(i)


game = GameCore()
game.restart_game()
while True:
    print_2d(game.Board())
    stdin = input("Move:")
    direction = char_to_direction(stdin)
    if direction is None:
        continue

    game.try_move(direction)
