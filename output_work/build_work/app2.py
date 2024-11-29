from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Workspace\expenses_splitter_GUI\Tkinter-Designer\output\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class ExpenseApp(Frame):
    def __init_(self, root):
        self.colour = 'WHITE'

        super().__init__(
            root,
            bg=self.colour
        )
        self.main_frame = self
        self.main_frame.pack(fill,tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0,weight=1)
        self.main_frame.rowconfigure(0, weight=1)

root = Tk()
root.title('Expenses App')
root.geometry('700x500')
app_instance= ExpenseApp(root)
root.mainloop()