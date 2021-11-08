import win32print
import win32api
import os
from time import sleep
from pathlib import Path

#Colocar aqui o comando para o python Criar uma pasta
caminho= os.getcwd()+'\imprimir'
try:
    os.mkdir(caminho+'\\'+'imprimir')    
except:
    print('Pasta imprimir já existe') 
#lista_arquivos=os.listdir(caminho)
while 0==0:
    lista_arquivos = os.listdir(caminho)
    if lista_arquivos != []: 
        for arquivo in lista_arquivos:
            win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
            sleep(5)
            os.remove(caminho+'\\'+arquivo)
            sleep (5)