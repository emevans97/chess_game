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
            'r': Rook(0, "black"),
            "n": Knight(0, "black"),
            "b": Bishop(0, "black"),
            "q": Queen(0, "black"),
            "k": King(0, "black"),
            "p": Pawn(0, "black"),
            'R': Rook(0, "white"),
            "N": Knight(0, "white"),
            "B": Bishop(0, "white"),
            "Q": Queen(0, "white"),
            "K": King(0, "white"),
            "P": Pawn(0, "white"),
            " ": " "}

    def setup(self):
        for count, row in enumerate(self.state):
            mapped_list = pd.Series(row).map(self.piece_dict)
            self.state[count] = mapped_list
        print(self.state)
    
    def print_board(self):
        for row in self.state:
            temp_row = []
            for piece in row:
                if piece != " ":
                    temp_row.append(piece.get_name())
                else:
                    temp_row.append(piece)
            print(temp_row)




