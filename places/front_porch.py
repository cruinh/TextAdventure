from place import Place

class FrontPorch(Place):
	def __init__(self, world):
		Place.__init__(self,
			"Front Porch",
			"You are on the front porch of the house.",
			world)
