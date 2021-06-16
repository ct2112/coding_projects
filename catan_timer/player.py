from math import floor

class player:
	def __init__(self, inp_name, init_time, inp_id):
		self.name = inp_name
		self.time_left = init_time * 60 #time in seconds
		self.id  = inp_id
	def __str__(self):
		return "{:d}:{:12} - {:02d}:{:02d}".format(self.id, self.name,floor(self.time_left/60), floor(self.time_left%60))

class game:
	def __init__(self, inp_players, inp_scr):
		self.time_elapsed = 0
		self.cur_turn = 0
		self.cur_turn_time = 0
		self.in_progress = 0
		self.players = inp_players
		self.scr = inp_scr

	def start(self, scr):
		scr.clear()
		num_players = len(self.players)
		scr.addstr("there are {} players:\n".format(num_players))
		for i, play in enumerate(self.players):
			scr.addstr(i,0,"{}:{}".format(i, play))
		scr.addstr("\npress any key to start")
		scr.refresh()
		scr.getch()
		scr.clear()		
if __name__ == "__main__":		
	temp = player("casey", 15)
	print(temp)
