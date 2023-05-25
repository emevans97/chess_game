Board as embedded list
Pieces are objects
Pieces can have attribute position - coord on board, colour, 
method move - different for each piece
Piece has a master class - each different piece inherits from this - inherits piece and colour attribute but has different move method etc.
Board class handles things like printing out the state of the board