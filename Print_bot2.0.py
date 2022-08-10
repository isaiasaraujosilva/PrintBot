from os import system
from Class_os import System
from time import sleep
from Class_printer import Printer
import win32print

system=System
system.createFolder('imprimir')
printer=Printer
print('Lista de impressoras instaladas no sistema:')
genCode=-1

for p in printer.getListPrinter():
    genCode=genCode+1
    p1=p 
    print(' ---> {} {}'.format(genCode,p1[2]))

prtCodeA4=input('Digite o numero da impressora de A4: ')
printer.setImpA4(prtCodeA4)
print('\n \n Em Execução...')

while True:  
    if system.fileList() != []: 
        for i in system.fileList():
            print(i)
            #win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            printer.sendPrint(i,system.getPrintFolder())
            print_jobs = win32print.EnumJobs(,0, -1, 1)
            print(print_jobs)
            sleep(5)    
            system.remover(i)
                        
           
            
