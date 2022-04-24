from player import player

class Thing():
	def __init__(self, name, description, owner=None):
		self.name = name
		self.description = description
		self.commands = []
		self.owner = owner
		
	def use(self, game):
		self.handleCommand("use", game)
	
	def commands(self):
		return self.commands
		
	def describe(self):
		print(self.description)
				
	def handleCommand(self, cmd, game):
		print("You " + cmd + " the " + self.name)
		
	def combineWith(self, otherThing):
		print("You combine the " + self.name + " with the " + otherThing.name)
		
	def handleCommand(self, cmd, arg, game):
		print(self.name + " doesn't know how to handle the command '" + cmd + "'")
		
