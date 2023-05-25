class ChessPiece():
    def __init__(self, coord, colour) -> None:
        self.coord = coord
        self.colour = colour
    
    def move(self):
        pass

class Pawn(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
    
    def move(self):
        #move forward one or 2 or diagonally
        pass