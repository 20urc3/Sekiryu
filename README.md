# GhidrAI
## A python script that performs automatic decompilation and analysis of binary files with Ghidra and ChatGPT

### Requirements

To use this plugin, you will need the following:

    Ghidra 9.2 or higher (available at https://ghidra-sre.org/)
    Python 3.6 or higher
    Python Pip for Ghidra (available at https://pypi.org/project/pip/)
    OpenAI Python API (available at https://github.com/openai/openai-python)

### Installation

    Clone this repository to your local machine
    Go to your Ghidra folder and go copy the python files..
    Open the script manager and run the script.

### Usage

To use this plugin, simply open Ghidra and open the binary file you wish to analyze. Once the binary has been loaded, you can run the plugin.

The plugin will automatically connect to the OpenAI API to perform the decompilation and analysis. Once the process is complete, the plugin will display the decompiled code and analysis results in a new window.

### Headless mode

    ./analyzeHeadless GHIDRA_PROJECT_DIRECTORY -import YOUR_BINARY -postscript ghidrai.py

### Acknowledgements

This plugin was created by 2ourc3 at Bushido Security as part of a research project. We would like to thank OpenAI for developing the ChatGPT language model and making it available to the research community.

For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
