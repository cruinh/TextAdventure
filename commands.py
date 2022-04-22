from player import player

def examineCommand():
	player.location.describe()
	return True

def helpCommand(locationCmds):
	helpTxt = "Commands: (ex)amine, quit, help"
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

def commandHandler(cmd):	
	locationCmds = player.location.commands()
	
	if cmd == "examine" or cmd == "ex":
		return examineCommand()
	elif cmd == "quit":
		return quitCommand()
	elif cmd == "help":
		return helpCommand(locationCmds)
	elif cmd in locationCmds:
		return player.location.handleCommand(cmd, player)
	else:
		print("What do you mean by '"+ cmd + "'?")
		
	return True
