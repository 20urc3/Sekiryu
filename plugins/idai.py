import idautils, idaapi 
import os, xmlrpc, subprocess, re, sys
from time import sleep
from xmlrpc.client import ServerProxy

def get_funcs():

    """
    Get all functions address 
    """
    
    start = ida_ida.cvar.inf.min_ea
    end = ida_ida.cvar.inf.max_ea
    # find first function head chunk in the range
    chunk = ida_funcs.get_fchunk(start)
    if not chunk:
        chunk = ida_funcs.get_next_fchunk(start)
    while chunk and chunk.start_ea < end and (chunk.flags & ida_funcs.FUNC_TAIL) != 0:
        chunk = ida_funcs.get_next_fchunk(chunk.start_ea)
    func = chunk

    while func and func.start_ea < end:
        startea = func.start_ea
        yield startea
        func = ida_funcs.get_next_func(startea)
           
           
def analyzing_binary():

    """
    Decompiles all functions, analyze it, generate
    comment and rename variable, export it in a text file
    """
    
    func_ea = get_funcs()
    for i in func_ea:
        funcs=idaapi.get_func(i)
        decompiled_code=idaapi.decompile(funcs)
        proxy.analyse_GPT(str(decompiled_code))
    print(done)

proxy = ServerProxy('http://localhost:13337')
analyzing_binary()
