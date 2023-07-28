import serial
import time
import json

class Robot_hard:
	def __init__(self, porrobot, path, compass):
		self.por = porrobot
		self.path = path[0]
		self.ber = path[1]
		self.compass = compass
		self.u = {}
		self.u["vl"] = 0
		self.u["vr"] = 0
		self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
		
	def move_h(self):
		print("theta_taget:",self.ber[0])
		if self.compass <= self.ber[0] - 10:
			self.u["vl"] = 0.05
			self.u["vr"] = -0.05
			
		elif self.compass >= self.ber[0] + 10:
			self.u["vl"] = -0.05
			self.u["vr"] = 0.05
			
		elif  self.ber[0] - 10 <= self.compass <= self.ber[0] + 10:
			self.u["vl"] = 0.1
			self.u["vr"] = 0.1
			
		if len(self.path[0]) == 0 :
			self.u["vl"] = 0
			self.u["vr"] = 0
		
		sendtroll = json.dumps(self.u)
		bytes_troll = sendtroll.encode('ascii')
		self.ser.write(bytes_troll + b"\n")
		time.sleep(1)
		
def port_controll():
	ser = serial.Serial('/dev/ttyACM0', 115200, timeout= 1)
	ser.reset_input_buffer()
		
		
