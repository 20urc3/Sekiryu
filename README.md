# Sekiryu
## A python script that performs automatic decompilation and analysis of binary files with your prefered Decompiler and ChatGPT
                                     
Are you tired of your computer going "Beep Boop" and you don't understand it ? Let this lazy script help you while reverse engineering
binary, cracksme challenge, or the malware your lover wrote you.

### Version 
This script is a BETA version. The goal is to make it compatible with IDA, Binja, R2 and GDB. Lots of improvement have to be done, but
for the moment it is working and it's fun.

    This plugins is tested on Linux for the moment. However, nothing stop you to run it on Windows. 
    Only Ghidra is supported at the moment

### Requirements

To use this plugin, you will need the following:

    Python 3.6 or higher
    Python Pip (available at https://pypi.org/project/pip/)
    OpenAI Python API (available at https://github.com/openai/openai-python)

### Installation

    - pip download Sekiryu
    - Run the server on your machine, then the script ghidrai.py inside Ghidra.

### Usage

To use this plugin, simply run the server and open the binary file you wish to analyze in your prefered decompiler. Once the binary has been loaded, you can run the plugin.

The plugin will automatically connect to the OpenAI API to perform the decompilation and analysis. Once the process is complete, the plugin will create a file with the analysed and commented pseudo-code.

    To make the app work, you need to set the OpenAI API key (available at https://openai.com/api/) as the OPENAI_API_KEY environment variable.

### Headless mode

#### Ghidra

    ./analyzeHeadless GHIDRA_PROJECT_DIRECTORY -import YOUR_BINARY -postscript ghidrai.py


### Example 

##### Initial code:

```c
    _memset(local_34,0,0x30);                                         
    if (param_2 == 0x111) {                                            
      if (param_3 == 2) {                                             
        PostQuitMessage(0);                                        
      else {                    
        if (param_3 == 0x3e9) {                                      
          GetDlgItemTextA(hDlg_004142a0,1000,(LPSTR)local_34,0x30); 
          pcVar4 = "cr4ckingL3ssons";                                           
          pbVar2 = local_34;                                             
          do {                                        
            bVar1 = *pbVar2;                                             
            bVar5 = bVar1 < (byte)*pcVar4;                                         
            if (bVar1 != *pcVar4)
```
            
##### Analysed code:
```c
    _memset(localSerialKey, 0, 0x30); // Initializes localSerialKey buffer with 0.
    
    if (message == WM_COMMAND) { // Checks if the event is WM_COMMAND.
    if (event == 2) { // Checks if the event is a button click on the close button.
    PostQuitMessage(0); // Sends a WM_QUIT message to the window.
    else if (event == 0x3e9) { // Checks if the event is a button click on a button with control ID of 1001.
    GetDlgItemTextA(hDialogBox_004142a0, 1000, (LPSTR)localSerialKey, 0x30);  // Retrieves the text of the control with the given control ID.
    serialKey = "cr4ckingL3ssons";
    bytePtr = localSerialKey;
    do {
    currentByte = *bytePtr;
    comparisonResultBool = currentByte < (byte)*serialKey;
    if (currentByte != *serialKey)
```

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
    
# Warning
 
    The xmlrpc.server module is not secure against maliciously constructed data. If you need to parse 
    untrusted or unauthenticated data see XML vulnerabilities. 

For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
