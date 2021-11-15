import win32print
import win32api
import os
from time import sleep
from pathlib import Path

#Colocar aqui o comando para o python Criar uma pasta
caminho= os.getcwd()
caminho_imp=caminho+'\\'+'imprimir'

try:
    os.mkdir(caminho_imp)
    print('Criando pasta Imprimir')    
except:
    print('Pasta imprimir já existe') 
#lista_arquivos=os.listdir(caminho)
while 0==0:
    lista_arquivos = os.listdir(caminho_imp)
    if lista_arquivos != []: 
        for arquivo in lista_arquivos:
            print(arquivo)
            win32api.ShellExecute(0, "print", arquivo, None, caminho_imp, 0)
            sleep(5)
            try:
                os.remove(caminho_imp+'\\'+arquivo)
            except PermissionError as erro:
                sleep(10)
                os.remove(caminho_imp+'\\'+arquivo)
            sleep (5)
            