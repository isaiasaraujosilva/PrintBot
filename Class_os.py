import os
main_folder= os.getcwd()
folder_print=main_folder+'\\'+'imprimir'

class System:
    def getMainFolder():
            return main_folder
    def getPrintFolder():
        return folder_print        
    def createFolder(folder):
        try:
            os.mkdir(main_folder+'\\'+folder)
        except FileExistsError:
            return print('a Pasta imprimir já exite')
    def fileList():
        file=os.listdir(folder_print)
        return file
    def fileCout():
         cout=len(os.listdir(folder_print))
         return cout
    def remover(deleteFile):
      try:
        os.remove(folder_print+'\\'+deleteFile)
      except PermissionError:
          while PermissionError:
                try:
                    os.remove(folder_print+'\\'+deleteFile)
                    break  
                except PermissionError:
                        pass
                           
    #return print('Arquivo deletado: {}'.format(deleteFile))      