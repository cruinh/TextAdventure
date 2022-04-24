from place import Place
from direction import *

from places.atrium import *
from places.hallway import *
from places.front_porch import *
from places.diningroom import *
from places.livingroom import *

from things.housekey import *

class World(object):
	def __init__(self):
		self.places = []

		self.atrium = Atrium(self)
		self.atrium.placeThing(HouseKey())
		self.hallway = Hallway(self)
		self.frontPorch = FrontPorch(self)
		self.diningroom = Diningroom(self)
		self.livingroom = Livingroom(self)
	
		self.atrium.addExit(North, self.frontPorch, True)
		self.atrium.addExit(West, self.livingroom)
		self.atrium.addExit(South, self.hallway)
		
		self.livingroom.addExit(West, self.diningroom)
		
	def describe(self):
		print("You find yourself in a World. The world has has many places:")
		for r in self.places:
			print("\t" + r.name)
			
