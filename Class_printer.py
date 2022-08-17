import win32api
import win32print
import time
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
            return print("Erro: verifique o Foxit")

    def print_job_checker():
        jobs = [1]
        while jobs:
            jobs = []
            for p in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL,
                                            None, 1):
                flags, desc, name, comment = p
                print(p)
                phandle = win32print.OpenPrinter(name)
                print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
                #print_jobs = win32print.EnumJobs(phandle, 0, -1, 1)
                if print_jobs:
                    jobs.extend(list(print_jobs))
                for job in print_jobs:
                    print ("printer name => " + name)
                    document = job["pDocument"]
                    print ("Document name => " + document)
                win32print.ClosePrinter(phandle)            
            time.sleep(5)
        return 0
            


    