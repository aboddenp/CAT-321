from DataBases.commandBase import CommandBase
from Radio.radio import Radio
from DataBases.command import Command

def main():
	#initializes Radio and command dataBase 
	cmdDB = CommandBase()
	radio = Radio()
	#Setting up radio call back and initializing the internal dataBase 
	radio.setUP(cmdDB)

	while(True):
		try:
			#some code to run 
			radio.send("Hello there general kenobi")
			x = True
		except (KeyboardInterrupt):
			print("terminated")
			radio.terminate()
main()
