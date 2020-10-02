class piece:
   def __init__(self, piecetype, color):
      self.piecetype = piecetype
      self.color = color
      self.position = (1,2)
   def movepiece(self, origin, dest):
      pass
   def __str__(self):
      return self.color + " " + self.piecetype
   def __repr__(self):
      if self.piecetype == "knight":
         return "kn"
      else:
         return self.piecetype[0]
#
#temp = piece("king", "white")
#
#print(temp)
#print(temp.position)
#print(repr(temp))



#for moving bishops, for checking if it can move to the destination, |x2-x1| = |y2-y1| 
