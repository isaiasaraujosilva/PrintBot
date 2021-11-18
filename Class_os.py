import os
main_folder= os.getcwd()
folder_print=main_folder+'\\'+'imprimir'

class System:
    def createFolder(folder):
        try:
            os.mkdir(main_folder+'\\'+folder)
        except FileExistsError:
            return print('a Pasta imprimir já exite')
    def fileList():
        file=os.listdir(folder_print)
        return file
               