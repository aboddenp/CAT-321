from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import serial 

# send data 
# questions to decide on 
# are we doing broadcast or unicast
# broadcast will send to all xbee devices
# unary will be one to one requires to instantiate a remoteXbee 
#  remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))
# use device.send_data(remote_device, data)

# synchronus: This means the method waits until the transmit status response is received
# asynchronous: application does not block during the transmit process. send_data_async()


#recieve data 

class Radio:
	def __init__(self):
		self.serialPort = "/dev/tty.SLAB_USBtoUART" # port where Xbee is connected find by doing ls /dev/tty* on terminal	
		self.device = XBeeDevice(self.serialPort,9600)
		self.remote_device = RemoteXBeeDevice(self.device, XBee64BitAddress.from_hex_string("0013A200406343f7")) # "0013A20040XXXXXX"


	def __repr__(self):
		return "Xbee Device at Port {0}\nopen = {1}".format(self.serialPort,self.device.is_open())
	def __str__(self):
		return "Xbee Device at Port {0}\nopen = {1}".format(self.serialPort,self.device.is_open())

	def openConnection(self):
		if (self.device.is_open() == False and self.device != None):
			self.device.open()
		
	

	def closeConnection(self):
		if (self.device.is_open() and self.device != None):
			self.device.close()
	

	def send(self, data):
		try:
			self.openConnection()
			#self.device.send_data_broadcast(data)
			self.device.send_data(self.remote_device,data)
			#self.device.send_data_async(remote_device,data)
		except : 
			print("something went wrong when sending data")
		finally:
			self.closeConnection()

	# def recieve(self): # data has to be a string or byte array
	# 	#try: 
	# 	print("waiting for data....")
	# 	self.openConnection()
	# 	#xbeeMessage = device.wait_read_frame()
	# 	xbeeMessage = self.device.read_data_from(self.remote_device)
	# 	print(xbeeMessage)
	# 	# should create a command class that will store the time stop and the data 
	# 	if (xbeeMessage != None):
	# 		printf(xbeeMessage.data)
	# 		return xbeeMessage.data;
	# 	#except:
	# 	#print("something went wrong when recieving data")
	# 	#finally: 
	# 	self.closeConnection()


	def setUP(self):

		self.device.open()

		def my_data_received_callback(xbee_message):
			address = xbee_message.remote_device.get_64bit_addr()
			data = xbee_message.data.decode("utf8")
			print("Received data from %s: %s" % (address, data))

		self.device.add_data_received_callback(my_data_received_callback)


	def terminate(self):
		self.closeConnection()


