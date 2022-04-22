from place import Place

class Hallway(Place):
	def __init__(self, world):
		Place.__init__(self,
			"Hallway",
			"You find yourself in the main downstairs hallway of the house.",
			world)
