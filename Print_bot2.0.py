from os import system
import win32print
from Class_os import System
import win32api
from time import sleep

#Colocar aqui o comando para o python Criar uma pasta
System=System
System.createFolder('imprimir')
while True:
    #lista_arquivos = os.listdir(caminho_imp)
    #print(lista_arquivos[])
    print(System.fileList())
    if System.file() != []: 
        for arquivo in system.fileList():
            print(arquivo)
            win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            sleep(5)
            
            try:
                os.remove(caminho_imp+'\\'+arquivo)
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
