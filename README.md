# Sekiryu v0.0.2

This Ghidra Toolkit is a comprehensive suite of tools designed to streamline and automate various tasks associated with running Ghidra in Headless mode. This toolkit provides a wide range of scripts that can be executed both inside and alongside Ghidra, enabling users to perform tasks such as Vulnerability Hunting, Pseudo-code Commenting with ChatGPT and Reporting with Data Visualization on the analyzed codebase. It allows user to load and save their own script and interract with the built-in API of 
the script.

## Key Features

- **Headless Mode Automation**: The toolkit enables users to seamlessly launch and run Ghidra in Headless mode, allowing for automated and batch processing of code analysis tasks.

- **Script Repository**: The toolkit includes a repository of pre-built scripts that can be executed within Ghidra. These scripts cover a variety of functionalities, empowering users to perform diverse analysis and manipulation tasks.

- **Vulnerability Hunting**: Leverage the toolkit's scripts to identify potential vulnerabilities within the codebase being analyzed. This helps security researchers and developers uncover security weaknesses and proactively address them.

- **Automatic Pseudo Code Generating**: Automatically generate pseudo code within Ghidra's Headless mode. This feature assists in understanding and documenting the code logic without manual intervention.

- **Pseudo-code Commenting with ChatGPT**: Enhance the readability and understanding of the codebase by utilizing ChatGPT to generate human-like comments for pseudo-code snippets. This feature assists in documenting and explaining the code logic.

- **Reporting and Data Visualization**: Generate comprehensive reports with visualizations to summarize and present the analysis results effectively. The toolkit provides data visualization capabilities to aid in identifying patterns, dependencies, and anomalies in the codebase.

- **Script Management**: The toolkit allows users to load and save their own scripts, providing flexibility and customization options for their specific analysis requirements. Users can easily manage and organize their script collection. A very simple collection of API functions allow user to develop their own Ghidra script solution with Sekiryu.

- **Flexible Input Options**: Users can utilize the toolkit to analyze individual files or entire folders containing multiple files. This flexibility enables efficient analysis of both small-scale and large-scale codebases.

  
## Pre-requisites

Before using this project, make sure you have the following software installed:

- Ghidra: You can download Ghidra from the National Security Agency's GitHub repository @  https://github.com/NationalSecurityAgency/ghidra
- Ghidrathon: Get the Ghidrathon plugin from the mandiant GitHub repository @ https://github.com/mandiant/Ghidrathon
- Java: Make sure you have Java Development Kit (JDK) version 17 or higher installed. You can download it from the OpenJDK website @ https://openjdk.org/projects/jdk/17/

## Installation

- Install the pre-requisites mentionned above.
- Download Sekiryu release directly from Github or use: `pip install sekiryu`.

## Usage
In order to use the script you can simply run it against a binary with the options that you want to execute.
- `sekiryu [-F FILE][OPTIONS]`

Please note that performing a binary analysis with **Ghidra** (or any other product) is a relatively *slow* process. Thus, expect the binary analysis to take several minutes depending on the host performance.
If you run Sekiryu against a very large application or a large amount of binary files, be prepared to **WAIT**

## Tutorial
- Installation

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

## Contributions

- **Optimization**: Any kind of optimization are welcomed and will almost automically be approved and deployed every release, some nice things could be: improve parallel tasking, code cleaning and overall improvement.
- **Malware analysis**: It's a big part, which i'm not familiar with. Any malware analyst willing to contribute can suggest idea, script, or even commit code directly in the project.
-  **Reporting**: I ain't no data visualization engineer, if anyone is willing to improve/contribue on this part, it'll be very nice.
-  **Installation/Setup**: It would be really nice to allow an user to simply download the pip package and run a setup that does everything, install ghidra, all dependencies, Ghidrathon, etc. Any help appreciated.

# Warning
 
    The xmlrpc.server module is not secure against maliciously constructed data. If you need to parse 
    untrusted or unauthenticated data see XML vulnerabilities.

# Special thanks
    A lot of people encouraged me to push further on this tool and improve it. Without you all this project wouldn't have been 
    the same so it's time for a proper shout-out: @JeanBedoul @McProustinet @MilCashh @Aspeak @mrjay @Esbee|sandboxescaper @Rosen @Cyb3rops @RussianPanda 
    @Dr4k0nia @Inversecos @C5pider @djinn @corelanc0d3r @ramishaath @chompie1337 
    Thanks for your feedback, support, encouragement, test, ideas, time and care.
    
For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
