#!/usr/bin/env python
import threading

from .modules.cli import *
color_red = '\033[91m'

def main():
	try:		

		# Parse command + options
		main_thread = threading.Thread(target=core(parsing()))
		main_thread.start()
		main_thread.join()

	except KeyboardInterrupt:
		print(color_red + 'Keyboard Interrupt: Exiting.' + color_reset)

if __name__ == '__main__':
	main()
