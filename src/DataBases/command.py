class Command: 

	#initializes a command object the function of this class is still uknown 
	# ideas: This class could be responsible of decoding the commands we recieve from ground 
	# as well as map a command to a weight to be used in the priority queue 
	# ?? should the message itself include the priority of the command, or should the priorities be static 
	
	def __init__(self,XbeeMessage):
		#self.data = message.data
		self.code = XbeeMessage.data # still have to figure how commands will work 
		self.data = code.decode("utf8") # Command String 
		self.weight = self.calculateWeight()
		#self.timestamp = message.timestamp

	def calculateWeight(self):
		return 0 
	def getInstruction(self): 
		return self.data 