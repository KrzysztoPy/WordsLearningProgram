from LOGIC.LearningLogic import *
from tkinter import *


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
        # Set menu window invisible
        self.main_root.withdraw()

        # Set combobox
        self.learning_combo_box()

        # Set Label
        self.learning_label()

        #
        self.learning_butt()

    def learning_combo_box(self):
        clicked_file = StringVar()
        clicked_file.set("Empty")

        choice_file = OptionMenu(self.learning_root, clicked_file, "Empty")
        choice_file.grid(row=1, column=1, ipadx=65)

    def learning_label(self):
        # Empty label
        empty_label1 = Label(self.learning_root, text="")
        empty_label1.grid(row=0, column=0, ipadx=65)
        empty_label2 = Label(self.learning_root, text="")
        empty_label2.grid(row=1, column=0, ipadx=65)
        empty_label3 = Label(self.learning_root, text="")
        empty_label3.grid(row=3, column=0, ipadx=65)

        set_file = Label(self.learning_root, text="Choice words list name ")
        set_file.grid(row=0, column=1)

        # Raport label
        rap_counter_word = Label(self.learning_root, text="Raport ->>> ")
        rap_counter_word.grid(row=4, column=0)

        rap_counter_word = Label(self.learning_root, text="Word counter: ")
        rap_counter_word.grid(row=4, column=1)

        rap_words_completed = Label(self.learning_root, text="Words completed: ")
        rap_words_completed.grid(row=4, column=2)
        pass

    def learning_butt(self):
        butt_load = Button(self.learning_root, text="Load")
        # ,command=lambda: [self.set_table(),self.set_value_table(self.logic.load_butt(self.clicked_file.get()))])
        butt_load.grid(row=1, column=2, ipadx=70, pady=0)
        pass

    def learning_field(self):
        pass
