class telRec:
	#don't forget to fetch before you code!!!
	def __init__(self, dict):
		self.time = dict.get('Time')
		self.lat = dict.get('Latitude')
		self.long = dict.get('Longitude')
		self.course = dict.get('Course')
		self.alt = dict.get('Altitude')
		self.hum = dict.get('Humidity')
		self.temp = dict.get('Temperature')
		self.pressure = dict.get('Pressure')
		self.roll = dict.get('roll')
		self.pitch = dict.get('pitch')
		self.yaw = dict.get('yaw')
		self.x = dict.get('x')
		self.y = dict.get('y')
		self.z  = dict.get('z')
		self.speed = dict.get('Speed')
		self.FC = 0

	def __str__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nTime = {self.time}\nLatitude = {self.lat}\nLongitude = {self.long}\nCourse = {self.course}\n\
		Altitude = {self.alt}\nHumidity = {self.hum}\nTemperature = {self.temp}\nPressure = {self.pressure}\n \
		Roll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\nX = {self.x}\nY = {self.y}\nZ = {self.z}\n\
		Speed = {self.speed}\nFC = {self.FC}"
		return str
	def __repr__(self):
		str = "Telemetry Record: \n"
		str+= "--"*10 
		str += f"\nTime = {self.time}\nLatitude = {self.lat}\nLongitude = {self.long}\nCourse = {self.course}\n\
		Altitude = {self.alt}\nHumidity = {self.hum}\nTemperature = {self.temp}\nPressure = {self.pressure}\n \
		Roll = {self.roll}\nPitch = {self.pitch}\nYaw = {self.yaw}\nX = {self.x}\nY = {self.Y}\nZ = {self.z}\n\
		Speed = {self.speed}\nFC = {self.FC}"
		return str 

	
#the following methods are all similar, just for different attributes

	def setTime (self, time):
		self.time = time

	def setLatitude (self,lat):
		#dict['latitude'] = lat
		self.lat  = lat 

	def setLongitude (self, lon):	
		#telRec['longitude'] = lon
		self.lon  = lon

	def setCourse (self, course):
		self.course = course	

	def setAltitude (self,alt):
		#dict['altitude'] = alt
		self.alt = alt

	def setHumidity (self,hum):
		#dict['humidity'] = hum
		self.hum  = hum		

	def setTemperature (self,temp):
		#dict['temperature'] = temp
		self.temp  = temp

	def setPressure (self, pressure):
		self.pressure = pressure

	def setRoll (self,roll):
		#dict['roll'] = roll
		self.roll  = roll

	def setPitch (self,pitch):
		#dict['pitch'] = pitch
		self.pitch  = pitch

	def setYaw (self,yaw):
		#dict['yaw'] = yaw
		self.yaw = yaw 

	def setX (self, x):
		self.x = x

	def setY (self, y):
		self.y = y

	def setZ (self, z):
		self.z = z

	def setSpeed (self, speed):
		self.speed = speed

	def addFC (self,faultC):
		self.FC = faultC