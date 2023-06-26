# Sekiryu v0.0.2

This Ghidra Toolkit is a comprehensive suite of tools designed to streamline and automate various tasks associated with running Ghidra in Headless mode. This toolkit provides a wide range of scripts that can be executed both inside and alongside Ghidra, enabling users to perform tasks such as Vulnerability Hunting, Pseudo-code Commenting with ChatGPT and Reporting with Data Visualization on the analyzed codebase. It allows user to load and save their own script and interract with the built-in API of 
the script.

## Key Features

- **Headless Mode Automation**: The toolkit enables users to seamlessly launch and run Ghidra in Headless mode, allowing for automated and batch processing of code analysis tasks.

- **Script Repository/Management**: The toolkit includes a repository of pre-built scripts that can be executed within Ghidra. These scripts cover a variety of functionalities, empowering users to perform diverse analysis and manipulation tasks. It allows users to load and save their own scripts, providing flexibility and customization options for their specific analysis requirements. Users can easily manage and organize their script collection.

- **Flexible Input Options**: Users can utilize the toolkit to analyze individual files or entire folders containing multiple files. This flexibility enables efficient analysis of both small-scale and large-scale codebases.

### Available scripts

- **Vulnerability Hunting**: Leverage the toolkit's scripts to identify potential vulnerabilities within the codebase being analyzed. This helps security researchers and developers uncover security weaknesses and proactively address them.

- **Automatic Pseudo Code Generating**: Automatically generate pseudo code within Ghidra's Headless mode. This feature assists in understanding and documenting the code logic without manual intervention.

- **Pseudo-code Commenting with ChatGPT**: Enhance the readability and understanding of the codebase by utilizing ChatGPT to generate human-like comments for pseudo-code snippets. This feature assists in documenting and explaining the code logic.

- **Reporting and Data Visualization**: Generate comprehensive reports with visualizations to summarize and present the analysis results effectively. The toolkit provides data visualization capabilities to aid in identifying patterns, dependencies, and anomalies in the codebase.



  
## Pre-requisites

Before using this project, make sure you have the following software installed:

- Ghidra: You can download Ghidra from the National Security Agency's GitHub repository @  https://github.com/NationalSecurityAgency/ghidra
- Java: Make sure you have Java Development Kit (JDK) version 17 or higher installed. You can download it from the OpenJDK website @ https://openjdk.org/projects/jdk/17/
- BinExport (OPTIONNAL) Follow the instruction for installing the Ghidra Extension https://github.com/google/binexport
- SemGrep (OPTIONNAL) Follow the instruction detailed https://semgrep.dev/docs/getting-started/

## Installation

- Install the pre-requisites mentionned above.
- Download Sekiryu release directly from Github or use: `pip install sekiryu`.

## Usage
In order to use the script you can simply run it against a binary with the options that you want to execute.
- `sekiryu [-F FILE][OPTIONS]`

Please note that performing a binary analysis with **Ghidra** (or any other product) is a relatively *slow* process. Thus, expect the binary analysis to take several minutes depending on the host performance.
If you run Sekiryu against a very large application or a large amount of binary files, be prepared to **WAIT**

## Demos
- Find demo on www.bushido-sec.com

## API
    
    The "server.py" is basically built to allow scripts to interract with Ghidra each other and with the host system. 
    An User can easily develop their own script, load and saved it in the script folder and use the known functions 
    of the API to interract with Ghidra.    
In order to use it the User must import xmlrpc in their script and call the function like for example: `proxy.send_data`
#### Functions
  - **send_data()** - Allows user to send data to the server. ("data" is a Dictionnary)
  - **recv_data()** - Allows user to receive data from the server. ("data" is a Dictionnary)
  - **request_GPT()** - Allows user to send string data via ChatGPT API.

### Use your own scripts
Scripts are saved in the folder /modules/scripts/ you can simply copy your script there.
In the `ghidra_pilot.py` file you can find the following function which is responsible to run a headless ghidra script:

```python
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
```
The usage is pretty straight forward, you can create your own script then just add a function in the `ghidra_pilot.py` such as:
```python
def yourfunction(file):
	try:
		# Setting script
		script = "modules/scripts/your_script.py"
	
		# Start the exec_headless function in a new thread
		thread = threading.Thread(target=exec_headless, args=(file, script))
		thread.start()
		thread.join()
	except Exception as e:
		print(str(e))
```
The file `cli.py` is responsible for the command-line-interface and allows you to add argument and command associated like this:
```python
analysis_parser.add_argument('[-ShortCMD]', '[--LongCMD]', help="Your Help Message", action="store_true")
```
## Contributions

- **Scripts/SCRIPTS/SCRIIIIIPTS**: This tool is designed to be a toolkit allowing user to save and run their own script easily, obviously if you can contribue in any sort of script (anything that is interesting will be approved !)
-  **Optimization**: Any kind of optimization are welcomed and will almost automically be approved and deployed every release, some nice things could be: improve parallel tasking, code cleaning and overall improvement.
- **Malware analysis**: It's a big part, which i'm not familiar with. Any malware analyst willing to contribute can suggest idea, script, or even commit code directly in the project.
-  **Reporting**: I ain't no data visualization engineer, if anyone is willing to improve/contribue on this part, it'll be very nice.
-  **Installation/Setup**: It would be really nice to allow an user to simply download the pip package and run a setup that does everything, install ghidra, all dependencies, Ghidrathon, etc. Any help appreciated.

# Warning
 
    The xmlrpc.server module is not secure against maliciously constructed data. If you need to parse 
    untrusted or unauthenticated data see XML vulnerabilities.

# Special thanks
    A lot of people encouraged me to push further on this tool and improve it. Without you all this project wouldn't have been
    the same so it's time for a proper shout-out:
    - @JeanBedoul @McProustinet @MilCashh @Aspeak @mrjay @Esbee|sandboxescaper @Rosen @Cyb3rops @RussianPanda @Dr4k0nia
    - @Inversecos @Vs1m @C5pider @djinn @corelanc0d3r @ramishaath @chompie1337
    Thanks for your feedback, support, encouragement, test, ideas, time and care.
For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
