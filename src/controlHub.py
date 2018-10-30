from radio import Radio 
from commandBase import commandBase
from command import command 

def main():

	# initializes radio 
	radio = Radio() 
	#initializes command DataBase 
	cmdDB = commandBase()

	#constantly recieve data and store in command object and put in database
	# still have to take into consideration how duplicates commands will be handled 
	while(True): 
		message = radio.recieve()
		if(message != None):
			Newcommand = command(message) #convert data recieve into a command object 
			cmdDB.addCommand(comand)
