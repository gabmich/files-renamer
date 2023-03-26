import os
from datetime import datetime


class RenameFiles():
    """
    Rename files in a target directory with file's modification date
    """
    folder_path = ''
    files       = []
    DATE_FORMAT = '%Y-%m-%d'

    def __init__(self, folder_path):
        self.check_folder(folder_path)

    def check_folder(self, folder_path):
        # chef if folder_path exists and ensure that it's a valid directory
        if os.path.exists(str(folder_path)) and os.path.isdir(str(folder_path)):
            self.folder_path = str(folder_path)
            self.get_folder_content()
            # self.list_and_rename_files()
        else:
            print('not a valid folder')

    def get_folder_content(self):
        # get files in target folder
        # excludes all folders and hidden files
        files_and_dirs  = os.listdir(self.folder_path)
        self.files      = [f for f in files_and_dirs if (os.path.isfile(f'{self.folder_path}/{f}') and not f.startswith('.'))]
        print('There are', len(self.files), 'files in this directory.')

    def timestamp_to_datetime(self, file_full_path):
        # try to transform timestamp to a datestring
        # date string formatting given in self.FORMAT
        timestamp = os.path.getmtime(file_full_path)

        try:
            return datetime.fromtimestamp(timestamp).strftime(self.DATE_FORMAT)
        except Exception as e:
            print('Error in the file\'s modification date : not a valid timestamp')
            return ''

    def list_and_rename_files(self):
        # list all files in choosen directory and rename them with FORMAT date at the beginning
        output = []

        for filename in self.files:
            dt           = self.timestamp_to_datetime(f'{self.folder_path}/{filename}')
            new_filename = f"{dt}_{filename}"
            print(new_filename)
            output.append(new_filename)
            # os.rename(f'{self.folder_path}/{filename}', f'{self.folder_path}/{new_filename}')
            # output.append(f'{self.folder_path}/{new_filename}')

        return output
