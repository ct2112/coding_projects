from math import floor
import time
import threading

class player:
	def __init__(self, inp_name, init_time, inp_id):
		self.name = inp_name
		self.time_left = init_time * 60 #time in seconds
		self.id  = inp_id
	def __str__(self):
		return "{:d}:{:12} - {:02d}:{:02d}".format(self.id, self.name,floor(self.time_left/60), floor(self.time_left%60))

class game:
	def __init__(self, inp_players):
		self.time_elapsed = 0
		self.cur_turn = 0
		self.cur_turn_time = 0
		self.num_turns = 0
		self.in_progress = 0
		self.players = inp_players

	def setup(self):
		self.scr.clear()
		num_players = len(self.players)
		self.scr.addstr("there are {} players:\n".format(num_players))
		for i, play in enumerate(self.players):
			self.scr.addstr(i,0,"{}".format(play))
		self.scr.addstr("\npress any key to start")
		self.scr.refresh()
		self.scr.getch()
		self.scr.clear()

	def play(self):
		disp_thread  = threading.Thread(target = self.display_thread, daemon=True)
		timer_thread = threading.Thread(target = self.timer_func, daemon=True)
		self.in_progress = 1

		disp_thread.start()
		timer_thread.start()
		while self.in_progress:
			#if self.scr.getch() == KEY_BACKSPACE:
			#	self.in_progress = 0
			#	self.scr.getch()
			#	self.in_progress = 1
			self.scr.getch()
			self.cur_turn = (self.cur_turn + 1) % len(self.players)
			if self.cur_turn == 0:
				self.num_turns = self.num_turns + 1
		
	def display_thread(self):
		game_start = int(time.time())
		while 1:
			self.scr.clear()
			time_elapsed = int(time.time()) - game_start
			self.scr.addstr(0,0, "total Time elapsed - {:d}:{:02d}\n".format(int(time_elapsed/60), time_elapsed % 60))
			self.scr.addstr("{}'s turn {:d}".format(self.players[self.cur_turn].name, self.num_turns))
			for player in self.players:
				self.scr.addstr(player.id * 2 + 1, 0, str(player))
			self.scr.refresh()
			time.sleep(1)

	def timer_func(self):
		prev_turn = 0
		orig_turn_time = self.players[0].time_left
		cur_turn_time = int(time.time())
		while 1:
			if prev_turn != self.cur_turn:
				cur_turn_time = int(time.time())
				orig_turn_time = self.players[self.cur_turn].time_left
				prev_turn = self.cur_turn
			self.players[self.cur_turn].time_left = orig_turn_time - (int(time.time()) - cur_turn_time)
			time.sleep(1)
				
if __name__ == "__main__":		
	temp = player("casey", 15)
	print(temp)
