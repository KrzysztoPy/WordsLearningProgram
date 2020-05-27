from tkinter import *

from GUI.WordsWindow import *
from GUI.StartLearning import *


class MainWindow(WordsWindow, StartLearning):
    start_learning = StartLearning()
    root = Tk()
    add_words = None
    start_learning = None
    add_words_pop = None

    words_window = WordsWindow()

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
        # Set two button
        self.add_words = Button(self.root, text="Add new words list", bd=5,
                                command=lambda: self.words_window.words_window_main(self.root))
        self.start_learning = Button(self.root, text="Start learning", bd=5)

        self.add_words.grid(row=0, column=1, ipadx=25, pady=25)
        self.start_learning.grid(row=0, column=2, ipadx=40, pady=25)




def main():
    gui = MainWindow()
    gui.main_menu()


main()
