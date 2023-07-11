from player import player

class Thing():
	def __init__(self, names, description, owner=None):
		self.names = names
		self.description = description
		self.commands = []
		self.owner = owner

	def get_name(self):
		return self.names[0]
	
	name = property(get_name)
		
	def use(self, game):
		self.handleCommand("use", game)
	
	def commands(self):
		return self.commands
		
	def describe(self):
		print(self.description)
				
	def handleCommand(self, cmd, game):
		print("You " + cmd + " the " + self.names[0])
		
	def combineWith(self, otherThing):
		print("You combine the " + self.names[0] + " with the " + otherThing.names[0])
		
	def handleCommand(self, cmd, arg, game):
		print(self.name[0] + " doesn't know how to handle the command '" + cmd + "'")

	def respondsToName(self, aName):
		for n in self.names:
			if n.lower() == aName.lower():
				return True
		return False
		
