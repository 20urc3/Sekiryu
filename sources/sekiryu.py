#!/usr/bin/env python

from modules.cli import *
from modules.ghidra_pilot import *
from modules.server import *

def main():
	try:		
		# Start Server
		server_thread = XMLServerThread()
		server_thread.start()

		try:
			# Parse command + options 
			core(parsing())
		except Exception as e:
			pass

		# Exiting server
		server_thread.stop()
		server_thread.join()	

	except KeyboardInterrupt:
		print('Keyboard Interrupt: Exiting.')


if __name__ == '__main__':
	main()
