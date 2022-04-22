from place import Place

class Diningroom(Place):
	def __init__(self, world):
		Place.__init__(self,
			"Diningroom",
			"You are in the diningroom of the house. The table is bare, the place settings from the last meal having been long swept away to the kitchen.  Lace curtains border the window on the exterior wall.",
			world)
