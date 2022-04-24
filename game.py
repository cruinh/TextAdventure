from player import *
from world import *

class Game (object):
	def __init__(self):
		self.player = Player()
		self.world = World()
			
		self.player.location = self.world.atrium
		
		self.temporaryCommandHandler = None
	
	def useCommand(self,thingName):
		things = self.player.inventory.contents
		thing = None
		for t in things:
			if t.name.lower() == thingName.lower():
				thing = t
				
		if thing is not None:
			thing.use(self)
		else:
			print("You don't have a " + thingName)
		return True
	
	def inventoryCommand(self):
		print("You are carrying:")
		for i in self.player.inventory.contents:
			print(i.name)
		return True
	
	def getCommand(self,thingName):
		things = self.player.location.inventory.contents
		thing = None
		for t in things:
			if t.name.lower() == thingName.lower():
				thing = t
		
		if thing is not None:
			self.player.inventory.add(thing)
			print("You get the " + thing.name)
		else:
			print("You don't see a " + thingName)
		return True
	
	def examineCommand(self):
		self.player.location.describe()
		return True
	
	def helpCommand(self,locationCmds):
		helpTxt = "Commands: (ex)amine, (g)et, (i)nventory, (u)se, (q)uit, (h)elp"
		if len(locationCmds) > 0:
			cmdsTxt = ""
			for c in locationCmds:
				cmdsTxt += ", " + c
			print(helpTxt + cmdsTxt)
		else:
			print(helpTxt)
		return True
			
	def quitCommand(self):
		print("Thanks for playing.")
		return False
	
	def commandHandler(self, cmd, arg):	
		if self.temporaryCommandHandler is not None:
			self.temporaryCommandHandler.handleCommand(cmd, arg, self)
		else:
			locationCmds = self.player.location.commands()
			
			cmd = cmd.lower()
			arg = arg.lower()
			
			if cmd == "examine" or cmd == "ex":
				return self.examineCommand()
			elif cmd == "i" or cmd == "inventory":
				return self.inventoryCommand()
			elif cmd == "get" or cmd == "g":
				return self.getCommand(arg)
			elif cmd == "use" or cmd == "u":
				return self.useCommand(arg)
			elif cmd == "quit" or cmd == "q":
				return self.quitCommand()
			elif cmd == "help" or cmd == "h":
				return self.helpCommand(locationCmds)
			elif cmd in locationCmds:
				return self.player.location.handleCommand(cmd, self)
			else:
				print("What do you mean by '"+ cmd + "'?")
			
		return True
