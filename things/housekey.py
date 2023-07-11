from thing import Thing
from places.atrium import Atrium

class HouseKey(Thing):
	def __init__(self):
		Thing.__init__(self,
			["House Key", "Key"],
			"An ordinary-looking house key.")
			
	def use(self, game):
		if isinstance(game.player.location,Atrium):
			print("Which door do you want to use the key in?")
			game.temporaryCommandHandler = self
		else:
			print("The key doesn't seem to fit anything here.")
			
	def handleCommand(self, cmd, arg, game):
		game.temporaryCommandHandler = None
		
		cmd = cmd.lower()
		exit = game.player.location.getExit(cmd)
		
		if exit is not None:
			if exit.direction.name == "North":
				print("You attempt to unlock the door to the north")
				if exit.locked:
					print("The key turns in the lock and you hear a click.")
					exit.locked = False
				else:
					print("It's already unlocked.")
			else:
				print("The key doesn't fit in that lock")
		else:
			print("There's no door in that direction")
		
