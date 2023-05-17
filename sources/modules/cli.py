import argparse, os, pathlib, time
import re, sys, threading

from modules.ghidra_pilot import *
from modules.report import *
from modules.pcode import *
from modules.vuln_search import *

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

	#Initiate Reporting subparser
	report_parser = parser.add_argument_group("Reporting options")
	#Reporting options
	report_parser.add_argument('-r', '--report', help="Generate a One Pager report", action="store_true")

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
	if args.file:
		print("File used: " + str(args.file))
		if os.path.isfile(args.file):
			print("This is a file")
			file_list = [str(args.file)]
		elif os.path.isdir(args.file):
			print("This is a directory")
			fList = os.listdir(args.file)
			file_list = [os.path.join(args.file, file) for file in fList]
	
	elif (args.file == None):
		# No file provided, exiting
		print("No file provided, mandatory. Now exiting")
		raise Exception

	if not os.path.exists("output"):
		os.makedirs("output")

	for file in file_list:

		if args.decompile:
			# Decompile the file provided
			thread1 = threading.Thread(target=decompiling(file,))
			thread1.start()
			thread1.join()
			
			if not args.GPT:
				# Generating the Pseudo-code file
				thread2 = threading.Thread(target=simple_source(file))
				thread2.start()
				thread2.join()
				
			elif args.GPT:
				# Generationg GPT commented Pseudo-code file
				thread3 = threading.Thread(target=gpt_source(file))
				thread3.start()
				thread3.join()

		if args.vul:
			# Vulnerability detection
			thread4 = threading.Thread(target=vuln_hunt())
			thread4.start()
			thread4.join()

		if args.vulgpt:
			# Vulnerability detection with ChatGPT
			print("Vulnerability hunting via ChatGPT")

		if args.mal:
			# Malware analysis 
			print("Malware analysis via Pattern Recognition and Behaviour Analysis")

		if args.malgpt:
			# Malware analysis with ChatGPT
			print("Malware analysis via ChatGPT")

		if args.report:
			# Generating the report	
			print("Generating the report.")
			thread6 = threading.Thread(target=report())
			thread6.start()
			thread6.join()

		if args.compile:
			# Attempt to compile the Pcode source file
			print("Compiling the pseudo source code generated")
