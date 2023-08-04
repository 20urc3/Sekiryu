import os, subprocess, threading, time, readline

def get_ghidra_headless_path():
	ghidra_headless = os.environ.get('GHIDRA_HEADLESS_PATH')
	if not ghidra_headless:
		ghidra_headless = input("Please enter the path to Ghidra Headless folder: ")
		with open(os.path.expanduser("~/.bashrc"), "a") as f:
			f.write(f'\nexport GHIDRA_HEADLESS_PATH="{ghidra_headless}"')
		os.environ['GHIDRA_HEADLESS_PATH'] = ghidra_headless
	
	# Ensure the path ends with a slash
	if not ghidra_headless.endswith('/'):
		ghidra_headless += '/'
		
	return ghidra_headless

# Setting path
ghidra_path = get_ghidra_headless_path()

def exec_headless(file, script):
	"""
	Execute the headless analysis of ghidra
	"""
	path = ghidra_path + 'analyzeHeadless'
	# Setting variables
	tmp_folder = "/tmp/out"
	os.mkdir(tmp_folder)
	cmd = ' ' + tmp_folder + ' TMP_DIR -import'+ ' '+ file + ' '+ "-postscript "+ script +" -deleteProject"	

	# Running ghidra with specified file and script
	try:	
		p = subprocess.run([str(path + cmd)], shell=True, capture_output=True)
		os.rmdir(tmp_folder)

	except KeyError as e:
		print(e)
		os.rmdir(tmp_folder)


def decompiling(file):
	"""
	Execute the decompiling script
	"""

	try:
		# Setting script
		current_script_path = os.path.abspath(__file__)
		current_script_dir = os.path.dirname(current_script_path)
		script = os.path.join(current_script_dir, 'scripts', 'ghidra_decompiler.py')

	
		# Start the exec_headless function in a new thread
		thread = threading.Thread(target=exec_headless, args=(file, script))
		thread.start()
	
		# Animate the loading while waiting for the thread to finish
		animation = "|/-\\"
		idx = 0
		while thread.is_alive():
			print("Decompiling your binary... " + animation[idx % len(animation)], end="\r")
			idx += 1
			time.sleep(0.1)
	
		thread.join()

	except Exception as e:
		print(str(e))

	print("Binary successfully decompiled !")

def binexporting(file):
	"""
	Execute the decompiling script
	"""

	try:
		# Setting script
		current_script_path = os.path.abspath(__file__)
		current_script_dir = os.path.dirname(current_script_path)
		script = os.path.join(current_script_dir, 'scripts', 'bindiff_export.py')
	
		# Start the exec_headless function in a new thread
		thread = threading.Thread(target=exec_headless, args=(file, script))
		thread.start()
	
		# Animate the loading while waiting for the thread to finish
		animation = "|/-\\"
		idx = 0
		while thread.is_alive():
			print("BinExporting the binary..." + animation[idx % len(animation)], end="\r")
			idx += 1
			time.sleep(0.1)
		thread.join()

	except Exception as e:
		print(str(e))
	print("Successfully exported the binary with BinExport!")
