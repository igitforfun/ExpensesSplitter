from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Workspace\expenses_splitter_GUI\Tkinter-Designer\output\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)  

class ExpensesApp(Tk):
    def __init__(self):
        super().__init__()
        self.title('Expenses Tracker')
        self.geometry("789x294")
        self.configure(bg = "#D1EDF9")
        self.p1 = Page1()
        self.p2 = Page2()
        self.pageIndex = 0
        self.pages = [Page1, Page2]
        # self.currentPage=self.pages[self.pageIndex]()
        self.currentPage = self.p1
    
    def nextpage(self):
        # self.pageIndex +=1
        # self.currentPage = self.pages[self.pageIndex]()
        self.currentPage = self.p2

class Page1(ExpensesApp):
    def __init__(self):
        self = Canvas(
            bg = "#D1EDF9",
            height = 294,
            width = 789,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.place(x = 0, y = 0)
        self.create_text(
            167.0,
            125.0,
            anchor="nw",
            text="How many participants?",
            fill="#000000",
            font=("AnonymousPro Regular", 14 * -1)
        )
        self.create_text(
            251.0,
            38.0,
            anchor="nw",
            text="Expenses Calculator",
            fill="#000000",
            font=("AnonymousPro Regular", 20 * -1)
        )
        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.create_image(
            390.5,
            134.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=359.0,
            y=121.0,
            width=63.0,
            height=24.0
        )
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png")
        )
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ExpensesApp().nextpage(),
            relief="flat"
        )
        self.button_1.place(
            x=351.0,
            y=199.0,
            width=80.0,
            height=39.0
        )

class Page2(ExpensesApp):
    def __init__(self):
        self = Canvas(
            bg = "#D1EDF9",
            height = 687,
            width = 789,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.place(x = 0, y = 0)
        self.create_text(
            251.0,
            38.0,
            anchor="nw",
            text="Expenses Calculator",
            fill="#000000",
            font=("AnonymousPro Regular", 20 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.create_image(
            233.5,
            284.5,
            image=self.entry_image_2
        )
        self.entry_2 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=24.0,
            y=82.0,
            width=419.0,
            height=403.0
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.create_image(
            610.5,
            284.0,
            image=self.entry_image_3
        )
        self.entry_3 = Text(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=462.0,
            y=81.0,
            width=297.0,
            height=404.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=285.0,
            y=565.0,
            width=109.0,
            height=44.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=407.0,
            y=565.0,
            width=109.0,
            height=44.0
        )
    
        
if __name__ == "__main__":
    app = ExpensesApp()
    app.mainloop()
