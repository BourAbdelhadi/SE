__author__ = "Bour Mohamed Abdelhadi"
__copyright__ = "Copyright (C) 2017 @Bour Mohamed Abdelhadi"
__version__ = "1.0"

import socket
import threading
import pickle
import sys

print "Welcom Client ...\n"
print "if you want to exit the chat type : algeria\n"
person = raw_input("[+]Enter Your Username :")	

class Client():

	def __init__(self, host="127.0.0.1", port=8899):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((str(host), int(port)))

		receive_message = threading.Thread(target=self.receive_message)

		receive_message.daemon = True
		receive_message.start()

		while True:
			message = raw_input('-->')
			if message != 'algeria':
				self.send_message(message + " [+]Received from:" + person)
			else:
				self.sock.close()
				sys.exit()

	def receive_message(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send_message(self, message):
		self.sock.send(pickle.dumps(message))


cli = Client()