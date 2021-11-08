import win32print
import win32api
import os
from time import sleep

# escolher qual impressora a gente vai querer usar
lista_impressoras = win32print.EnumPrinters(2)
impressora = lista_impressoras[3]
win32print.SetDefaultPrinter(impressora[2])

#mandar imprimir todos os arquivos de uma pasta
caminho = r"C:\Users\Isaias\OneDrive\Projetos\DesenvolvementoDeSoftware\Python\pythonProject\PrintBot\imprimir"
#spooler=r"C:\Windows\System32\spool\PRINTERS"
#lista_spooler=os.listdir(spooler)
#print(lista_spooler)
#print(lista_arquivos)
# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea
print('')
print('')
print('')
print('@@@@@@@@@@@@@@@@@@@> PRINT BOT BY ISAIAS  <@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('')
print('')
print('')
while 0==0:
    lista_arquivos = os.listdir(caminho)
    if lista_arquivos != []: 
        for arquivo in lista_arquivos:
            win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
            sleep(5)
            os.remove(caminho+'\\'+arquivo)
            sleep (5)