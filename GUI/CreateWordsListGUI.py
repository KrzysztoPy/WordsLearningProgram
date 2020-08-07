from tkinter import messagebox
from LOGIC.CreateWordsListLogic import *
from tkinter import ttk


# Program create at system new directory about name "Words list" and stores in there files with words list


class CreateWordsListGUI(CreateWordsListLogic):
    word_window_logic = CreateWordsListLogic()
    main_menu_root = None
    create_words_list_logic = None

    list_words_name = None

    widget_option_menu = None

    actual_list_word_lists = None
    list_with_words_lists_name = None

    table_with_headers = None

    widget_entry_polish_word = None
    widget_entry_english_word = None

    actual_select_file = None

    label_currently_open_folder = None
    label_currently_open_file = None

    def set_param_main_pop(self, main_menu_root) -> str:
        window_width = 1300
        window_height = 600
        # Setting window center position at your monitor
        position_right = int(main_menu_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_menu_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def words_window_main(self, root):
        self.main_menu_root = root
        # Create new folder in system
        # self.word_window_logic.path_create_directory()

        self.actual_select_file = StringVar()
        # Create new top pop
        self.create_words_list_logic = Toplevel(self.main_menu_root)

        self.create_words_list_logic.geometry(self.set_param_main_pop(self.main_menu_root))

        # Main pop set invisible
        self.main_menu_root.withdraw()

        # self.set_frame()
        self.changing_label_widget()
        self.label_widget()
        self.field_widget()
        self.option_menu_widget()
        self.button_widget()

        # Set windows close event
        self.create_words_list_logic.protocol("WM_DELETE_WINDOW", self.close_words_window)
        self.set_table()

    # set all button
    def button_widget(self):

        butt_save = Button(self.create_words_list_logic, text="Save word list",
                           command=lambda: [
                               self.info_popup(self.word_window_logic.file_create(self.list_words_name.get()))
                               , self.word_window_logic.file_list(), self.option_menu_widget()])
        butt_save.grid(row=1, column=2, ipadx=70, pady=0)
        self.create_words_list_logic.grid_columnconfigure(butt_save, minsize=1)

        butt_load = Button(self.create_words_list_logic, text="Load",
                           command=lambda: [self.set_table(), self.word_window_logic.open_file_and_return_words_list(
                               self.list_with_words_lists_name.get()),
                                            self.set_value_table(),
                                            self.actual_select_file.set(
                                                self.word_window_logic.actual_select_file_string_set(
                                                    self.list_with_words_lists_name.get())),
                                            self.changing_label_widget()])
        butt_load.grid(row=1, column=4, ipadx=70, pady=0)
        self.create_words_list_logic.grid_columnconfigure(butt_load, minsize=1)

        butt_remove = Button(self.create_words_list_logic, text="Remove",
                             command=lambda: [self.set_table(), self.word_window_logic.remove_button(
                                 self.list_with_words_lists_name.get()),
                                              self.option_menu_widget(),
                                              self.actual_select_file.set(
                                                  self.word_window_logic.actual_select_file_string_set(
                                                      "None"))])
        butt_remove.grid(row=1, column=5, ipadx=70, pady=0)

        butt_save = Button(self.create_words_list_logic, text="Save words")
        butt_save.grid(row=4, column=4, ipadx=70, pady=0)

        butt_add = Button(self.create_words_list_logic, text="Add",
                          command=lambda: [
                              self.info_popup(
                                  self.word_window_logic.whether_repeat_empty_field_and_no_selected_list(
                                      self.widget_entry_polish_word.get(),
                                      self.widget_entry_english_word.get())), self.set_value_table()
                          ])
        butt_add.grid(row=2, column=4, ipadx=10, pady=25)

        butt_remove = Button(self.create_words_list_logic, text="Remove word",
                             command=lambda: [self.info_popup(self.word_window_logic.remove_word_from_lists()),
                                              self.set_value_table()])
        butt_remove.grid(row=2, column=5, ipadx=10, pady=25)

        butt_find = Button(self.create_words_list_logic, text="Find", command=self.word_window_logic.find_word)
        butt_find.grid(row=2, column=6, ipadx=10, pady=25)

        butt_back = Button(self.create_words_list_logic, text="Back",
                           command=lambda: self.word_window_logic.close_words_window(self.create_words_list_logic,
                                                                                     self.main_menu_root))
        butt_back.grid(row=4, column=0, ipadx=25, pady=25)

        # set all field

    def field_widget(self):

        label_currently_open_file_first_version = Label(self.create_words_list_logic,
                                                        text="Actual select file: None",
                                                        fg="dark green", font='Helvetica 15 bold', padx=2)
        label_currently_open_file_first_version.grid(row=0, column=3)

        self.list_words_name = Entry(self.create_words_list_logic, width=25, bd=5)
        self.list_words_name.grid(row=1, column=1, ipadx=25, pady=25)

        self.widget_entry_polish_word = Entry(self.create_words_list_logic, width=25, bd=5)
        self.widget_entry_polish_word.grid(row=2, column=1, ipadx=25, pady=25)

        self.widget_entry_english_word = Entry(self.create_words_list_logic, width=25, bd=5)
        self.widget_entry_english_word.grid(row=2, column=3, ipadx=25, pady=25)

    def changing_label_widget(self):
        self.label_currently_open_folder = Label(self.create_words_list_logic,
                                                 text="Directory with word lists: {}                       ".format(
                                                     self.word_window_logic.dir_with_words_list),
                                                 fg="red", font='Helvetica 15 bold', padx=2)
        self.label_currently_open_folder.config(width=50)
        self.label_currently_open_folder.grid(row=0, column=0, columnspan=3, )

        self.label_currently_open_file = Label(self.create_words_list_logic,
                                               textvariable=self.actual_select_file,
                                               fg="dark green", font='Helvetica 15 bold', padx=2, anchor='w')
        self.label_currently_open_file.config(width=40)
        self.label_currently_open_file.grid(row=0, column=3, columnspan=3)

    def label_widget(self):

        label_set_name_file = Label(self.create_words_list_logic, text="Choice words list name ")
        label_set_name_file.grid(row=1, column=0)

        lab_polish_word = Label(self.create_words_list_logic, text="Polish word version:")
        lab_polish_word.grid(row=2, column=0)

        lab_english_word = Label(self.create_words_list_logic, text="English word version:")
        lab_english_word.grid(row=2, column=2)

    def set_table(self):
        self.table_with_headers = ttk.Treeview(self.create_words_list_logic, selectmode='browse')
        self.table_with_headers.grid(row=3, column=2, columnspan=2)
        verscrlbar = ttk.Scrollbar(self.create_words_list_logic, orient="vertical",
                                   command=self.table_with_headers.yview)
        verscrlbar.grid(row=3, column=3, sticky=N + S + E)
        self.table_with_headers.configure(xscrollcommand=verscrlbar.set)

        self.table_with_headers["columns"] = ("1", "2", "3")
        self.table_with_headers['show'] = 'headings'

        self.table_with_headers.column("1", width=20, anchor='se')
        self.table_with_headers.column("2", width=180, anchor='se')
        self.table_with_headers.column("3", width=180, anchor='se')

        self.table_with_headers.heading("1", text="Id")
        self.table_with_headers.heading("2", text="Polish word")
        self.table_with_headers.heading("3", text="English word")
        self.table_with_headers.bind('<Double-1>', self.on_select)

    def add_new_word_from_table(self):
        # self.table_with_headers.insert("", 'end',
        #                                values=self.word_window_logic.return_words_line(counter))
        pass

    def set_value_table(self):
        # [[x,y,x],[x,y,z]]

        self.table_with_headers.delete(*self.table_with_headers.get_children())
        for counter in range(0, self.word_window_logic.get_all_words_in_select_list().__len__(), 3):
            self.table_with_headers.insert("", 'end',
                                           values=self.word_window_logic.return_words_line(counter))
        print(self.table_with_headers.get_children())

    def option_menu_widget(self):
        self.actual_list_word_lists = self.word_window_logic.file_list()
        self.list_with_words_lists_name = StringVar()
        self.list_with_words_lists_name.set(self.actual_list_word_lists[0])

        self.widget_option_menu = OptionMenu(self.create_words_list_logic, self.list_with_words_lists_name,
                                             *self.actual_list_word_lists)
        self.widget_option_menu.config(width=20)
        self.widget_option_menu.grid(row=1, column=3, ipadx=30)

    # Remember add_butt command return give 3 variable [type pop, information, new words list]
    def info_popup(self, info_list):
        if info_list[0] == "Error":
            messagebox.showerror(info_list[0], info_list[1])
            pass
        elif info_list[0] == "Information":
            self.option_menu_widget()
            messagebox.showinfo(info_list[0], info_list[1])
        elif info_list[0] == "Save":
            self.set_table()
            self.set_value_table()
            messagebox.showinfo(info_list[0], info_list[1])

    def on_select(self, event):
        cur_item = self.table_with_headers.focus()
        self.word_window_logic.convert_value_from_table_to_remove(self.table_with_headers.item(cur_item))

    # def close_words_window(self):
    #     self.create_words_list_logic.destroy()
    #     self.main_menu_root.destroy()
    #     exit()
