from tkinter import *
from LOGIC.Logic import *


class WordsWindow(Logic):
    main_root = None
    words_window_root = None

    def set_main_pop(self, main_root) -> str:
        # Set size view window
        window_width = 1200
        window_height = 600
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def add_words_window(self, root):
        self.main_root = root
        # Create new top pop
        self.words_window_root = Toplevel(self.main_root)
        self.words_window_root.geometry(self.set_main_pop(self.main_root))
        # Main pop set invisible
        self.main_root.withdraw()
        self.add_words_label()
        self.add_words_in_field()
        self.add_words_button()
        # Set windows close event
        self.words_window_root.protocol("WM_DELETE_WINDOW", self.close_add_words_window)

    def add_words_button(self):
        butt_save = Button(self.words_window_root, text="Save")
        butt_save.grid(row=0, column=2, ipadx=50, pady=25)

        butt_load = Button(self.words_window_root, text="Load")
        butt_load.grid(row=0, column=4, ipadx=50, pady=25)

        butt_load = Button(self.words_window_root, text="Add")
        butt_load.grid(row=1, column=4, ipadx=10, pady=25)

        butt_load = Button(self.words_window_root, text="Remove")
        butt_load.grid(row=1, column=5, ipadx=10, pady=25)

        butt_load = Button(self.words_window_root, text="Find")
        butt_load.grid(row=1, column=6, ipadx=10, pady=25)

        butt_back = Button(self.words_window_root, text="Back", command=self.close_add_words_window)
        butt_back.grid(row=4, column=0, ipadx=25, pady=25)

    def add_words_in_field(self):
        field_file_name = Entry(self.words_window_root, width=25, bd=5)
        field_file_name.grid(row=0, column=1, ipadx=25, pady=25)

        polish_word = Entry(self.words_window_root, width=25, bd=5)
        polish_word.grid(row=1, column=1, ipadx=25, pady=25)

        english_word = Entry(self.words_window_root, width=25, bd=5)
        english_word.grid(row=1, column=3, ipadx=25, pady=25)

    def add_words_label(self):
        lab_name_fail = Label(self.words_window_root, text="Enter the file name: ")
        lab_name_fail.grid(row=0, column=0)

        lab_polish_word = Label(self.words_window_root, text="Polish word version:")
        lab_polish_word.grid(row=1, column=0)

        lab_english_word = Label(self.words_window_root, text="English word version:")
        lab_english_word.grid(row=1, column=2)

    def close_add_words_window(self):
        self.words_window_root.destroy()
        self.main_root.deiconify()
