class Exit():
	def __init__(self, direction=None, destination=None, doorName="Door", locked=False):
		self.direction = direction
		self.destination = destination
		self.doorName = doorName
		self.locked = locked
		
	def use(self,player):
		if self.destination is not None:
			if self.locked == False:
				player.location = self.destination
				self.destination.describe()
			else:
				print("The door is locked.")
		else:
			print("This exit goes nowhere.")
