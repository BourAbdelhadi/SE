__author__ = "Bour Mohamed Abdelhadi"
__copyright__ = "Copyright (C) 2017 @Bour Mohamed Abdelhadi"
__version__ = "1.0"

import socket
import threading
import pickle
import sys

class Server():

	def __init__(self, host="127.0.0.1", port=8899):

		self.client = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((str(host), int(port)))
		self.sock.listen(10)
		self.sock.setblocking(False)

		t1 = threading.Thread(target=self.connecting)
		t2 = threading.Thread(target=self.processing)
		
		t1.daemon = True
		t1.start()

		t2.daemon = True
		t2.start()

		while True:
			message = raw_input('[+]If you want to exit the server type:algeria : -->')
			if message == 'algeria':
				self.sock.close()
				sys.exit()
			else:
				pass

	def send_messages_all(self, message, client):
		for i in self.client:
			try:
				if i != client:
					i.send(message)
			except:
				self.client.remove(i)

	def connecting(self):
		print("[+] Connected")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.client.append(conn)
			except:
				pass

	def processing(self):
		print("[+]Listening on port 8899 ... ")
		while True:
			if len(self.client) > 0:
				for i in self.client:
					try:
						data = i.recv(1024)
						if data:
							self.send_messages_all(data,i)
					except:
						pass
ser = Server()
