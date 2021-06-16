from curses import wrapper
from player import player, game
import sys
import time
from datetime import datetime
import threading
from math import floor

screen = 0
def display_thread(scr):

	game_start = int(time.time())
	while 1:
		scr.clear()
		time_elapsed = int(time.time()) - game_start
		scr.addstr(0,0, "total Time elapsed - {:d}:{:02d}".format(int(time_elapsed/60), time_elapsed % 60))
		for player in players:
			scr.addstr(player.id * 2, 0, str(player))
		scr.refresh()
		time.sleep(1)

def timer_func():
	prev_turn = game.cur_turn
	cur_turn_time = 0
	while 1:
		if prev_turn != game.cur_turn:
			cur_turn_time = int(time.time())

		players[game.cur_turn].time_left
		

def main(scr):
    # Clear screen
	game = game(players, scr)
	game.start()
	disp_thread = threading.Thread(target=display_thread, args=[scr])
	timer_thread= threading.Thread(target=timer_func)
	game_in_prog = 1
	scr.refresh()
	disp_thread.start()
	timer_thread.start()
	while game_in_prog:
		scr.getch()
		game.cur_turn = (game.cur_turn + 1) % len(players)

	
if __name__ == "__main__":
	time_to_start_with = sys.argv[1] #time in minutes per player
	players = []
	for i, name in enumerate(sys.argv[2:]):
		players.append(player(name, int(time_to_start_with), i + 1 ))
	
	wrapper(main)
