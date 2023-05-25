class ChessPiece():
    def __init__(self, coord, colour) -> None:
        self.coord = coord
        self.colour = colour
    
    def move(self):
        pass

class Pawn(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "P"
    
    def move(self):
        pass

class Rook(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "R"
    
    def move(self):
        pass

class Knight(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "N"
    
    def move(self):
        pass

class Bishop(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "B"
    
    def move(self):
        pass

class Queen(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "Q"
    
    def move(self):
        pass

class King(ChessPiece):
    def __init__(self, coord, colour) -> None:
        super().__init__(coord, colour)
        self.name = "K"
    
    def move(self):
        pass