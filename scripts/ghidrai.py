#GhidrAI - An Integrated AI in Ghidra.
#@author 2ourc3 (www.bushido-sec.com)
#@category AI
#@keybinding 
#@menupath Tools.Ghidrai
#@toolbar Ghidrai

##    results = subprocess.run(['python3', 'chat_gpt.py', message], capture_output=True)
##    return (results.stdout.decode('utf-8'))


import os
import sys
import subprocess
import re

from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor


print('''

 ,,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
                                     .$"
                                     "

... Starting Ghidrai, "Intelligent" script for Ghidra ...

''')

def get_global():
    infos = []
    state = getState()
    project = state.getProject()
    locator = project.getProjectData().getProjectLocator()
    projectMgr = project.getProjectManager()
    activeProject = projectMgr.getActiveProject()
    projectData = activeProject.getProjectData()
    rootFolder = projectData.getRootFolder()
    infos.append(str(state) + str(project) + str(locator) + str(projectMgr) + str(activeProject) + str(projectData))
    return infos


def get_funcs():
    func = getFirstFunction()
    funcList = []
    nameList = []
    entryList = []
    while func is not None:
        name = ("{}".format(func.getName()))
        entry_point = ("0x{}".format(func.getEntryPoint()))
        func = getFunctionAfter(func)
        nameList.append(str(name))
        entryList.append(str(entry_point))
    names = nameList
    entries = entryList
    return names, entries


def get_namedBlocks():
    blocks = currentProgram.getMemory().getBlocks()
    nameList = []
    for block in blocks:
        string=("Name: {}, Size: {}".format(block.getName(), block.getSize()))
        nameList.append(string)
    names = str(nameList)
    return names

def get_allXREF():
    func = getFirstFunction()
    xref = []
    while func is not None:
        entry_point = func.getEntryPoint()
        reference = getReferencesTo(entry_point)
        func = getFunctionAfter(func)
        xref.append(reference)
    xrefs = xref
    return xrefs


def get_decomp():
    program = getCurrentProgram()
    ifc = DecompInterface()
    ifc.openProgram(program)
    func = getFirstFunction()
    decompiled = []
    while func is not None:
        function = func
        results = ifc.decompileFunction(function, 0, ConsoleTaskMonitor())
        decompiled.append(str(results.getDecompiledFunction().getC()))
        func = getFunctionAfter(func)
    return decompiled

def cleaning_code(text):
    # Remove multi-line comments
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    # Replace undefined8 with 8bytesData
    text = re.sub(r'undefined8', '8bytesData', text)
    # Replace local_res with reservedStack_VAR
    text = re.sub(r'local_res', 'reservedStack_VAR', text)
    # Replace DAT_ with globalVar
    text = re.sub(r'DAT_', 'globalVar', text)
    # Replace local_ with localVar_
    text = re.sub(r'local_', 'localVar_', text)
    # Remove blank lines
    text = re.sub(r'\n(?=\n)', '', text)
    # Remove consecutive spaces
    text = re.sub(r'\s{5,}', ' ', text)
    # Remove consecutive tabs
    text = re.sub(r'\t+', '', text)
    return text

global_info = get_global()
funcs = get_funcs()
named_blocks = get_namedBlocks()
xrefs = get_allXREF()
decompiled_code = get_decomp()

def analyzing_binary():
    f = open("analysis.c", "a")
    for text in decompiled_code:
        text = cleaning_code(text)
        message = ("Modify the following code snippet by adding comment on how it works, change variable and function name for more understeable one: " + str(text))
        results = subprocess.run(['python3', 'chat_gpt.py', message], capture_output=True)
        f.write(results.stdout.decode('utf-8'))
    f.close()
    print("The binary file has been analysed and the report is waiting for you. \n")
    print('''

     ⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⣻⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡏⠦⣄⡀⠀⠀⠀⠀⢀⣴⠞⠁⡀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡇⠀⠈⠙⠲⣄⠀⢠⡾⠁⠀⡜⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⡇⠀⢢⡀⠀⠈⢷⣾⡇⠀⢀⡇⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⡀⠀⠉⢳⡄⠀⢿⡇⢀⠾⠁⢀⣾⣷⠶⠒⠲⠶⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⣤⡀⠀⢻⠀⣸⠑⠠⠤⢴⠟⠉⠀⠀⠀⢀⣀⠀⠈⠛⢦⡀
⠀⠀⠀⠀⣀⡤⠶⠒⠛⠛⠷⣦⠊⠁⠀⠀⠀⢸⡑⠲⠶⠖⠋⠁⠀⠀⣠⠶⠒⠛
⢤⡠⠴⠚⠁⠀⠀⠀⣀⣤⣤⡈⠃⠀⠀⠀⠀⡠⠛⢶⣤⣤⠤⠴⠖⠋⠁⠀⠀⠀
⠈⠓⢤⣀⠀⠐⠒⠉⠁⠀⢀⣤⡷⠒⠒⠄⣾⠀⡇⠀⠈⠙⢷⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠲⠶⠤⠶⠾⣿⠋⠀⣠⠖⠁⣿⡀⠻⣄⠀⠀⠈⢷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⢸⠃⠀⠀⣿⢷⡄⠈⠑⢆⠀⠸⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⠀⠀⣼⠏⠀⠙⠶⣄⡀⠀⠀⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢁⣠⠞⠁⠀⠀⠀⠀⠀⠉⠳⣴⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀
''')

analyzing_binary()
