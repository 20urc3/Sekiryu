# GhidrAI
## A python script that performs automatic decompilation and analysis of binary files with your prefered Decompiler and ChatGPT
                                     
Are you tired of your computer going "Beep Boop" and you don't understand it ? Let this lazy script help you while reverse engineering
binary, cracksme challenge, or the malware your lover wrote you.

### Version 
    This plugins is tested on Linux for the moment. However, nothing stop you to run it on Windows. 

### Requirements

To use this plugin, you will need the following:

    Python 3.6 or higher
    Python Pip (available at https://pypi.org/project/pip/)
    OpenAI Python API (available at https://github.com/openai/openai-python)

### Installation

    pip install sekiryu

### Usage

To use this plugin, simply run the server and open the binary file you wish to analyze in your prefered decompiler. Once the binary has been loaded, you can run the plugin.

The plugin will automatically connect to the OpenAI API to perform the decompilation and analysis. Once the process is complete, the plugin will create a file with the analysed and commented pseudo-code.

    To make the app work, you need to set the OpenAI API key (available at https://openai.com/api/) as the OPENAI_API_KEY environment variable.

### Headless mode

#### Ghidra

    ./analyzeHeadless GHIDRA_PROJECT_DIRECTORY -import YOUR_BINARY -postscript ghidrai.py

### Acknowledgements

This plugin was created by 2ourc3 at Bushido Security as part of a research project. 
    
#### Accuracy - What ChatGPT says

    As an AI language model, I don't have a fixed percentage of accuracy in reviewing code. 
    The quality and accuracy of my responses depend on the input I receive and the knowledge I have been trained on.
      
    My responses are based on the patterns and information I have learned from analyzing vast amounts of text data. 
    While I am designed to provide helpful and informative responses, I may not always be able to provide a complete
    or accurate analysis of complex code or specialized domains.
    
    It's important to note that my responses should be used as guidance only, and any code should be thoroughly 
    reviewed and tested by experienced developers before it is used in a production environment.

For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
