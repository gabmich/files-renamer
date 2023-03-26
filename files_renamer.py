import os


class RenameFiles():
    """
    Rename files in a target directory as wanted
    """
    folder_path = ''
    files       = []

    def __init__(self, folder_path):
        self.check_folder(folder_path)

    def check_folder(self, folder_path):
        if os.path.exists(str(folder_path)) and os.path.isdir(str(folder_path)):
            self.folder_path = str(folder_path)
            self.get_folder_content()
        else:
            print('not a valid folder')

    def get_folder_content(self):
        self.files = os.listdir(self.folder_path)
        print('Il y a ', len(self.files), 'fichiers dans ce dossier.')



folder_path = input('Entrez le chemin du dossier cible : ')

a = RenameFiles(folder_path)
