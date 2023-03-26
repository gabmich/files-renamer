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

        path_label = toga.Label(
            "Path: ",
            style=Pack(padding=(0, 5))
        )
        self.path_input = toga.TextInput(style=Pack(flex=1))

        path_box = toga.Box(style=Pack(direction=ROW, padding=5))
        path_box.add(path_label)
        path_box.add(self.path_input)

        self.output = toga.MultilineTextInput(id='output',
                                              readonly=True)

        button = toga.Button(
            "Rename all files",
            on_press=self.rename,
            style=Pack(padding=5)
        )

        main_box.add(path_box)
        main_box.add(button)
        main_box.add(self.output)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def rename(self, widget):
        print(self.path_input.value)
        rename = RenameFiles(self.path_input.value)
        self.output.value = "\n".join(rename.list_and_rename_files()) # = self.path_input.value


def main():
    return Filesrenamer()
