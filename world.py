from place import Place
from direction import *

from places.atrium import *
from places.hallway import *
from places.front_porch import *
from places.diningroom import *
from places.livingroom import *

from things.housekey import *

class World():
	def __init__(self):
		self.places = []
		
	def describe(self):
		print("You find yourself in a World. The world has has many places:")
		for r in theWorld.places:
			print("\t" + r.name)
			
theWorld = World()

atrium = Atrium(theWorld)
atrium.placeThing(HouseKey())
hallway = Hallway(theWorld)
frontPorch = FrontPorch(theWorld)
diningroom = Diningroom(theWorld)
livingroom = Livingroom(theWorld)
	
atrium.addExit(North, hallway)
atrium.addExit(West, livingroom)
atrium.addExit(East, frontPorch)
