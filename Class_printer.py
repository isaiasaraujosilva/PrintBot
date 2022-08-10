import win32api
import win32print
#from Class_os import System
#system=System
#fileFolder=system.getMainFolder()

class Printer:
    
    def setImpEtiqueta(prtCodeEtiqueta):
        prtCodeEtiqueta=int(prtCodeEtiqueta)
        list_imp=win32print.EnumPrinters(2)
        imp=list_imp[prtCodeEtiqueta]
        win32print.SetDefaultPrinter(imp[2])
        return print('impressora de etiqueta selecionada: {}'.format(imp[2] ))

    def setImpA4(prtCodeA4):
        prtCodeA4=int(prtCodeA4)
        list_imp=win32print.EnumPrinters(2)
        imp2=list_imp[prtCodeA4]
        win32print.SetDefaultPrinter(imp2[2])
        win32print.OpenPrinter(imp2[2])
        return print('impressora de A4 selecionada: {}'.format(imp2[2] ))

    def getListPrinter():
        list_printer = win32print.EnumPrinters(2)
        return list_printer

    def sendPrint(file,fileFolder):
        try:
            win32api.ShellExecute(0, "print", file, None, fileFolder, 0)
            return print('Aquivo enviado para a impressora: {} '.format(file))
        except:
            return print("Erro: verifique o Foxit");


  