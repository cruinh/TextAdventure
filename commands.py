from player import player

def inventoryCommand():
	print("You are carrying:")
	for i in player.inventory.contents:
		print(i.name)
	return True

def getCommand(thingName):
	things = player.location.inventory.contents
	thing = None
	for t in things:
		if t.name == thingName:
			thing = t
	
	if thing is not None:
		player.inventory.add(thing)
		print("You get the " + thing.name)
	else:
		print("You don't see a " + thingName)
	return True

def examineCommand():
	player.location.describe()
	return True

def helpCommand(locationCmds):
	helpTxt = "Commands: (ex)amine, get, (i)nventory, quit, help"
	if len(locationCmds) > 0:
		cmdsTxt = ""
		for c in locationCmds:
			cmdsTxt += ", " + c
		print(helpTxt + cmdsTxt)
	else:
		print(helpTxt)
	return True
		
def quitCommand():
	print("Thanks for playing.")
	return False

def commandHandler(cmd, arg):	
	locationCmds = player.location.commands()
	
	if cmd == "examine" or cmd == "ex":
		return examineCommand()
	elif cmd == "i" or cmd == "inventory":
		return inventoryCommand()
	elif cmd == "get":
		return getCommand(arg)
	elif cmd == "quit":
		return quitCommand()
	elif cmd == "help":
		return helpCommand(locationCmds)
	elif cmd in locationCmds:
		return player.location.handleCommand(cmd, player)
	else:
		print("What do you mean by '"+ cmd + "'?")
		
	return True
