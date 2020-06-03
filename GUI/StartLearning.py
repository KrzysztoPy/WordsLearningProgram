from LOGIC.LearningLogic import *
from tkinter import *
from termcolor import colored


class StartLearning(LearningLogic):
    l_logic = LearningLogic()

    # MainMenu root
    main_root = None
    # StartLearning root
    learning_root = None

    # Main def
    def start_learning_menu(self, root):
        # set var root from main root
        self.main_root = root

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

        #
        self.learning_butt()
        #
        self.learning_field()

    def learning_combo_box(self):
        file_lists = self.l_logic.file_list()
        clicked_file = StringVar()
        clicked_file.set(file_lists[0])

        choice_file = OptionMenu(self.learning_root, clicked_file, *file_lists)
        choice_file.grid(row=1, column=1, ipadx=65)

    def learning_label(self):
        # Empty label
        empty_before_report_label = Label(self.learning_root, text="")
        empty_before_report_label.grid(row=2, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=4, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=6, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=10, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=11, column=0, ipadx=65)

        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=14, column=0, ipadx=65)
        empty_after_report_label = Label(self.learning_root, text="")
        empty_after_report_label.grid(row=15, column=0, ipadx=65)
        # /#

        set_file = Label(self.learning_root, font='Helvetica 11 bold', text="Choice words list name ")
        set_file.grid(row=0, column=1)

        # General report label
        rap_count_word = Label(self.learning_root, font='Helvetica 11 bold', text="Words report ->>> ")
        rap_count_word.grid(row=12, column=0)

        rap_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold', text="Words counter ---> ")
        rap_count_word.grid(row=13, column=1)

        rap_words_completed = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                    text="Words correctly ---> ")
        rap_words_completed.grid(row=13, column=2)

        rap_count_word = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                               text="Words incorrectly --->")
        rap_count_word.grid(row=13, column=3)

        sent_rap_word_complied = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                       text="Words completed --->")
        sent_rap_word_complied.grid(row=13, column=4)
        # /#

        # Sentence report label
        rap_count_word = Label(self.learning_root, font='Helvetica 11 bold', text="Sentence report ->>> ")
        rap_count_word.grid(row=16, column=0)

        sent_rap_counter = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                 text="Sentence counter ---> ")
        sent_rap_counter.grid(row=17, column=1)

        sent_rap_well = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                              text="Sentence correctly ---> ")
        sent_rap_well.grid(row=17, column=2)

        sent_rap_bad = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                             text="Sentence incorrectly ---> ")
        sent_rap_bad.grid(row=17, column=3)

        sent_rap_when_complied = Label(self.learning_root, fg="dark blue", font='Helvetica 11 bold',
                                       text="Sentence completed ---> ")
        sent_rap_when_complied.grid(row=17, column=4)

        # Words label
        label_polish_word = Label(self.learning_root, font='Helvetica 11 bold', text="Polish version ---> ")
        label_polish_word.grid(row=3, column=0)

        label_english_word = Label(self.learning_root, font='Helvetica 11 bold', text="English version ---> ")
        label_english_word.grid(row=3, column=2)
        # /#

        # Sentence label
        label_polish_sentence = Label(self.learning_root, font='Helvetica 11 bold', text="Polish sentence version ")
        label_polish_sentence.grid(row=8, column=0)

        label_english_sentence = Label(self.learning_root, font='Helvetica 11 bold', text="English sentence version ")
        label_english_sentence.grid(row=9, column=0)

    def learning_butt(self):
        butt_load = Button(self.learning_root, font='Helvetica 11 bold', text="Load")
        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_load.grid(row=1, column=2, ipadx=70, pady=0)

        butt_word_check = Button(self.learning_root, font='Helvetica 11 bold', text="Words Check")
        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_word_check.grid(row=3, column=4, ipadx=70, pady=0)

        butt_sentence_check = Button(self.learning_root, font='Helvetica 11 bold',
                                     text="Sentence Check")
        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_sentence_check.grid(row=9, column=4, ipadx=70, pady=0)

    def learning_field(self):
        # Words Label
        entry_polish_word = Entry(self.learning_root, width=25, bd=5)
        entry_polish_word.grid(row=3, column=1, ipadx=25, pady=25)

        entry_english_word = Entry(self.learning_root, width=25, bd=5)
        entry_english_word.grid(row=3, column=3, ipadx=25, pady=25)
        # /#

        entry_polish_sentence = Entry(self.learning_root, width=25, bd=5)
        entry_polish_sentence.grid(row=8, column=1, ipadx=225, pady=25, columnspan=3)

        entry_english_sentence = Entry(self.learning_root, width=25, bd=5)
        entry_english_sentence.grid(row=9, column=1, ipadx=225, pady=25, columnspan=3)
