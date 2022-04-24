from thing import Thing
from places.atrium import Atrium

class HouseKey(Thing):
	def __init__(self):
		Thing.__init__(self,
			"House Key",
			"An ordinary-looking house key.")
			
	def use(self, player):
		Thing.use(self, player)
		if (isinstance(player.location,Atrium)):
			print("You try the key in the front door.")
		else:
			print("The key doesn't seem to fit anything here.")
