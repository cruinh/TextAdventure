
class Inventory():
	def __init__(self, owner):
		self.owner = owner
		self.contents = []
	
	def add(self, thing):
		if thing.owner is not None and thing.owner.inventory is not None:
			thing.owner.inventory.remove(thing)
		self.contents.append(thing)
		thing.owner = self.owner
		
	def remove(self,thing):
		if thing.owner == self.owner:
			thing.owner == None
		self.contents.remove(thing)
		
	def contains(self, thing):
		return thing in self.contents
		
	def describe(self, prefix=""):
		description = prefix
		if len(prefix) > 0:
			description += " "
			
		for i in range(0,len(contents)):
			if i > 0:
				description += ", "
			description += self.contents[i].name
			
		print(description)
		
			
