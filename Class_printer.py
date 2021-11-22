import win32api
import win32print
#from Class_os import System
#system=System
#fileFolder=system.getMainFolder()

class Printer:
    
    def getListPrinter():
        list_printer = win32print.EnumPrinters(2)
        return list_printer
    def sendPrint(file,fileFolder):
        win32api.ShellExecute(0, "print", file, None, fileFolder, 0)
        return print('Aquivo enviado para a impressora: {} '.format(file))
        
#definir impressora
#definir metodo de impressão 
