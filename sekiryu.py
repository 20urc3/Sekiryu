import sys, os, subprocess, threading, time

"""
	ghidraPath = os.getenv("GHIDRA_PATH")
	idaPath = os.getenv("IDAT_PATH")
	binjaPath = os.getenv("BINJA_PATH")
"""

class core:
	def __init__(self):
		self.ghidraPath="/path/to/ghidra"
		self.idaPath="/path/to/ida"
		self.binjaPath="/path/to/binja"
		self.ghidraPLUGIN="/ghidraPLUGIN"
		self.idaPLUGIN="/ghidraPLUGIN"
		self.BINARY="binary"
		self.reportFILE="report"
		self.vulnPLUGIN="/vulnPLUGIN"
		self.vuln_GPT_PLUGIN="/vuln_GPT_PLUGIN"
		self.mal_GPT_PLUGIN="/mal_GPT_PLUGIN"

	def analyse_ghidra(self):
		"""
		Analysing with Ghidra
		"""
		os.startfile(self.ghidraPath + self.ghidraPLUGIN + self.BINARY)

	def analyse_IDA(self):
		"""
		Analysing with Ghidra
		"""
		os.startfile(self.idaPath + self.idaPLUGIN + self.BINARY)

	def analyse_binja(self):
		"""
		Analysing with Ghidra
		"""
		os.startfile(self.binjaPath + self.binjaPLUGIN + self.BINARY)

	def vuln_search(self):
		"""
		Analysing with Ghidra
		"""
		os.startfil(self.reportFILE + self.vulnPLUGIN)

	def vuln_GPT(self):
		"""
		Analysing with Ghidra
		"""
		os.startfil(self.reportFILE + self.vuln_GPT_PLUGIN)

	def mal_GPT(self):
		"""
		Analysing with Ghidra
		"""
		os.startfil(self.reportFILE + self.mal_GPT)

	def exiting(self):
		subprocess.Popen.kill()
		exit()

	def main_menu(self):
		"""
		Choosing menu
		"""
		print("""
----------------------------------------------
|                    MENU                    |
----------------------------------------------
| 1. Analyse with Ghidra                     |
| 2. Analyse with IDA                        |
| 3. Analyse with Binja                      |
| 4. Search for vulnerabilities              |
| 5. Search for vulnerabilities with ChatGPT |
| 6. Malware analysis with ChatGPT           |
| 0. Exit                                    |
----------------------------------------------
""")



def running():
	"""
	Running the tool
	"""
	run = core()


	choices = {
    '1': run.analyse_ghidra,
    '2': run.analyse_IDA,
    '3': run.analyse_binja,
    '4': run.vuln_search,
    '5': run.vuln_GPT,
    '6': run.mal_GPT,
    '0': run.exiting
	}

	run.main_menu()

	while True:
		try:
			subprocess.Popen(['python', '-m', 'server'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		except KeyboardInterrupt:
			run.exiting()
			
		choice = input("\nEnter your choice:")
		if choice not in choices:
			print("Invalid choice. Please enter a valid option")
			continue
		choices[choice]()

running()
