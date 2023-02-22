# GhidrAI
## A python script that performs automatic decompilation and analysis of binary files with Ghidra and ChatGPT

Are you tired of your computer going "Beep Boop" and you don't understand it ? Let this lazy script help you while reverse engineering
binary, cracksme challenge, or the malware your lover wrote you.

### Version 
        This plugins is only available on Linux for the moment.

### Requirements

To use this plugin, you will need the following:

    Ghidra 9.2 or higher (available at https://ghidra-sre.org/)
    Python 3.6 or higher
    Python Pip for Ghidra (available at https://pypi.org/project/pip/)
    OpenAI Python API (available at https://github.com/openai/openai-python)

### Installation

    Clone this repository to your local machine
    Go to your Ghidra Scripts folder and copy the python files..
    Open the script manager and run the script.

### Usage

To use this plugin, simply open Ghidra and open the binary file you wish to analyze. Once the binary has been loaded, you can run the plugin.

The plugin will automatically connect to the OpenAI API to perform the decompilation and analysis. Once the process is complete, the plugin will display the decompiled code and analysis results in a new window.

                To make the app work, you need to set the OpenAI API key as the OPENAI_API_KEY environment variable.

### Headless mode

    ./analyzeHeadless GHIDRA_PROJECT_DIRECTORY -import YOUR_BINARY -postscript ghidrai.py

### Acknowledgements

This plugin was created by 2ourc3 at Bushido Security as part of a research project. We would like to thank OpenAI for developing the ChatGPT language model and making it available to the research community.

### Exemple 
#### Initial code
    /* lpDialogFunc parameter of CreateDialogParamA
    */
    undefined4 lpDialogFunc_004010a0(undefined4 param_1,int param_2,short param_3)
    
    {
    byte bVar1;
    byte *pbVar2;
    uint uVar3;
    char *pcVar4;
    bool bVar5;
    byte local_34 [48];
      
    _memset(local_34,0,0x30);
    if (param_2 == 0x111) {
      if (param_3 == 2) {
        PostQuitMessage(0);
      }
      else {
        if (param_3 == 0x3e9) {
          GetDlgItemTextA(hDlg_004142a0,1000,(LPSTR)local_34,0x30);
          pcVar4 = "cr4ckingL3ssons";
          pbVar2 = local_34;
          do {
            bVar1 = *pbVar2;
            bVar5 = bVar1 < (byte)*pcVar4;
            if (bVar1 != *pcVar4)

#### Analysed code

    /* This function is a callback function used as lpDialogFunc parameter in the CreateDialogParamA API. 
    It is used to handle messages and events that are associated with the dialog box window. 
    The variable names are renamed to make them more meaningful.*/
    
    undefined4 handleDialogBoxEvents(undefined4 param_1, int message, short event)
    {
    byte currentByte;
    byte *bytePtr;
    uint comparisonResult;
    char *serialKey;
    bool comparisonResultBool;
    byte localSerialKey[48];
    
    _memset(localSerialKey, 0, 0x30); // Initializes localSerialKey buffer with 0.
    
    if (message == WM_COMMAND) { // Checks if the event is WM_COMMAND.
    if (event == 2) { // Checks if the event is a button click on the close button.
    PostQuitMessage(0); // Sends a WM_QUIT message to the window.
    }
    else if (event == 0x3e9) { // Checks if the event is a button click on a button with control ID of 1001.
    GetDlgItemTextA(hDialogBox_004142a0, 1000, (LPSTR)localSerialKey, 0x30); 
    // Retrieves the text of the control with the given control ID.
    serialKey = "cr4ckingL3ssons";
    bytePtr = localSerialKey;
    do {
    currentByte = *bytePtr;
    comparisonResultBool = currentByte < (byte)*serialKey;
    if (currentByte != *serialKey)
    
#### Accuracy - What ChatGPT says

    As an AI language model, I don't have a fixed percentage of accuracy in reviewing code. 
    The quality and accuracy of my responses depend on the input I receive and the knowledge I have been trained on.
      
    My responses are based on the patterns and information I have learned from analyzing vast amounts of text data. 
    While I am designed to provide helpful and informative responses, I may not always be able to provide a complete
    or accurate analysis of complex code or specialized domains.
    
    It's important to note that my responses should be used as guidance only, and any code should be thoroughly 
    reviewed and tested by experienced developers before it is used in a production environment.

For more information about Bushido Security, please visit our website: https://www.bushido-sec.com/.
