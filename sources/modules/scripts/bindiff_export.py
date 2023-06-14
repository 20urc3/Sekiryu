from com.google.security.binexport import BinExportExporter
from java.io import File
import os

addr_set = currentProgram.getMemory()
program_name = currentProgram.getName()
name = File(program_name + ".BinExport")
exporter = BinExportExporter() 
os.chdir("output")
exporter.export(name, currentProgram, addr_set, monitor)
