import numpy as np
from piece import piece 
#import ncurses 

class board:
   def __init__(self):
      self.board =  np.matrix([[piece("knight", "white") for i in range(8)] for j in range(7)], piece)

   def __str__(self):
      print( self.board)
      return ""
   def initBoard(self):
      self.board[0] = np.array([piece("Pawn", "white") for i in range(8)] )
      #self.board.item((1,1)) = [piece("Rook", "white") for i in range(8)]

tempy = board()
tempy.initBoard()
print(tempy)
print("----------------")
print(tempy.board[0])
print(type(tempy.board[1]))
