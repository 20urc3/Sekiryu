#!/usr/bin/env python
import threading

from modules.cli import *

def main():
	try:		

		# Parse command + options
		main_thread = threading.Thread(target=core(parsing()))
		main_thread.start()
		main_thread.join()

	except KeyboardInterrupt:
		print('Keyboard Interrupt: Exiting.')

if __name__ == '__main__':
	main()
