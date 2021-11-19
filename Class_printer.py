import win32api
from Class_os import System

system=System
fileFolder=system.getMainFolder()

class Printer:
    def sendPrint(file):
        win32api.ShellExecute(0, "print", file, None, fileFolder, 0)
        
#definir impressora
#definir metodo de impressão 
