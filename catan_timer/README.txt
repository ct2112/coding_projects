Pre-run:
	Ensure that the Catan_Timer executable is in the same library as the Lib folder
	
Starting the program:
    To run the catan timer, run the following command
    ./Catan_Timer <time> [<player_name>,<player_color>]
    	where:
    	<time> is the abount of time in minutes for each player
    	[<player_name>,<player_color>] is a list separated by spaces of name,color pairs
		Acceptable colors are brown, green, red, orange, white, blue and is case sensitive
    
    ex. 1
    	./Catan_Timer 10 Casey,brown Zeb,red Dante,blue
    		creates a 10 minute game (each player has 10 minutes) with order 1. Casey 2. Zeb 3. Dante
    
Controls:
once the game has been started, press any key to start

Backspace 		- pause the game, can be unpaused by pressing any other key
A		  		- go back a player
D		  		- next player
S or arrow down - end the game
Any other key	- next turn
