from LOGIC.LearningLogic import *
from tkinter import *


class GuiLearning(LearningLogic):
    l_logic = LearningLogic()

    # MainMenu root
    main_root = None
    # StartLearning root
    learning_root = None

    # Label and variable text words to translate
    lab_wid_quest_word = None
    text_lab_quest_word = None

    # Label language changer
    Label_text_language_version = None

    # changed Label Words and Correct

    text_quest_word = None
    correct_answer = None
    text_correct_answer = None

    # StringVar fill OptionMenu
    clicked_file = None
    # List with external words
    external_words = None
    # Global set entry
    words_entry = None
    entry_english_word = None

    # Good || Wrong answer variable
    good_answer = None
    wrong_answer = None

    # Edit widget text
    label_text_version_word = None

    label_text_curr_ans = None

    # Edit widget text (Report)
    words_counter = None
    words_correctly = None
    words_incorrectly = None

    # Widged report editor
    var_rep_count_word = None
    var_rep_words_correctly = None
    var_rep_words_incorrectly = None

    butt_back = None

    # Main def
    def start_learning_menu(self, root):
        # set var root from main root
        self.main_root = root

        # Edit widget text
        self.label_text_version_word = StringVar()
        self.text_lab_quest_word = StringVar()
        self.label_text_curr_ans = StringVar()

        # Edit widget text (Report)
        self.words_counter = StringVar()
        self.words_correctly = StringVar()
        self.words_incorrectly = StringVar()

        self.learning_root = Toplevel(self.main_root)
        # Set window size
        self.learning_root.geometry(self.l_logic.set_main_pop(self.main_root))
        # Lock resizable
        self.learning_root.resizable(width=False, height=False)
        # Set menu window invisible
        self.main_root.withdraw()

        # Set combobox
        self.learning_combo_box()

        # Set Label
        self.learning_label()

        self.learning_field()
        #
        self.learning_butt()
        self.learning_root.bind('<Return>', self.butt_word_check_command)

        #

    def learning_combo_box(self):
        file_lists = self.l_logic.file_list()
        self.clicked_file = StringVar()
        self.clicked_file.set(file_lists[0])

        choice_file = OptionMenu(self.learning_root, self.clicked_file, *file_lists)
        choice_file.grid(row=1, column=0, ipadx=65)

    def learning_label(self):
        # Empty label
        empty_before_report_label = Label(self.learning_root, text="")
        empty_before_report_label.grid(row=2, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=3, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=3, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=4, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=6, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=8, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=10, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=11, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=14, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=15, column=0, ipadx=65)

        label_text_word = Label(self.learning_root, font='Helvetica 11 bold', text="")
        label_text_word.grid(row=4, column=1, columnspan=2)
        # /#

        set_file = Label(self.learning_root, font='Helvetica 11 bold', text="Choice words list name ")
        set_file.grid(row=0, column=0)

        word_sent_version = Label(self.learning_root, font='Helvetica 11 bold',
                                  text="Answer in language: ")
        word_sent_version.grid(row=1, column=2)

        self.Label_text_language_version = Label(self.learning_root, font='Helvetica 11 bold',
                                                 text="Polish version")
        self.Label_text_language_version.grid(row=1, column=3)

        # From file text word
        label_text_word = Label(self.learning_root, font='Helvetica 11 bold', text="Words: ")
        label_text_word.grid(row=4, column=0)

        self.correct_answer = Label(self.learning_root, fg="green", font='Helvetica 11 bold', text="Correct answer: ")
        self.correct_answer.grid(row=4, column=2)
        # /#
        # Words label
        label_polish_word = Label(self.learning_root, font='Helvetica 11 bold', text="Polish version ---> ")
        label_polish_word.grid(row=5, column=0)

        # /#
        # Words report label
        rep_count_word = Label(self.learning_root, font='Helvetica 11 bold', text="Words report ->>> ")
        rep_count_word.grid(row=7, column=0)

        self.var_rep_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                        text="Words counter: 0")
        self.var_rep_count_word.grid(row=7, column=1)

        self.var_rep_words_correctly = Label(self.learning_root, fg="green", font='Helvetica 11 bold',
                                             text="Words correctly: 0")
        self.var_rep_words_correctly.grid(row=7, column=2)

        self.var_rep_words_incorrectly = Label(self.learning_root, fg="red", font='Helvetica 11 bold',
                                               text="Words incorrectly: 0")

        self.var_rep_words_incorrectly.grid(row=7, column=3)

    def learning_butt(self):
        butt_load = Button(self.learning_root, font='Helvetica 11 bold', text="Load",
                           command=lambda: [
                               self.l_logic.clear_all_word_list_variable(),
                               self.text_lab_quest_word.set(self.l_logic.load_file_butt(self.clicked_file.get())),
                               self.words_counter.set(self.l_logic.report_counter_set()),
                               self.words_correctly.set(self.l_logic.report_correctly_set()),
                               self.words_incorrectly.set(self.l_logic.report_incorrectly_set()),
                               self.label_text_curr_ans.set(self.l_logic.currently_answer()),

                               self.var_word_label(),
                               self.var_report_count(),
                               self.var_report_correctly(),
                               self.var_report_incorrectly(),
                               self.var_current_answer(),

                           ])
        butt_load.grid(row=1, column=1, ipadx=70, pady=0)

        version_butt = Button(self.learning_root, font='Helvetica 11 bold', text="Change",
                              command=lambda:
                              [self.l_logic.change_language(),
                               self.label_text_version_word.set(self.l_logic.set_version_label()),
                               self.text_lab_quest_word.set(self.l_logic.change_butt_mixing()),
                               self.var_language_words(),
                               self.words_correctly.set(self.l_logic.report_correctly_set()),
                               self.words_incorrectly.set(self.l_logic.report_incorrectly_set()),
                               self.label_text_curr_ans.set(self.l_logic.currently_answer()),
                               self.var_report_correctly(),
                               self.var_report_incorrectly(),
                               self.var_current_answer()
                               ])

        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        version_butt.grid(row=1, column=4, ipadx=70, pady=0)

        butt_word_check = Button(self.learning_root, font='Helvetica 11 bold', text="Words Check",
                                 command=lambda:
                                 [self.l_logic.check_button(self.words_entry.get(),
                                                            self.text_lab_quest_word.get()),
                                  # Set widget and go to next words
                                  self.label_text_curr_ans.set(
                                      self.l_logic.set_label_text_curr_ans(self.text_lab_quest_word.get())),
                                  # Set widget
                                  self.text_lab_quest_word.set(self.l_logic.load_next_word()),
                                  self.words_correctly.set(self.l_logic.report_correctly_set()),
                                  self.words_incorrectly.set(self.l_logic.report_incorrectly_set()),
                                  self.var_current_answer(),
                                  self.var_word_label(),
                                  self.var_report_correctly(),
                                  self.var_report_incorrectly()

                                  ])
        butt_word_check.grid(row=5, column=2, ipadx=70, pady=0)
        self.butt_back = Button(self.learning_root, font='Helvetica 11 bold',
                                text="BACK", command=self.l_logic.close_Learning_window)

        self.butt_back.grid(row=9, column=0, ipadx=70, pady=0)

    # Label change language

    def butt_word_check_command(self, event):
        self.l_logic.check_button(self.words_entry.get(), self.text_lab_quest_word.get())
        self.label_text_curr_ans.set(self.l_logic.set_label_text_curr_ans(self.text_lab_quest_word.get()))
        # Set widget
        self.text_lab_quest_word.set(self.l_logic.load_next_word())
        self.words_correctly.set(self.l_logic.report_correctly_set()),
        self.words_incorrectly.set(self.l_logic.report_incorrectly_set()),
        self.var_current_answer(),
        self.var_word_label(),
        self.var_report_correctly(),
        self.var_report_incorrectly()

    def var_language_words(self):
        self.Label_text_language_version = Label(self.learning_root, font='Helvetica 11 bold',
                                                 textvariable=self.label_text_version_word)
        self.Label_text_language_version.grid(row=1, column=3)

    # Label change translated word
    def var_word_label(self):
        # From file text word
        self.lab_wid_quest_word = Label(self.learning_root, font='Helvetica 11 bold', fg="dark blue",
                                        textvariable=self.text_lab_quest_word)
        self.lab_wid_quest_word.grid(row=4, column=1)

    # Label change correct answer ( dynamic view)
    def var_current_answer(self):
        self.Label_text_language_version = Label(self.learning_root, font='Helvetica 11 bold',
                                                 textvariable=self.label_text_curr_ans)
        self.Label_text_language_version.grid(row=4, column=3)

    def var_report_count(self):
        self.var_rep_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                        textvariable=self.words_counter)
        self.var_rep_count_word.grid(row=7, column=1)

    def var_report_correctly(self):
        self.var_rep_words_correctly = Label(self.learning_root, fg="green", font='Helvetica 11 bold',
                                             textvariable=self.words_correctly)
        self.var_rep_words_correctly.grid(row=7, column=2)

    def var_report_incorrectly(self):
        self.var_rep_words_incorrectly = Label(self.learning_root, fg="red", font='Helvetica 11 bold',
                                               textvariable=self.words_incorrectly)
        self.var_rep_words_incorrectly.grid(row=7, column=3)

    def learning_field(self):
        # Words Label
        self.words_entry = Entry(self.learning_root, width=25, bd=5)
        self.words_entry.grid(row=5, column=1, ipadx=25, pady=25)
