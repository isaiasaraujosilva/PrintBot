from os import system
import win32print
from Class_os import System
import win32api
from time import sleep
from Class_printer import Printer
#Colocar aqui o comando para o python Criar uma pasta
system=System
system.createFolder('imprimir')
printer=Printer
while True:
    #lista_arquivos = os.listdir(caminho_imp)
    #print(lista_arquivos[])
    print(system.fileList())
    if system.fileList() != []: 
        print(system.fileList)
        for i in system.fileList():
            print(i)
            #win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            printer.sendPrint(i)
            sleep(5)
            
            try:
                #os.remove(caminho_imp+'\\'+arquivo)
                system.remover(i)
            except PermissionError as erro:
               lista_arquivos = os.listdir(caminho_imp)
               while True:
                    sleep(5)
                    try:
                        os.remove(caminho_imp+'\\'+arquivo)
                    except:
                        while arquivo in lista_arquivos:
                           try:
                                os.remove(caminho_imp+'\\'+arquivo)
                                break
                           except PermissionError:
                               pass
                           lista_arquivos = os.listdir(caminho_imp) 
                        #if lista_arquivos[]==arquivo
                    
                                            
            sleep (5)
