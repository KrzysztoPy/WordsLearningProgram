from FileOperations.FileOperations import open_folder_with_words_lists
from tkinter import messagebox
from tkinter import ttk

from LOGIC.CreateWordsListLogic import *


class CreateWordsListGUI(CreateWordsListLogic):
    create_words_list_logic_class = CreateWordsListLogic()
    main_menu_root = None

    list_words_name = None
    widget_option_menu = None
    actual_list_word_lists = []
    list_with_words_lists_name = None
    table_with_headers = None
    widget_entry_polish_word = None
    widget_entry_english_word = None
    actual_select_file_string_var = None
    label_currently_selected_word_var = None
    label_currently_selected_word = None
    label_currently_open_folder = None
    label_currently_open_file = None

    def size_and_position_main_window(self, main_menu_root):
        main_window_width = 1400
        main_window_height = 600
        position_from_right_side_screen = int(main_menu_root.winfo_screenwidth() / 2 - main_window_width / 2)
        position_from_left_side_screen = int(main_menu_root.winfo_screenheight() / 2 - main_window_height / 2)
        return "{}x{}+{}+{}".format(main_window_width, main_window_height, position_from_right_side_screen,
                                    position_from_left_side_screen)

    def words_window_main(self, root):
        self.main_menu_root = root
        self.actual_select_file_string_var = StringVar()
        self.label_currently_selected_word_var = StringVar()

        self.create_words_list_logic = Toplevel(self.main_menu_root)
        self.create_words_list_logic.geometry(self.size_and_position_main_window(self.main_menu_root))

        # Removes the window from the screen(without destroying it).
        self.main_menu_root.withdraw()
        # New
        self.label_displays_name_word_list_file()
        self.label_widget_unchanging()
        self.actual_select_file_string_var.set(
            self.create_words_list_logic_class.set_actual_selected_file() +
            self.create_words_list_logic_class.NOTHING_SELECTED)
        self.label_currently_selected_word_var_initial_state()

        # button New
        self.button_add_new_words_list()
        self.button_load_data_from_selected_words_list()
        self.button_remove_words_list()
        self.button_tmp_add_new_words_from_list()
        self.button_remove_tmp_add_words_from_list()
        self.button_find_words_in_actual_chooser_list()
        self.button_back_to_earlier_menu()
        self.button_save_a_list_with_new_added_words()
        self.create_words_list_logic_class.set_name_actual_select_file(
            self.create_words_list_logic_class.NOTHING_SELECTED)
        self.label_displays_actual_selected_word()
        # Old
        self.label_displays_actual_select_file()

        self.field_widget()
        self.option_menu_widget_list_with_words_list()

        # Set windows close event
        self.create_words_list_logic.protocol("WM_DELETE_WINDOW", self.close_words_window)
        self.set_table()

    def label_displays_name_word_list_file(self):

        butt_open_file_with_words_lists = Button(self.create_words_list_logic, text="Open directory with words lists",
                                                 fg="red", font='Helvetica 12 bold',
                                                 command=open_folder_with_words_lists)
        butt_open_file_with_words_lists.grid(row=0, column=0, columnspan=2, ipadx=70, pady=20)

    def label_widget_unchanging(self):
        label_set_name_file = Label(self.create_words_list_logic, text="Choice words list name ")
        label_set_name_file.grid(row=1, column=0)

        lab_polish_word = Label(self.create_words_list_logic, text="Polish word version:")
        lab_polish_word.grid(row=2, column=0)

        lab_english_word = Label(self.create_words_list_logic, text="English word version:")
        lab_english_word.grid(row=2, column=2)

    def label_displays_actual_select_file(self):
        self.label_currently_open_file = Label(self.create_words_list_logic,
                                               textvariable=self.actual_select_file_string_var,
                                               fg="dark green", font='Helvetica 15 bold', padx=2, anchor='w')
        self.label_currently_open_file.config(width=40)
        self.label_currently_open_file.grid(row=0, column=2, columnspan=2, sticky=E)

    def option_menu_widget_list_with_words_list(self):

        self.list_with_words_lists_name = StringVar()
        self.actual_list_word_lists = self.create_words_list_logic_class.get_list_name_converted_words_lists()

        self.list_with_words_lists_name.set(self.actual_list_word_lists[0])
        self.widget_option_menu = OptionMenu(self.create_words_list_logic, self.list_with_words_lists_name,
                                             *self.actual_list_word_lists)
        self.widget_option_menu.config(width=20)
        self.widget_option_menu.grid(row=1, column=3, ipadx=30)

    def button_add_new_words_list(self):
        butt_add_new_words_list = Button(self.create_words_list_logic, text="Add new word list",
                                         command=self.logic_to_use_button_add_new_words_list)
        butt_add_new_words_list.grid(row=1, column=2, ipadx=70, pady=0)
        self.create_words_list_logic.grid_columnconfigure(butt_add_new_words_list, minsize=1)

    def logic_to_use_button_add_new_words_list(self):
        new_name_a_file = self.list_words_name.get()
        repeated_name = ["", "", True]

        repeated_name = self.create_words_list_logic_class.check_whether_exists_file_with_the_same_name(new_name_a_file)
        self.info_popup(repeated_name)

        if not repeated_name[2]:
            repeated_name = self.create_words_list_logic_class.create_new_empty_list(new_name_a_file)
            self.info_popup(repeated_name)
            if repeated_name[2]:
                self.create_words_list_logic_class.clear_words_list_name(self.list_words_name)
                self.option_menu_widget_list_with_words_list()

    def button_load_data_from_selected_words_list(self):
        butt_load = Button(self.create_words_list_logic, text="Load list",
                           command=self.logic_to_use_button_load_list)
        butt_load.grid(row=1, column=4, ipadx=70, pady=0)
        self.create_words_list_logic.grid_columnconfigure(butt_load, minsize=1)

    def logic_to_use_button_load_list(self):
        if self.create_words_list_logic_class.which_selected_some_list(self.list_with_words_lists_name.get()):
            self.create_words_list_logic_class.open_file_and_return_converted_words_list(
                self.list_with_words_lists_name.get())
            self.clean_previous_data_from_table()
            self.set_value_table()
            self.create_words_list_logic_class.set_name_actual_select_file(
                self.list_with_words_lists_name.get())
            self.actual_select_file_string_var.set(
                (self.create_words_list_logic_class.INITIAL_STATE +
                 self.create_words_list_logic_class.get_name_actual_select_file()))
        else:
            self.info_popup([self.ERROR, "List with words list are empty. You aren't load nothing!"])

    def button_remove_words_list(self):
        butt_remove = Button(self.create_words_list_logic, text="Remove selected words list",
                             command=self.logic_to_use_button_remove_list_with_word)
        butt_remove.grid(row=1, column=5, columnspan=3, ipadx=70, pady=0)

    def logic_to_use_button_remove_list_with_word(self):
        selected_file_to_remove = self.list_with_words_lists_name.get()
        if self.create_words_list_logic_class.which_list_with_words_list_is_not_empty(selected_file_to_remove):
            self.info_popup(self.create_words_list_logic_class.butt_remove_file(selected_file_to_remove))

            if self.create_words_list_logic_class.remove_list_which_is_load(selected_file_to_remove):
                self.actual_select_file_string_var.set(
                    self.create_words_list_logic_class.set_actual_selected_file() +
                    self.create_words_list_logic_class.NOTHING_SELECTED)
                self.create_words_list_logic_class.set_all_words_in_select_list(
                    self.create_words_list_logic_class.EMPTY_LIST)
                self.create_words_list_logic_class.set_name_actual_select_file(
                    self.create_words_list_logic_class.NOTHING_SELECTED)
                self.label_currently_selected_word_var_initial_state()
                self.set_table()
        else:
            self.info_popup(
                [self.ERROR, "You don't selected list for remove. First you must selected list and next remove."])

    def button_tmp_add_new_words_from_list(self):
        butt_add = Button(self.create_words_list_logic, text="Add words",
                          command=self.logic_to_use_button_add_new_word)
        butt_add.grid(row=2, column=4, ipadx=10, pady=25)

    def logic_to_use_button_add_new_word(self):
        if self.create_words_list_logic_class.which_list_with_words_list_is_not_empty():
            self.info_popup(
                self.create_words_list_logic_class.check_is_empty_repeat_field(self.widget_entry_polish_word.get(),
                                                                               self.widget_entry_english_word.get()))
            if self.create_words_list_logic_class.added_new_words:
                self.create_words_list_logic_class.set_added_new_words(False)
                self.clean_previous_data_from_table()
                self.widget_entry_polish_word.delete(0, 'end')
                self.widget_entry_english_word.delete(0, 'end')
                self.set_value_table()
        else:
            self.info_popup([self.ERROR, "You must first select which list."])

    def button_remove_tmp_add_words_from_list(self):
        butt_remove = Button(self.create_words_list_logic, text="Remove word",
                             command=self.logic_to_use_button_remove_selected_word)
        butt_remove.grid(row=2, column=5, ipadx=10, pady=25)

    def logic_to_use_button_remove_selected_word(self):
        self.remove_words()
        self.set_table()
        self.set_value_table()
        self.info_popup(self.create_words_list_logic_class.remove_word_from_lists())

    def button_find_words_in_actual_chooser_list(self):
        butt_find = Button(self.create_words_list_logic, text="Find",
                           command=self.create_words_list_logic_class.find_word)
        butt_find.grid(row=2, column=6, ipadx=10, pady=25)

    def button_back_to_earlier_menu(self):
        butt_back = Button(self.create_words_list_logic, text="Back",
                           command=lambda: self.create_words_list_logic_class.close_words_window(
                               self.create_words_list_logic,
                               self.main_menu_root))
        butt_back.grid(row=4, column=0, ipadx=25, pady=25)

    def button_save_a_list_with_new_added_words(self):
        butt_save = Button(self.create_words_list_logic, text="Save words")
        butt_save.grid(row=4, column=4, ipadx=70, pady=0)

    def field_widget(self):

        self.list_words_name = Entry(self.create_words_list_logic, width=25, bd=5)
        self.list_words_name.grid(row=1, column=1, ipadx=25, pady=25)

        self.widget_entry_polish_word = Entry(self.create_words_list_logic, width=25, bd=5)
        self.widget_entry_polish_word.grid(row=2, column=1, ipadx=25, pady=25)

        self.widget_entry_english_word = Entry(self.create_words_list_logic, width=25, bd=5)
        self.widget_entry_english_word.grid(row=2, column=3, ipadx=25, pady=25)

    def remove_words(self):
        clicked_elem = ('<Double-1>', self.on_select)
        self.table_with_headers.bind('<Double-1>', self.on_select)

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

    def label_displays_actual_selected_word(self):
        self.label_currently_selected_word = Label(self.create_words_list_logic,
                                                   textvariable=self.label_currently_selected_word_var,
                                                   fg="dark green", font='Helvetica 15 bold', padx=2, anchor='w')
        self.label_currently_selected_word.config(width=40)
        self.label_currently_selected_word.grid(row=3, column=4, columnspan=2, sticky=E)

    def set_value_table(self):
        for counter in range(0, self.create_words_list_logic_class.get_converted_words_from_selected_list().__len__(),
                             3):
            self.table_with_headers.insert("", 'end',
                                           values=self.create_words_list_logic_class.return_separated_individual_elem(
                                               counter))

    def clean_previous_data_from_table(self):
        self.get_set_table_with_headers().delete(*self.get_set_table_with_headers().get_children())

    def set_table_with_headers(self, table_with_headers):
        self.table_with_headers = table_with_headers

    def get_set_table_with_headers(self):
        return self.table_with_headers

    def info_popup(self, info_list):
        if info_list[0] == self.create_words_list_logic_class.ERROR:
            messagebox.showerror(info_list[0], info_list[1])
        elif info_list[0] == self.create_words_list_logic_class.INFORMATION:
            self.option_menu_widget_list_with_words_list()
            messagebox.showinfo(info_list[0], info_list[1])
        elif info_list[0] == self.create_words_list_logic_class.SAVE:

            self.set_value_table()
            messagebox.showinfo(info_list[0], info_list[1])

    def on_select(self, event):
        cur_item = self.table_with_headers.focus()
        self.create_words_list_logic_class.convert_value_from_table_to_remove(self.table_with_headers.item(cur_item))
        print(self.create_words_list_logic_class.get_convert_value_from_click_table_event())
        self.label_currently_selected_word_var.set(
            self.create_words_list_logic_class.get_convert_by_view_value_from_click_table_event())

    def label_currently_selected_word_var_initial_state(self):
        self.label_currently_selected_word_var.set(
            self.create_words_list_logic_class.set_actual_selected_words() +
            self.create_words_list_logic_class.NOTHING_SELECTED)

    def close_words_window(self):
        self.create_words_list_logic.destroy()
        self.main_menu_root.destroy()
        exit()
