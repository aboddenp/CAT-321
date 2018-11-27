class telemetryDB:

	def __init__(self, telemetry):
		self.telemetry = []
		self.recordCount = 0

	#We are adding an entire telemetry record each time and also incrementing our counter
	def addRecord(t):
		telemetry.append(telRec)
		recordCount += 1

	#this gets the total number of records, or our counter recordCount
	def getNumRec():
		return recordCount

	#this gives us the most recent record which is in the back of the list
	def getLastRecord():
		return telemetry(recordCount - 1)

	#this allows us to look at any record we want
	def getRecord(i):
		return telemetry(i)



