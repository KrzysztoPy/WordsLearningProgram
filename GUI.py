from tkinter import *
from Logic import Logic


class MainWindow(Logic):
    def __init__(self):
        self.logic = Logic

    root = Tk()
    add_words = None
    start_learning = None
    add_words_pop = None

    def main_menu(self):
        self.root.title("Words learning")
        self.root.geometry(self.set_main_pop(335, 75))
        self.root.resizable(width=False, height=False)
        self.set_buttons()
        self.root.mainloop()

    def set_main_pop(self, window_width, window_height) -> str:
        # Set size view window
        window_width = 335
        window_height = 75
        # Set center position
        position_right = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def set_buttons(self):
        self.add_words = Button(self.root, text="Add new words list", bd=5,
                                command=self.add_words_window)
        self.start_learning = Button(self.root, text="Start learning", bd=5)

        self.add_words.grid(row=0, column=1, ipadx=25, pady=25)
        self.start_learning.grid(row=0, column=2, ipadx=40, pady=25)

    def add_words_window(self):
        self.add_words_pop = Toplevel(self.root)
        self.add_words_pop.geometry(self.set_main_pop(335, 75))
        self.root.withdraw()
        self.add_words_button()
        self.add_words_in_field()

    def add_words_button(self):
        butt_back = Button(self.add_words_pop, text="Back", command=self.close_add_words_window)
        butt_back.grid(row=1, column=0, ipadx=25, pady=25)

        butt_save = Button(self.add_words_pop, text="Save", command=self.close_add_words_window)
        butt_save.grid(row=0, column=1, ipadx=10, pady=25)

        butt_load = Button(self.add_words_pop, text="Load", command=self.close_add_words_window)
        butt_load.grid(row=0, column=2, ipadx=10, pady=25)

    def add_words_in_field(self):
        field_file_name = Entry(self.add_words_pop, width=25, bd=10)
        field_file_name.grid(row=0, column=0, ipadx=25, pady=25)

    def close_add_words_window(self):
        self.add_words_pop.destroy()
        self.root.deiconify()


# class WordsWindow(MainWindow):
#     def __init__(self,MainWindow):
#         self.mainwindow


def main():
    gui = MainWindow()
    gui.main_menu()


main()
