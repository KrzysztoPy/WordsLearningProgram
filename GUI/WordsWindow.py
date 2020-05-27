from tkinter import *
from tkinter import messagebox
from LOGIC.Logic import *


class WordsWindow(Logic):
    logic = Logic()

    main_root = None
    words_window_root = None

    # Entry field // take name directory
    field_file_name = None

    # Variable for test
    listbox_with_folder = None

    def set_main_pop(self, main_root) -> str:
        # Set size view window
        window_width = 1200
        window_height = 600
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def words_window_main(self, root):
        self.main_root = root
        # Create new top pop
        self.words_window_root = Toplevel(self.main_root)

        self.words_window_root.geometry(self.set_main_pop(self.main_root))
        # Main pop set invisible
        self.main_root.withdraw()
        self.words_window_label()
        self.words_window_in_field()
        self.words_window_button()

        # Set windows close event
        self.words_window_root.protocol("WM_DELETE_WINDOW", self.close_words_window)

    def words_window_button(self):
        butt_save = Button(self.words_window_root, text="Save",
                           command=lambda: self.info_popup(self.logic.dir_name_is_empty(self.field_file_name.get())))
        butt_save.grid(row=1, column=2, ipadx=70, pady=0)

        butt_load = Button(self.words_window_root, text="Load")
        butt_load.grid(row=1, column=4, ipadx=70, pady=0)
        self.words_window_root.grid_columnconfigure(butt_load, minsize=1)

        butt_load = Button(self.words_window_root, text="Add")
        butt_load.grid(row=2, column=4, ipadx=10, pady=25)

        butt_load = Button(self.words_window_root, text="Remove")
        butt_load.grid(row=2, column=5, ipadx=10, pady=25)

        butt_load = Button(self.words_window_root, text="Find")
        butt_load.grid(row=2, column=6, ipadx=10, pady=25)

        butt_back = Button(self.words_window_root, text="Back", command=self.close_words_window)
        butt_back.grid(row=5, column=0, ipadx=25, pady=25)

    def words_window_in_field(self):
        self.field_file_name = Entry(self.words_window_root, width=25, bd=5)
        self.field_file_name.grid(row=1, column=1, ipadx=25, pady=25)

        polish_word = Entry(self.words_window_root, width=25, bd=5)
        polish_word.grid(row=2, column=1, ipadx=25, pady=25)

        english_word = Entry(self.words_window_root, width=25, bd=5)
        english_word.grid(row=2, column=3, ipadx=25, pady=25)

    def words_window_label(self):
        lab_name_fail = Label(self.words_window_root, text="Enter the file name: ")
        lab_name_fail.grid(row=1, column=0)

        currently_open_file = Label(self.words_window_root, text="Currently choice file: None  ",
                                    fg="red", font='Helvetica 13 bold', padx=2)
        currently_open_file.grid(row=0, column=1)

        lab_polish_word = Label(self.words_window_root, text="Polish word version:")
        lab_polish_word.grid(row=2, column=0)

        lab_english_word = Label(self.words_window_root, text="English word version:")
        lab_english_word.grid(row=2, column=2)

    # Get list with 2 elem:
    # First: Messagebox type
    # Second: How text view
    def info_popup(self, info_list):
        if info_list[0] == "Error":
            messagebox.showerror(info_list[0], info_list[1])
            pass
        elif info_list[0] == "Information":
            messagebox.showinfo(info_list[0], info_list[1])

    def set_combobox(self):
        combobox_folder_list = OptionMenu()

    def close_words_window(self):
        self.words_window_root.destroy()
        self.main_root.destroy()
        exit()

    def test(self):
        my_list = ["One", "Two", "Three"]
        for i in range(0, 11):
            self.listbox_with_folder.insert("end", "This is a number !!!!!!!!!!!!!!: {}".format(i))
