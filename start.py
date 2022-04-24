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
		entry = input('\n--> ').split()
		cmd = entry.pop(0)
		arg = ' '.join(entry)

		if commandHandler(cmd, arg) == False:
			break
			
if __name__ == '__main__':
	main()
