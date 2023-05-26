# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from board import Board

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = Board()
    board.setup()
    board.print_board()
    print(board.state[0][2].coord)
    print(board.state[0][0] is board.state[0][7])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
