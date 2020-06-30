from LOGIC.LearningLogic import *
from tkinter import *


class GuiLearning(LearningLogic):
    l_logic = LearningLogic()

    # MainMenu root
    main_root = None
    # StartLearning root
    learning_root = None

    # Sentence and words list
    words_list = []
    sentence_list = []

    # for change button version name

    word_sent_version_chose = None

    # changed Label Words and Correct
    quest_word = None
    text_quest_word = None
    correct_answer = None
    text_correct_answer = None
    # StringVar fill OptionMenu
    clicked_file = None
    # List with external words
    external_words = None
    # Global set entry
    entry_polish_word = None
    entry_english_word = None

    # Good || Wrong answer variable
    good_answer = None
    wrong_answer = None

    # Edit widget text
    version_label_text_word = None
    view_tmp_word_label = None
    label_text_curr_ans = None

    # Edit widget text (Report)
    words_counter = None
    words_correctly = None
    words_incorrectly = None

    # Main def
    def start_learning_menu(self, root):
        # set var root from main root
        self.main_root = root

        # Edit widget text
        self.version_label_text_word = StringVar()
        self.view_tmp_word_label = StringVar()
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

        self.word_sent_version_chose = Label(self.learning_root, font='Helvetica 11 bold',
                                             text="Polish version")
        self.word_sent_version_chose.grid(row=1, column=3)

        # From file text word
        label_text_word = Label(self.learning_root, font='Helvetica 11 bold', text="Words: ")
        label_text_word.grid(row=4, column=0)

        self.correct_answer = Label(self.learning_root, fg="green", font='Helvetica 11 bold', text="Correct answer: ")
        self.correct_answer.grid(row=4, column=3)
        # /#
        # Words label
        label_polish_word = Label(self.learning_root, font='Helvetica 11 bold', text="Polish version ---> ")
        label_polish_word.grid(row=5, column=0)

        label_english_word = Label(self.learning_root, font='Helvetica 11 bold', text="English version ---> ")
        label_english_word.grid(row=5, column=2)
        # /#
        # Words report label
        rap_count_word = Label(self.learning_root, font='Helvetica 11 bold', text="Words report ->>> ")
        rap_count_word.grid(row=7, column=0)

        rap_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold', text="Words counter ---> ")
        rap_count_word.grid(row=8, column=1)

        rap_words_completed = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                    text="Words correctly ---> ")
        rap_words_completed.grid(row=8, column=2)

        rap_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                               text="Words incorrectly --->")
        rap_count_word.grid(row=8, column=3)
        # /#
        # Good || Wrong answer

    def learning_butt(self):
        butt_load = Button(self.learning_root, font='Helvetica 11 bold', text="Load",
                           command=lambda: [
                               self.view_tmp_word_label.set(self.l_logic.load_file_butt(self.clicked_file.get())),
                               self.tmp_word_label()])
        butt_load.grid(row=1, column=1, ipadx=70, pady=0)

        version_butt = Button(self.learning_root, font='Helvetica 11 bold', text="Change",
                              command=lambda:
                              [self.version_label_text_word.set(self.l_logic.set_version_label()),
                               self.view_tmp_word_label.set(self.l_logic.change_butt_mixing()),
                               self.tmp_language_words()])

        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        version_butt.grid(row=1, column=4, ipadx=70, pady=0)

        butt_word_check = Button(self.learning_root, font='Helvetica 11 bold', text="Words Check",
                                 command=lambda:
                                 [self.l_logic.check_button(self.entry_polish_word.get(),
                                                            self.entry_english_word.get()),
                                  self.label_text_curr_ans.set(self.l_logic.set_label_text_curr_ans()),
                                  self.variable_labels_current_answer(),
                                  self.view_tmp_word_label.set(self.l_logic.load_next_word()),
                                  # Niepowinien ponownie wczytywać słów !!!
                                  self.tmp_word_label()])

        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_word_check.grid(row=5, column=4, ipadx=70, pady=0)

        butt_back = Button(self.learning_root, font='Helvetica 11 bold',
                           text="BACK", command=self.l_logic.close_Learning_window)
        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_back.grid(row=9, column=0, ipadx=70, pady=0)

    # Label change language
    def tmp_language_words(self):
        self.word_sent_version_chose = Label(self.learning_root, font='Helvetica 11 bold',
                                             textvariable=self.version_label_text_word)
        self.word_sent_version_chose.grid(row=1, column=3)

    # Label change translated word
    def tmp_word_label(self):
        # From file text word
        self.quest_word = Label(self.learning_root, font='Helvetica 11 bold', fg="dark blue",
                                textvariable=self.view_tmp_word_label)
        self.quest_word.grid(row=4, column=1, columnspan=2)

    # Label change correct answer
    def variable_labels_current_answer(self):
        self.word_sent_version_chose = Label(self.learning_root, font='Helvetica 11 bold',
                                             textvariable=self.label_text_curr_ans)
        self.word_sent_version_chose.grid(row=4, column=4)

    def learning_field(self):
        # Words Label
        self.entry_polish_word = Entry(self.learning_root, width=25, bd=5)
        self.entry_polish_word.grid(row=5, column=1, ipadx=25, pady=25)

        self.entry_english_word = Entry(self.learning_root, width=25, bd=5)
        self.entry_english_word.grid(row=5, column=3, ipadx=25, pady=25)
