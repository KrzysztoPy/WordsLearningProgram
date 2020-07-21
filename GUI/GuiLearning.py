from LOGIC.LearningLogic import *
from tkinter import *


class GuiLearning(LearningLogic):
    l_logic = LearningLogic()

    gui_learning_main_root = None
    learning_logic_root = None

    label_word_for_translate = None
    tmp_word_for_translate = None
    label_text_language_version = None

    file_words_list = None
    entry_label_word_translation = None

    tmp_text_answer_in_language = None

    tmp_text_correct_answer = None

    tmp_all_words_counter = None
    tmp_correctly_words_counter = None
    tmp_incorrectly_words_counter = None
    tmp_user_wrote_answer = None
    tmp_label_good_bad_answer = "None"
    tmp_color_and_good_bad_answer = None

    label_all_words_counter = None
    label_correctly_words_counter = None
    label_incorrectly_words_counter = None
    label_user_wrote_answer = None
    label_good_bad_answer = None

    def start_learning_menu(self, root):
        self.gui_learning_main_root = root

        self.tmp_text_answer_in_language = StringVar()
        self.tmp_word_for_translate = StringVar()
        self.tmp_text_correct_answer = StringVar()

        self.tmp_all_words_counter = StringVar()
        self.tmp_correctly_words_counter = StringVar()
        self.tmp_incorrectly_words_counter = StringVar()

        self.tmp_user_wrote_answer = StringVar()
        self.tmp_label_good_bad_answer = StringVar()

        self.learning_logic_root = Toplevel(self.gui_learning_main_root)
        self.learning_logic_root.geometry(self.l_logic.set_size_main_pop(self.gui_learning_main_root))
        self.learning_logic_root.resizable(width=False, height=False)
        # Set menu window invisible
        self.gui_learning_main_root.withdraw()
        #######check

        # Set combobox
        self.first_set_all_label()

        self.combo_box_with_words_lists()

        self.set_entry_field()
        self.set_all_button()
        # Click enter launch check_word method
        self.learning_logic_root.bind('<Return>', self.butt_word_check_command)

    def first_set_all_label(self):
        # Empty label
        empty_before_report_label = Label(self.learning_logic_root, text="")
        empty_before_report_label.grid(row=2, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_logic_root, text="")
        empty_after_report_label.grid(row=3, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_logic_root, text="")
        empty_after_report_label.grid(row=4, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_logic_root, text="")
        empty_after_report_label.grid(row=6, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_logic_root, text="")
        empty_after_report_label.grid(row=8, column=0, ipadx=65)
        # End empty label

        constans_label_set_file_which_get = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                                  text="Choice words list name ")
        constans_label_set_file_which_get.grid(row=0, column=0)

        constans_label_answer_language_version = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                                       text="Answer in language: ")
        constans_label_answer_language_version.grid(row=1, column=2)

        self.label_text_language_version = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                                 text="Polish version")
        self.label_text_language_version.grid(row=1, column=3)

        constans_label_actual_translate_word = Label(self.learning_logic_root, font='Helvetica 11 bold', text="Words: ")
        constans_label_actual_translate_word.grid(row=4, column=0)

        constans_label_correctly_answer = Label(self.learning_logic_root, fg="green", font='Helvetica 11 bold',
                                                text="Correct answer: ")
        constans_label_correctly_answer.grid(row=4, column=2)

        constans_label_user_answer = Label(self.learning_logic_root, fg="black", font='Helvetica 11 bold',
                                           text="Your answer: ")
        constans_label_user_answer.grid(row=4, column=4)

        constans_label_polish_word_version = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                                   text="Polish version ---> ")
        constans_label_polish_word_version.grid(row=5, column=0)

        constans_label_words_report = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                            text="Words report ->>> ")
        constans_label_words_report.grid(row=7, column=0)

        self.label_all_words_counter = Label(self.learning_logic_root, fg="dark blue", font='Helvetica 11 bold',
                                             text="Words counter: 0")
        self.label_all_words_counter.grid(row=7, column=1)

        self.label_correctly_words_counter = Label(self.learning_logic_root, fg="green", font='Helvetica 11 bold',
                                                   text="Words correctly: 0")
        self.label_correctly_words_counter.grid(row=7, column=2)

        self.label_incorrectly_words_counter = Label(self.learning_logic_root, fg="red", font='Helvetica 11 bold',
                                                     text="Words incorrectly: 0")

        self.label_incorrectly_words_counter.grid(row=7, column=3)

    def combo_box_with_words_lists(self):
        file_lists = self.l_logic.show_whole_file_in_file()
        self.file_words_list = StringVar()
        self.file_words_list.set(file_lists[0])

        choice_file = OptionMenu(self.learning_logic_root, self.file_words_list, *file_lists)
        choice_file.config(width=20)
        choice_file.grid(row=1, column=0, ipadx=65)

    def set_entry_field(self):
        self.entry_label_word_translation = Entry(self.learning_logic_root, width=25, bd=5)
        self.entry_label_word_translation.grid(row=5, column=1, ipadx=25, pady=25)

    def set_all_button(self):
        butt_load = Button(self.learning_logic_root, font='Helvetica 11 bold', text="Load",
                           command=lambda: [
                               self.l_logic.clear_all_word_list_variable(),
                               self.tmp_word_for_translate.set(
                                   self.l_logic.load_clicked_file(self.file_words_list.get())),
                               self.tmp_all_words_counter.set(self.l_logic.report_counter_set()),
                               self.tmp_correctly_words_counter.set(self.l_logic.report_correctly_set()),
                               self.tmp_incorrectly_words_counter.set(self.l_logic.report_incorrectly_set()),
                               self.tmp_text_correct_answer.set(self.l_logic.currently_answer()),

                               self.change_label_correctly_word_version(),
                               self.change_label_word_for_translation(),
                               self.change_label_report_words_counter(),
                               self.change_label_report_correctly_words(),
                               self.change_label_report_incorrectly_words(),
                           ])
        butt_load.grid(row=1, column=1, ipadx=70, pady=0)

        version_butt = Button(self.learning_logic_root, font='Helvetica 11 bold', text="Change",
                              command=lambda:
                              [self.tmp_text_answer_in_language.set(self.l_logic.change_language_answer()),
                               self.tmp_word_for_translate.set(self.l_logic.mix_words_after_change_language()),
                               self.change_label_language_version(),
                               self.l_logic.clear_to_first_position(),
                               self.tmp_correctly_words_counter.set(self.l_logic.report_correctly_set()),
                               self.tmp_incorrectly_words_counter.set(self.l_logic.report_incorrectly_set()),
                               self.tmp_text_correct_answer.set(self.l_logic.currently_answer()),
                               self.change_label_correctly_word_version(),
                               self.change_label_report_correctly_words(),
                               self.change_label_report_incorrectly_words(),
                               ])

        version_butt.grid(row=1, column=4, ipadx=70, pady=0)

        butt_word_check = Button(self.learning_logic_root, font='Helvetica 11 bold', text="Words Check",
                                 command=lambda: self.butt_word_check_command(event=NONE))

        butt_word_check.grid(row=5, column=2, ipadx=70, pady=0)
        butt_back = Button(self.learning_logic_root, font='Helvetica 11 bold',
                           text="BACK", command=lambda: self.l_logic.close_Learning_window(self.learning_logic_root,
                                                                                           self.gui_learning_main_root,
                                                                                           self.l_logic))

        butt_back.grid(row=9, column=0, ipadx=70, pady=0)

    # Copy butt_word_check from set_all_button for enter click event
    def butt_word_check_command(self, event):
        self.l_logic.check_correctness_word(self.entry_label_word_translation.get(),
                                            self.tmp_word_for_translate.get()),
        self.tmp_label_good_bad_answer.set(self.l_logic.set_label_whether_good_bad_answer()),
        self.tmp_color_and_good_bad_answer = self.l_logic.set_label_good_bad_answer_color(),

        self.tmp_user_wrote_answer.set(
            self.l_logic.set_label_user_answer(self.entry_label_word_translation.get())),
        self.entry_label_word_translation.delete(0, 'end'),
        self.tmp_text_correct_answer.set(
            self.l_logic.set_correct_answer_for_question(self.tmp_word_for_translate.get())),
        # Set widget
        self.tmp_word_for_translate.set(self.l_logic.load_next_word()),
        self.tmp_correctly_words_counter.set(self.l_logic.report_correctly_set()),
        self.tmp_incorrectly_words_counter.set(self.l_logic.report_incorrectly_set()),
        self.change_label_user_answer(),
        self.change_label_good_bad_view_answer(),
        self.change_label_correctly_word_version(),
        self.change_label_word_for_translation(),
        self.change_label_report_correctly_words(),
        self.change_label_report_incorrectly_words(),

    def change_label_language_version(self):
        self.label_text_language_version = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                                 textvariable=self.tmp_text_answer_in_language)
        self.label_text_language_version.grid(row=1, column=3)

    def change_label_correctly_word_version(self):
        self.label_correctly_answer = Label(self.learning_logic_root, font='Helvetica 11 bold',
                                            textvariable=self.tmp_text_correct_answer)
        self.label_correctly_answer.grid(row=4, column=3)

    def change_label_word_for_translation(self):
        self.label_word_for_translate = Label(self.learning_logic_root, font='Helvetica 11 bold', fg="dark blue",
                                              textvariable=self.tmp_word_for_translate)
        self.label_word_for_translate.grid(row=4, column=1)

    def change_label_report_words_counter(self):
        self.label_all_words_counter = Label(self.learning_logic_root, fg="dark blue", font='Helvetica 11 bold',
                                             textvariable=self.tmp_all_words_counter)
        self.label_all_words_counter.grid(row=7, column=1)

    def change_label_report_correctly_words(self):
        self.label_correctly_words_counter = Label(self.learning_logic_root, fg="green", font='Helvetica 11 bold',
                                                   textvariable=self.tmp_correctly_words_counter)
        self.label_correctly_words_counter.grid(row=7, column=2)

    def change_label_report_incorrectly_words(self):
        self.label_incorrectly_words_counter = Label(self.learning_logic_root, fg="red", font='Helvetica 11 bold',
                                                     textvariable=self.tmp_incorrectly_words_counter)
        self.label_incorrectly_words_counter.grid(row=7, column=3)

    def change_label_user_answer(self):
        self.label_user_wrote_answer = Label(self.learning_logic_root, fg="black", font='Helvetica 11 bold',
                                             textvariable=self.tmp_user_wrote_answer)
        self.label_user_wrote_answer.grid(row=4, column=5)

    def change_label_good_bad_view_answer(self):
        self.label_good_bad_answer = Label(self.learning_logic_root, fg=self.tmp_color_and_good_bad_answer,
                                           font='Helvetica 11 bold',
                                           textvariable=self.tmp_label_good_bad_answer)
        self.label_good_bad_answer.grid(row=5, column=3)
