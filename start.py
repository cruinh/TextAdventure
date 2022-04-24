from sys import *
from game import *
from place import *
from player import player

def main():
	game = Game()
	
	print("Welcome. Type 'help' for a list of commands.\n")
	
	game.player.location.describe()
	
	while True:
		entry = input('\n--> ').split()
		cmd = entry.pop(0)
		arg = ' '.join(entry)

		if game.commandHandler(cmd, arg) == False:
			break
			
if __name__ == '__main__':
	main()
