from inventory import *
from direction import *
from exit import Exit

class Place():
	def __init__(self, name, description, world):
		self.name = name
		self.description = description
		self.actors = []
		self.inventory = Inventory(self)
		self.exits = []
		world.places.append(self)
	
	def placeThing(self, thing, silently=True):
		if self.inventory.contains(thing):
			if silently == False:
				print(self.name + " already has the" + thing.name)
		else:
			if silently == False:
				print("You place the " + thing.name + " in the " + self.name)
			self.inventory.add(thing)
	
	def commands(self):
		result = []
		for i in self.exits:
			result.append(i.direction.abbreviation)
		return result
		
	def describe(self):
		print(self.description)

		numActors = len(self.actors)
		if numActors > 0:
			txt = ""
			for i in range(0, numActors):
				if i > 0:
					txt += ", "
				txt += self.actors[i].name
			print("\tYou see " + txt)

		numItems = len(self.inventory.contents)
		if numItems > 0:
			txt = ""
			for i in range(0, numItems):
				if i > 0:
					txt += ", "
				txt += "a " + self.inventory.contents[i].name
			print("\tYou see " + txt)
			
		numExits = len(self.exits)
		if numExits > 0:
			txt = ""
			for i in range(0,numExits):
				if i > 0:
					txt += ", "
				txt += self.exits[i].direction.name
			print("\tThere are " + str(numExits) + " exits to the " + txt)
			
	def addExit(self, 
		direction, 
		destination, 
		doorName="Door", 
		locked=False, 
		oneWay=False, 
		returnDoor="Door", 
		returnLocked=False):
			
		exit = Exit(direction, destination, doorName, locked)
		self.exits.append(exit)
		if oneWay == False:
			returnExit = Exit(reverseDirection(direction), self, returnDoor, returnLocked)
			destination.exits.append(returnExit)
	
	def handleCommand(self, cmd, player):
		for i in self.exits:
			if i.direction.abbreviation == cmd:
				print("You move to the " + i.direction.name + "\n")
				i.use(player)
				break
		return True
