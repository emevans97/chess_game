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
            'r': Rook("black"),
            "n": Knight("black"),
            "b": Bishop("black"),
            "q": Queen("black"),
            "k": King("black"),
            "p": Pawn("black"),
            'R': Rook("white"),
            "N": Knight("white"),
            "B": Bishop("white"),
            "Q": Queen("white"),
            "K": King("white"),
            "P": Pawn("white"),
            " ": " "}

    def setup(self):
        for rowcount, row in enumerate(self.state):
            for col_count, piece in enumerate(self.state[rowcount]):
                mapped_list = pd.Series([piece]).map(self.piece_dict)
                self.state[rowcount] = mapped_list
                if piece != " ":
                    print([rowcount, col_count])
                    self.state[rowcount][col_count].coord = [rowcount, col_count]


    
    def print_board(self):
        for row in self.state:
            temp_row = []
            for piece in row:
                if piece != " ":
                    temp_row.append(piece.get_name())
                else:
                    temp_row.append(piece)
            print(temp_row)




