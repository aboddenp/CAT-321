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
		self.FC = 0

	def __str__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nLatitude = {self.lat}\nLongitude = {self.long}\nAltitude = {self.alt}\n\
Temperature = {self.temp}\nHumidity = {self.hum}\n\
Roll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\nFC = {self.FC}"
		return str
	def __repr__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nLatitude = {self.lat}\nLongitude = {self.long}\nAltitude = {self.alt}\n\
Temperature = {self.temp}\nHumidity = {self.hum}\n\
Roll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\nFC = {self.FC}"
		return str 

	
#the following methods are all similar, just for different attributes

	def setLatitude (self,lat):
		#dict['latitude'] = lat
		self.lat  = lat 

	def setLongitude (self, lon):	
		#telRec['longitude'] = lon
		self.lon  = lon

	def setAltitude (self,alt):
		#dict['altitude'] = alt
		self.alt = alt

	def setTemperature (self,temp):
		#dict['temperature'] = temp
		self.temp  = temp
	
	def setHumidity (self,hum):
		#dict['humidity'] = hum
		self.hum  = hum
	
	def setRoll (self,roll):
		#dict['roll'] = roll
		self.roll  = roll

	def setPitch (self,pitch):
		#dict['pitch'] = pitch
		self.pitch  = pitch

	def setYaw (self,yaw):
		#dict['yaw'] = yaw
		self.yaw = yaw 

	def addFC (self,faultC):
		self.FC = faultC