class telRec:

	def __init__(self, dict):
		self.lat = dict.get('Latitude')
		self.long = dict.get('Longitude')
		self.alt = dict.get('Altitude')
		self.temp = dict.get('Temperature')
		self.hum = dict.get('Humidity')
		self.roll = dict.get('Roll')
		self.pitch = dict.get('Pitch')
		self.yaw = dict.get('Yaw')
		FC = 0
	
#the following methods are all similar, just for different attributes

	def setLatitude (lat):
		dict['latitude'] = lat

	def setLongitude (lon):	
		telRec['longitude'] = lon	

	def setAltitude (alt):
		dict['altitude'] = alt

	def setTemperature (temp):
		dict['temperature'] = temp
	
	def setHumidity (hum):
		dict['humidity'] = hum
	
	def setRoll (roll):
		dict['roll'] = roll

	def setPitch (pitch):
		dict['pitch'] = pitch

	def setYaw (yaw):
		dict['yaw'] = yaw

	def addFC (faultC):
		FC = faultC