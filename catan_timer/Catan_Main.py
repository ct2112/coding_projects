import curses
import sys	
from math import floor
import time
import threading	
import os


class player:
	def __init__(self, inp_name, init_time, inp_id, inp_color):
		self.name = inp_name
		self.time_left = init_time #time in seconds
		self.id  = inp_id
		self.active = 1
		self.color = inp_color
	def __str__(self):
		return "{:d}:{:12} - {:02d}:{:02d}".format(self.id, self.name,floor(self.time_left/60), floor(self.time_left%60))

class game:
	def __init__(self, inp_players):
		self.time_elapsed = 0
		self.cur_turn = 0
		self.cur_turn_time = 0
		self.orig_turn_time = 0
		self.num_turns = 0
		self.status= "NOT STARTED"
		self.in_progress = 0
		self.players = inp_players
		self.num_players = len(inp_players)

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

	def next_turn(self, it = 0):
		if it == self.num_players:
			self.in_progress = 0
			return
		self.cur_turn = (self.cur_turn + 1) % len(self.players)
		if self.cur_turn == 0:
			self.num_turns = self.num_turns + 1
		if self.players[self.cur_turn].active == 0:
			self.next_turn(it+1)

	def prev_turn(self, it = 0):
		if it == self.num_players:
			self.in_progress = 0
			return
		self.cur_turn = (self.cur_turn - 1)
		if self.cur_turn < 0:
			self.cur_turn = len(self.players) - 1
			self.num_turns = self.num_turns - 1
		if self.players[self.cur_turn].active == 0:
			self.prev_turn(it + 1)

	def play(self):
		disp_thread  = threading.Thread(target = self.display_func, daemon=True)
		timer_thread = threading.Thread(target = self.timer_func, daemon=True)
		input_thread = threading.Thread(target = self.input_func, daemon=True)
		self.in_progress = 1
		self.status = "RUNNING"
		disp_thread.start()
		timer_thread.start()
		input_thread.start()
		while self.in_progress:
			pass

	def display_func(self):
		game_start = int(time.time())
		while 1:
			self.scr.clear()
			time_elapsed = int(time.time()) - game_start
			self.scr.addstr(0,0, "total Time elapsed - {:d}:{:02d}\n".format(int(time_elapsed/60), time_elapsed % 60))
			self.scr.addstr("{}'s turn {:d}\n".format(self.players[self.cur_turn].name, self.num_turns))
			if self.status == "RUNNING":
				self.scr.addstr(self.status, curses.color_pair(GREEN_COLOR))
			else:
				self.scr.addstr(self.status, curses.color_pair(RED_COLOR))
	
			for player in self.players:
				if player.active:
					self.scr.addstr(player.id * 2 + 4, 0, str(player), curses.color_pair(player.color))
				else:
					self.scr.addstr(player.id * 2 + 4, 0, "XXXXX" + str(player) + "XXXXX", curses.color_pair(player.color))
			self.scr.refresh()
			time.sleep(1)

	def timer_func(self):
		prev_turn = 0
		self.orig_turn_time = self.players[0].time_left
		self.cur_turn_time = int(time.time())
		while 1:
			if prev_turn != self.cur_turn: #reset the values
				self.cur_turn_time = int(time.time())
				self.orig_turn_time = self.players[self.cur_turn].time_left
				prev_turn = self.cur_turn
			if self.status == "RUNNING":
				self.players[self.cur_turn].time_left = self.orig_turn_time - (int(time.time()) - self.cur_turn_time)
				if self.players[self.cur_turn].time_left <= 0: #remove player
					self.players[self.cur_turn].active = 0
					self.next_turn()
			time.sleep(1)

	def input_func(self):
		while 1:
			inp = self.scr.getch()
			if inp == 127:
				self.status = "PAUSED"
			elif inp == 97:
				self.prev_turn()
			elif inp == 100:
				self.next_turn()
			elif inp in [66, 115]:
				self.in_progress = 0
			elif self.status == "PAUSED":
				self.cur_turn_time = int(time.time())
				self.orig_turn_time = self.players[self.cur_turn].time_left
				self.status = "RUNNING"
			else:
				self.next_turn()
			time.sleep(.1)

if __name__ == "__main__":
	#os.system("pip3 install")
	time_to_start_with = float(sys.argv[1]) #time in minutes per player
	players = []
	BROWN_COLOR  = 1
	RED_COLOR 	 = 2
	GREEN_COLOR  = 3
	ORANGE_COLOR = 4
	WHITE_COLOR  = 5
	BLUE_COLOR 	 = 6
	DEFAULT_COLOR= 7
	for i, play in enumerate(sys.argv[2:]):
		name, color = play.split(',')
		color = color.lower()
		if color == "brown":
			color_code = BROWN_COLOR
		elif color == "green":
			color_code = GREEN_COLOR
		elif color == "red":
			color_code = RED_COLOR
		elif color == "orange":
			color_code = ORANGE_COLOR
		elif color == "white":
			color_code = WHITE_COLOR
		elif color == "blue":
			color_code = BLUE_COLOR
		else:
			print(color + "is not an acceptable color")
			print("Acceptable colors are brown, green, red, orange, white, blue and is case sensitive")
			sys.exit()
		players.append(player(name, int(time_to_start_with * 60), i + 1, color_code))
	game = game(players)
	game.scr = curses.initscr()
	curses.noecho()
	curses.start_color()


	curses.init_pair(RED_COLOR, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(GREEN_COLOR, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(WHITE_COLOR, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(BLUE_COLOR, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(ORANGE_COLOR, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(BROWN_COLOR, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(DEFAULT_COLOR, curses.COLOR_WHITE, curses.COLOR_BLACK)

	curses.cbreak()
	game.setup()
	game.play()
	curses.endwin()
