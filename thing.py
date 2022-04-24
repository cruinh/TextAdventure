from player import player

class Thing():
	def __init__(self, name, description, owner=None):
		self.name = name
		self.description = description
		self.commands = []
		self.owner = owner
		
	def use(self, player):
		self.handleCommand(use, player, player.location)
	
	def commands(self):
		return self.commands
		
	def describe(self):
		print(self.description)
				
	def handleCommand(self, cmd, player, location):
		print("You " + cmd + " the " + self.name)
		
	def combineWith(self, otherThing):
		print("You combine the " + self.name + " with the " + otherThing.name)
		
