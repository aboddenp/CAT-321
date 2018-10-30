import queue

# commandBase is initialized with a radio object it needs to handle 
class commandBase: 

	def __init__(self): # should 
		#priority queue constructor gets a maximum size paramter, if 0 size can be infinity 
		self.queue = queue.PriorityQueue(0) #priority queue could be helpful certain commands should have higher priority
		#self.radio = radio

	def __repr__(self):
		return "Pending Commands: %s"%(self.queue.qsize())
	def __str__ (self):
		return "Pending Commands: %s"%(self.queue.qsize())

	def size(self):
		self.queue.qsize()

	# @param self object instance
	# @return commad to  do if empty returns None 
	def getCommand(self):
		if (self.size() > 0):
			return self.queue.get()
		else: 
			return None 
	# @param self object instance
	# @param command to add to database
	# @param wight the priority of the command 
	# @return true if command added succesfully 
	def addCommand(self,command):
		Queue.put_nowait(command.weight, command)
