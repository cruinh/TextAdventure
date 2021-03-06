class Direction():
	def __init__(self, name, abbreviation):
		self.name = name
		self.abbreviation = abbreviation
		
	def equals(self, otherDirection):
		if isinstance(otherDirection, Direction):
			if self.name == otherDirection.name or self.abbreviation == otherDirection.abbreviation:
				return True
		else:
			if self.name == otherDirection or self.abbreviation == otherDirection:
				return True
		return False
		
North = Direction("North", "n")
South = Direction("South", "s")
East = Direction("East", "e")
West = Direction("West", "w")
Northwest = Direction("Northwest", "nw")
Northeast = Direction("Northeast", "ne")
Southwest = Direction("Southwest", "sw")
Southeast = Direction("Southeast", "se")

def reverseDirection(dir):
	if dir == North:
		return South
	elif dir == South:
		return North
	elif dir == West:
		return East
	elif dir == East:
		return West
	elif dir == Northwest:
		return Southeast
	elif dir == Southeast:
		return Northwest
	elif dir == Northeast:
		return Southwest
	elif dir == Southwest:
		return Northeast
