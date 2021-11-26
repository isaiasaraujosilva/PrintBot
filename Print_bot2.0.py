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
prtCodeEtiqueta=input('Digite o numero da impressora de ETIQUETA: ')
printer.setImpEtiqueta(prtCodeEtiqueta)
prtCodeA4=input('Digite o numero da impressora de A4: ')
printer.setImpA4(prtCodeA4)
print('\n \n Em Execução...')
while True:  
    if system.fileList() != []: 
        for i in system.fileList():
            print(i)
            #win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            if i == 'hd.pdf':
                printer.setImpEtiqueta(prtCodeEtiqueta)
                sleep(2)
                printer.sendPrint('hd_inservivel.pdf',system.getMainFolder())
                sleep(2)
                printer.setImpA4(prtCodeA4)
                printer.sendPrint(i,system.getPrintFolder())
            else:   
                printer.sendPrint(i,system.getPrintFolder())
                sleep(5)
            sleep(5)    
            system.remover(i)
            
           
            
