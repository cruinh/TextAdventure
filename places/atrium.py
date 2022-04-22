from place import Place

class Atrium(Place):
	def __init__(self, world):
		Place.__init__(self,
			"Atrium",
			"You stand in a common atrium, suitable for a single-family home.",
			world)

