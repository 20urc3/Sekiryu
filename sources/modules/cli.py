import argparse, os, pathlib, time, webbrowser
import re, sys, threading

from .modules.ghidra_pilot import *
from .modules.report import *
from .modules.pcode import *
from .modules.vuln_search import *
from .modules.server import *

def open_html_file(file_path):
    webbrowser.open(file_path)


def parsing():
	"""
	CLI Menu using argparse
	"""

	#Initiate argparse and arguments
	parser = argparse.ArgumentParser(description='', add_help=False, usage="sekiryu [-f FILE] [OPTIONS]")
	parser.add_argument('-f','--file', help='The file to analyse',type=str)
	parser.add_argument('-v','--version', action='version', help="Show program's version number and exit.")
	parser.add_argument('-h','--help', action='help', default=argparse.SUPPRESS, help="Show this help message and exit.")

	#Initiate decompiler subparser
	decompiler_parser = parser.add_argument_group("Decompling options")
	#Decompiler options
	decompiler_parser.add_argument('-d', '--decompile', help="Decompilation of the folder/file", action="store_true")

	#Initiate Analysis subparser
	analysis_parser = parser.add_argument_group("Analysis options")
	#Analysis options
	analysis_parser.add_argument('-g','--GPT', help='ChatGPT Analysis', action="store_true")
	analysis_parser.add_argument('-vx','--vul', help='Vulnerability Hunting via Pattern Recognition', action="store_true")
	analysis_parser.add_argument('-vgpt','--vulgpt', help='Vulnerability Hunting via ChatGPT', action="store_true")
	analysis_parser.add_argument('-m','--mal', help='Malware Analysis', action="store_true")
	analysis_parser.add_argument('-mgpt','--malgpt', help='Malware Analysis via ChatGPT', action="store_true")
	analysis_parser.add_argument('-be', '--binEx', help="Exporting with BinDiff", action="store_true")

	#Initiate source generating parser
	compiling_parser = parser.add_argument_group("Source generating options")
	#Source generating options
	compiling_parser.add_argument('-c', '--compile', help='Attempt to compile the source code generated', action="store_true")

	parsed = parser.parse_args()
	return parsed

def core(args):
	"""
	Core module of the CLI. Responsible to start the action with the options set by the User.
	"""
	
	if (args.file is None):
		# No file provided, exiting
		print("No file provided, mandatory. Now exiting")
		pass

	else:

		# Start Server
		server_thread = XMLServerThread()
		server_thread.start()

		if os.path.isfile(args.file):
			print("File used: "+ str(args.file))
			file_list = [str(args.file)]

		elif os.path.isdir(args.file):
			print("File used: "+ str(args.file))
			fList = os.listdir(args.file)
			file_list = [str(args.file) + '/'+str(element) for element in fList]

		if not os.path.exists("output"):
			os.makedirs("output")

		for file in file_list:

			if args.binEx:
				# Exporting file with BinDiff
				thread10 = threading.Thread(target=binexporting(file))
				thread10.start()
				thread10.join()
			
			if args.decompile:
				# Decompile the file provided
				thread1 = threading.Thread(target=decompiling(file))
				thread1.start()
				thread1.join()
				
				os.chdir("output")

				if  args.GPT:
					# Generating the Pseudo-code file
					thread2 = threading.Thread(target=gpt_source(file))
					thread2.start()
					thread2.join()

				else:
					# Generating GPT commented Pseudo-code file
					thread3 = threading.Thread(target=simple_source(file))
					thread3.start()
					thread3.join()

				thread9 = threading.Thread(target=report())
				thread9.start()
				thread9.join()

				if args.vul:
					# Vulnerability detection
					thread4 = threading.Thread(target=vuln_hunt())
					thread4.start()
					thread4.join()

				if args.vulgpt:
					# Vulnerability detection with ChatGPT
					thread5 = threading.Thread(target=vuln_gpt(file))
					thread5.start()
					thread5.join()
	
				if args.mal:
					# Malware analysis
					pass 
		
				if args.malgpt:
					# Malware analysis with ChatGPT
					thread7 = threading.Thread(target=mal_gpt(file))
					thread7.start()
					thread7.join()
			
				if args.compile:
					# Attempt to compile the Pcode source file
					thread8 = threading.Thread(target=compile())
					thread8.start()
					thread8.join()


				# Open Report
				html_file_path = str(os.getcwd())+"/report.html"
				open_html_file(html_file_path)	
				
			# Exiting server
			server_thread.stop()
			server_thread.join()
