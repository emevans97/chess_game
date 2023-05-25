from chessPiece import Bishop, Pawn, King, Queen, Knight, Rook
import pandas as pd


class Board():
    def __init__(self):
        self.state = [["r", "n", "b", "q", "k", "b", "n", "r"],
                    ["p", "p", "p", "p", "p", "p", "p", "p"],
                    [" ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " ", " "],
                    ["P", "P", "P", "P", "P", "P", "P", "P"],
                    ["R", "N", "B", "Q", "K", "B", "N", "R"]]
        self.piece_dict = {
            'r': Rook(0, 0),
            "n": Knight(0, 0),
            "b": Bishop(0, 0),
            "q": Queen(0, 0),
            "k": King(0, 0),
            "p": Pawn(0, 0)}

    def setup(self):
        for count, row in enumerate(self.state):
            mapped_list = pd.Series(row).map(self.piece_dict)
            self.state[count] = mapped_list
        print(self.state)




