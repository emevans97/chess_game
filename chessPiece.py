class ChessPiece():
    def __init__(self, colour) -> None:
        self.colour = colour
        self.convert_name()
        self.coord = 0
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def convert_name(self):
        if self.colour == "black":
            self.set_name(self.name.lower())
    
    def move(self):
        pass

class Pawn(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "P"
        super().__init__(colour)
    
    def move(self):
        pass

class Rook(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "R"
        super().__init__(colour)
        
    
    def move(self):
        pass

class Knight(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "N"
        super().__init__(colour)
        
    
    def move(self):
        pass

class Bishop(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "B"
        super().__init__(colour)
        
    
    def move(self):
        pass

class Queen(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "Q"
        super().__init__(colour)
        
    
    def move(self):
        pass

class King(ChessPiece):
    def __init__(self, colour) -> None:
        self.name = "K"
        super().__init__(colour)
        
    
    def move(self):
        pass