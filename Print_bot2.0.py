from os import system
from Class_os import System
from time import sleep
from Class_printer import Printer
system=System
system.createFolder('imprimir')
printer=Printer
print('Lista de impressoras instaladas no sistema:')
genCode=-1
for p in printer.getListPrinter():
    genCode=genCode+1
    p1=p 
    print(' ---> {} {}'.format(genCode,p1[2]))
prtCode=input('Digite o numero da impressora de ETIQUETA: ')    
while True:  
    if system.fileList() != []: 
        for i in system.fileList():
            print(i)
            #win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            printer.sendPrint(i,system.getPrintFolder())
            sleep(5)
            system.remover(i)
            
           
            
