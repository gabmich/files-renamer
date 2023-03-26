"""
Files renamer app
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .controller import RenameFiles


class Filesrenamer(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.main_window = toga.MainWindow(title=self.formal_name)
        # selected_path = await self.main_window.select_folder_dialog(title='Choose a directory')

        path_label = toga.Label(
            "Path: ",
            style=Pack(padding=(0, 5))
        )
        self.path_input = toga.TextInput(style=Pack(flex=1))
        # self.path_input.value = selected_path

        path_box = toga.Box(style=Pack(direction=ROW, padding=5))
        path_box.add(path_label)
        path_box.add(self.path_input)

        self.output = toga.MultilineTextInput(id='output',
                                              readonly=True)

        button1 = toga.Button(
            "Select a folder",
            on_press=self.open_select_folder_dialog,
            style=Pack(padding=5)
        )

        button2 = toga.Button(
            "Rename all files",
            on_press=self.rename,
            style=Pack(padding=5)
        )

        main_box.add(button1)
        main_box.add(path_box)
        main_box.add(button2)
        main_box.add(self.output)

        self.main_window.content = main_box
        self.main_window.show()

    async def open_select_folder_dialog(self, widget):
        try:
            fname = await self.main_window.select_folder_dialog(
                title="Choose folder to work on", multiselect=False
            )
            if fname is not None:
                self.path_input.value = fname
        except ValueError:
            self.path_input.value = "Open file dialog was canceled"

    def rename(self, widget):
        print(self.path_input.value)
        rename = RenameFiles(self.path_input.value)
        self.output.value = "\n".join(rename.list_and_rename_files()) # = self.path_input.value


def main():
    return Filesrenamer()
