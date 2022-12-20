#GhidrAI - An Integrated AI in Ghidra.
#@author 2ourc3 (www.bushido-sec.com)
#@category AI
#@keybinding 
#@menupath Tools.Ghidrai
#@toolbar Ghidrai


import openai
import os
import sys

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

... Starting Ghidrai, integrated AI script for Ghidra ...

''')

openai.api_key = "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"

def chat_gpt(string):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=string,
            max_tokens=3000,
            temperature=0.6,
            frequency_penalty=1,
            presence_penalty=1
            )
    except openai.OpenAIError as error:
        raise print(f"Error: {str(e)}")

    try:
        answer = response["choices"][0]["text"]
    except(KeyError, IndexError) as error:
        pass
    print(answer)


def get_funcs():
    func = getFirstFunction()
    funcList = []
    while func is not None:
        string =("Function:{} @ 0x{}".format(func.getName(), func.getEntryPoint()))
        func = getFunctionAfter(func)
        funcList.append(string) 
    funcs = str(funcList)
    return funcs

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


def decompiles_func():
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
