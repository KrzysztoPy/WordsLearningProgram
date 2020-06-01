from tkinter import messagebox
from LOGIC.Logic import *
from tkinter import ttk


class WordsWindow(Logic):
    logic = Logic()

    # Main root and top window root
    main_root = None
    words_window_root = None

    # Entry field // take name directory
    file_name = None

    # Variable for test
    listbox_with_folder = None

    file_list = None

    clicked_file = None
    choice_file = None

    table = None

    # Set position and size all windows
    def set_main_pop(self, main_root) -> str:
        # Default window size
        window_width = 1200
        window_height = 600
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    # Main method create top window
    def words_window_main(self, root):
        self.main_root = root
        # Create new top pop
        self.words_window_root = Toplevel(self.main_root)

        self.words_window_root.geometry(self.set_main_pop(self.main_root))
        # Main pop set invisible
        self.main_root.withdraw()

        self.logic.create_directory()

        #
        self.words_window_label()
        self.words_window_in_field()
        self.option_menu()
        self.words_window_button()

        # Set windows close event
        self.words_window_root.protocol("WM_DELETE_WINDOW", self.close_words_window)
        self.set_table()

    # set all button
    def words_window_button(self):

        butt_save = Button(self.words_window_root, text="Save word list",
                           command=lambda: [self.info_popup(self.logic.file_create(self.file_name.get()))
                               , self.logic.file_list(), self.option_menu()])
        butt_save.grid(row=1, column=2, ipadx=70, pady=0)
        self.words_window_root.grid_columnconfigure(butt_save, minsize=1)

        butt_load = Button(self.words_window_root, text="Load", command=lambda: self.set_value_table(self.logic.load_butt(self.clicked_file.get())))
        butt_load.grid(row=1, column=4, ipadx=70, pady=0)
        self.words_window_root.grid_columnconfigure(butt_load, minsize=1)

        butt_save = Button(self.words_window_root, text="Save words")  # Without command!!!
        butt_save.grid(row=4, column=4, ipadx=70, pady=0)

        butt_add = Button(self.words_window_root, text="Add")
        butt_add.grid(row=2, column=4, ipadx=10, pady=25)

        butt_remove = Button(self.words_window_root, text="Remove")
        butt_remove.grid(row=2, column=5, ipadx=10, pady=25)

        butt_find = Button(self.words_window_root, text="Find")
        butt_find.grid(row=2, column=6, ipadx=10, pady=25)

        butt_back = Button(self.words_window_root, text="Back", command=self.close_words_window)
        butt_back.grid(row=4, column=0, ipadx=25, pady=25)

    # set all field
    def words_window_in_field(self):

        self.file_name = Entry(self.words_window_root, width=25, bd=5)
        self.file_name.grid(row=1, column=1, ipadx=25, pady=25)

        polish_word = Entry(self.words_window_root, width=25, bd=5)
        polish_word.grid(row=2, column=1, ipadx=25, pady=25)

        english_word = Entry(self.words_window_root, width=25, bd=5)
        english_word.grid(row=2, column=3, ipadx=25, pady=25)

    # Set all label
    def words_window_label(self):
        currently_open_file = Label(self.words_window_root,
                                    text="Directory with word lists: {}                       ".format(
                                        self.logic.dir_name),
                                    fg="red", font='Helvetica 15 bold', padx=2)
        currently_open_file.grid(row=0, column=0, columnspan=4)

        label_set_name_file = Label(self.words_window_root, text="Choice words list name ")
        label_set_name_file.grid(row=1, column=0)

        lab_polish_word = Label(self.words_window_root, text="Polish word version:")
        lab_polish_word.grid(row=2, column=0)

        lab_english_word = Label(self.words_window_root, text="English word version:")
        lab_english_word.grid(row=2, column=2)

        lab_english_word = Label(self.words_window_root, text="Selected file")
        lab_english_word.grid(row=0, column=3)

    def set_table(self):
        self.table = ttk.Treeview(self.words_window_root, selectmode='browse')
        self.table.grid(row=3, column=2, columnspan=2)
        verscrlbar = ttk.Scrollbar(self.words_window_root, orient="vertical", command=self.table.yview)
        verscrlbar.grid(row=3, column=2, sticky=N + S + E, columnspan=2)
        self.table.configure(xscrollcommand=verscrlbar.set)

        self.table["columns"] = ("1", "2", "3")
        self.table['show'] = 'headings'

        self.table.column("1", width=20, anchor='se')
        self.table.column("2", width=180, anchor='se')
        self.table.column("3", width=180, anchor='se')

        self.table.heading("1", text="Id")
        self.table.heading("2", text="Polish word")
        self.table.heading("3", text="English word")

    def set_value_table(self, words):
        # [[x,y,x],[x,y,z]]
        for i in words:
            self.table.insert("", 'end', text="L1", values=(i[0], i[1], i[2]))

    # Give possibility to choice
    def option_menu(self):
        self.file_list = self.logic.file_list()
        self.clicked_file = StringVar()
        self.clicked_file.set(self.file_list[0])

        self.choice_file = OptionMenu(self.words_window_root, self.clicked_file,
                                      *self.file_list)
        self.choice_file.grid(row=1, column=3, ipadx=65)

    def info_popup(self, info_list):
        if info_list[0] == "Error":
            messagebox.showerror(info_list[0], info_list[1])
            pass
        elif info_list[0] == "Information":
            self.option_menu()
            messagebox.showinfo(info_list[0], info_list[1])

    def close_words_window(self):
        self.words_window_root.destroy()
        self.main_root.destroy()
        exit()

    def test(self):
        my_list = ["One", "Two", "Three"]
        for i in range(0, 11):
            self.listbox_with_folder.insert("end", "This is a number !!!!!!!!!!!!!!: {}".format(i))
