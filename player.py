from inventory import *

class Player():
	def __init__(self):
		self.inventory = Inventory(self)
	
	def describeInventory(self):
		self.inventory.describe("You're holding")
		
	def getThing(self, thing):
		if self.inventory.contains(thing):
			print("You already have the" + thing.name)
		else:
			print("You grab the " + thing.name)
			self.inventory.add(thing)

player = Player()
