from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress
import serial 

# make other folders visible: 
import sys
sys.path.append('../')

# our own modules: 
from DataBases.commandBase import commandBase
from DataBases.command import command

# send data 
# questions to decide on 
# are we doing broadcast or unicast
# broadcast will send to all xbee devices
# unary will be one to one requires to instantiate a remoteXbee 
#  remote_device = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A20040XXXXXX"))
# use device.send_data(remote_device, data)

# synchronus: This means the method waits until the transmit status response is received
# asynchronous: application does not block during the transmit process. send_data_async()

#The idea for the callback is to add the command to the command database every time a message is recieved 

#This code will be run when an xbee_message has been recieved 

commandDB = commandBase()

def my_data_received_callback(xbee_message):
	address = xbee_message.remote_device.get_64bit_addr()
	data = xbee_message.data.decode("utf8")

	#store the XBbee into a command object for decoding etc...
	command = command(xbee_message)
	# add this command to the command dataBase
	commandDB.addCommand(command)


	print(xbee_message.data)
	print("Received data from %s: %s" % (address, data))

#recieve data 

class Radio:
	#commandDB where all commands will be stored 

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




	# opens the xbee device and sets the recieve call back 
	# parameters: database = command database to store commands 
	def setUP(self):
		self.device.open()
		self.device.add_data_received_callback(my_data_received_callback)

	#close xbeeconnection and delete callback 
	def terminate(self):
		self.device.del_data_received_callback(my_data_received_callback)
		self.closeConnection()


# testing using a main 
def main():
	radio = Radio() 
	radio.setUP()
	print("1 to stop")
	x = 0
	while(x == 0):
		x = int(input())
	print("done")
	radio.terminate()

main() 

