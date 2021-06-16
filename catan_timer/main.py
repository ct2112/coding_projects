from curses import wrapper
from player import player, game
import sys		

def main(scr):
    # Clear screen
	game.scr = scr
	game.setup()
	game.play()
	
if __name__ == "__main__":
	time_to_start_with = sys.argv[1] #time in minutes per player
	players = []
	for i, name in enumerate(sys.argv[2:]):
		players.append(player(name, int(time_to_start_with), i + 1 ))
	game = game(players)
	wrapper(main)
