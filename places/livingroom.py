from place import Place

class Livingroom(Place):
	def __init__(self, world):
		Place.__init__(self,
			"Livingroom",
			"You are in the livingroom.",
			world)
