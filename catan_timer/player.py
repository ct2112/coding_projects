from math import floor
class player:
	def __init__(self, inp_name, init_time):
		self.name = inp_name
		self.time = init_time * 60 #time in seconds
	def __str__(self):
		return "{} - {:02d}:{:02d}".format(self.name,floor(self.time/60), self.time%60)
		
if __name__ == "__main__":		
	temp = player("casey", 15)
	print(temp)
