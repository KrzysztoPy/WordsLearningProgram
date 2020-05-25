from tkinter import *


class WordsWindow:
    main_root = None
    add_words_pop = None

    def set_main_pop(self, main_root) -> str:
        # Set size view window
        window_width = 335
        window_height = 75
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def add_words_window(self, root):
        self.main_root = root
        self.add_words_pop = Toplevel(self.main_root)
        self.add_words_pop.geometry(self.set_main_pop(self.main_root))
        self.main_root.withdraw()
        self.add_words_in_field()
        self.add_words_button()

    def add_words_button(self):
        butt_back = Button(self.add_words_pop, text="Back", command=self.close_add_words_window)
        butt_back.grid(row=1, column=0, ipadx=25, pady=25)

        butt_save = Button(self.add_words_pop, text="Save")
        butt_save.grid(row=0, column=1, ipadx=10, pady=25)

        butt_load = Button(self.add_words_pop, text="Load")
        butt_load.grid(row=0, column=2, ipadx=10, pady=25)

    def add_words_in_field(self):
        field_file_name = Entry(self.add_words_pop, width=25, bd=10)
        field_file_name.grid(row=0, column=0, ipadx=25, pady=25)

    def close_add_words_window(self):
        self.add_words_pop.destroy()
        self.main_root.deiconify()
