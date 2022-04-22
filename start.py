from sys import *
from world import *
from player import *
from place import *
from direction import *
from commands import *
from player import player

def main():
	print("Welcome. Type 'help' for a list of commands.\n")
	
	player.location = atrium
	player.location.describe()
	
	while True:
		cmd = input('\n--> ')
		if commandHandler(cmd) == False:
			break
			
if __name__ == '__main__':
	main()
