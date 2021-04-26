from curses import wrapper
from player import player
import sys

def main(scr):
    # Clear screen
	scr.clear()
	game_in_prog = 0
    scr.addstr("press any key to start")
    scr.getch()
    scr.clear()
	#while game_in_prog:
		
    for player in players:
        scr.addstr(str(player))

    stdscr.refresh()
    stdscr.getkey()
    
if __name__ == "__main__":
	time = sys.argv[1] #time in minutes per player
	players = []
	for name in sys.argv[2:]:
		players.append(player(name, int(time)))

	wrapper(main)
