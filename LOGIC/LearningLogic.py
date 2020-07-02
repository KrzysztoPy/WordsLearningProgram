import os
from random import randint


class LearningLogic:
    POLISH_VERSION = "Polish version"
    ENGLISH_VERSION = "English version"

    # Raport variable
    words_counter = 0
    words_correctly = 0
    words_incorrectly = 0
    # Correct answer
    curr_ans = None

    # Variable with all file list
    file_list = None
    # Directory name where is all file
    dir_name = "Words list"

    # Button English/Polish version
    label_version = ["English version", "Polish version"]
    label_version_flag = False

    # words list
    ext_word_list = None
    actual_language_version = label_version[1]

    # Stores all words from file
    all_words_list = None
    all_words_mix_list = None
    # Actual get word
    actual_choice_word = None
    number_word = 0

    code_end = "Error 404"
    end_words = "End of words"

    def set_main_pop(self, main_root):
        # Default window size
        window_width = 1200
        window_height = 310
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def list_path(self):
        tmp_path = os.path.realpath(__file__)

        for i in tmp_path[::-1]:
            if i == "\\":
                break
            else:
                tmp_path = tmp_path[:-1]

        tmp_path += self.dir_name
        return tmp_path

    def file_list(self):
        self.file_list = os.listdir(self.list_path())

        if self.file_list.__len__() == 0:
            self.file_list.append("Empty")
        return self.file_list

    def set_version_label(self):
        # Sets again pointer to first word
        self.number_word = 0
        self.words_correctly = 0
        self.words_incorrectly = 0
        self.curr_ans = ""
    def change_language(self):
        if not self.label_version_flag:
            self.label_version_flag = True
            self.actual_language_version = self.label_version[0]
            return self.label_version[0]
        elif self.label_version_flag:
            self.label_version_flag = False
            self.actual_language_version = self.label_version[1]
            return self.label_version[1]

    def load_file_butt(self, file_name) -> str:
        tmp_path = self.list_path() + "\\" + file_name
        list_words = open(tmp_path, "r", encoding="utf=8")
        tmp = list_words.read()
        read_data = "".join(tmp.splitlines())

        if read_data == "":
            self.clear_all_word_list_variable()
            if self.label_version == self.POLISH_VERSION:
                return "Folder jest pusty!"
            elif self.label_version == self.ENGLISH_VERSION:
                return "Directory is empty!"
        else:
            return str(self.set_words(read_data))

    def set_words(self, file_data):

        words_list = []
        flag = False
        polish_words = ""
        english_words = ""
        # dom,ojczyzna|home
        for j in file_data:
            if j != "|" and flag == False and j != ";":
                if j == ",":
                    polish_words += j + " "
                else:
                    polish_words += j
            elif j == "|":
                flag = True
            elif j != "|" and flag == True and j != ";":
                if j == ",":
                    english_words += j + " "
                else:
                    english_words += j
            elif j == ";":
                words_list.append([polish_words, english_words])
                flag = False
                polish_words = ""
                english_words = ""
            self.all_words_list = words_list.copy()

            self.words_counter = self.all_words_list.__len__()

        return self.mixing_words(self.all_words_list.copy())

    def change_butt_mixing(self):
        if not self.all_words_list:
            return ""
        else:
            return self.mixing_words(self.all_words_list.copy())

    def mixing_words(self, words_list):

        mix_words_list = []
        size_list = words_list.__len__()
        for i in range(0, words_list.__len__()):
            draw_choose = randint(0, words_list.__len__() - 1)
            mix_words_list.append(words_list[draw_choose].copy())
            words_list.pop(draw_choose)
            size_list -= 1
        self.all_words_mix_list = mix_words_list.copy()
        mix_words_list.clear()

        self.actual_choice_word = self.all_words_mix_list[0]

        if self.actual_language_version == self.POLISH_VERSION:
            return self.actual_choice_word[1]
        elif self.actual_language_version == self.ENGLISH_VERSION:
            return self.actual_choice_word[0]

    # Check from which field get text, and compare with actual translate word
    def check_button(self, words_entry, word_label):
        if word_label != "End of words" or self.all_words_list is None:
            if self.all_words_mix_list:
                actual_trans_word = self.all_words_mix_list[self.number_word]
                if self.all_words_list:
                    words_entry = "".join(words_entry).replace(" ", "")

                if self.actual_language_version == self.POLISH_VERSION:
                    if words_entry.lower() == "".join(actual_trans_word[0].split()).lower():
                        self.words_correctly += 1
                    else:
                        self.words_incorrectly += 1
                elif self.actual_language_version == self.ENGLISH_VERSION:
                    if words_entry.lower() == "".join(actual_trans_word[1].split()).lower():
                        self.words_correctly += 1
                    else:
                        self.words_incorrectly += 1
        else:
            # Nothing to do
            pass

            # Set next word (actual_choice_word)

    def load_next_word(self):
        if self.all_words_mix_list:
            self.number_word += 1
            if self.number_word >= self.all_words_mix_list.__len__():
                self.number_word -= 1
                return self.end_words
            else:
                self.actual_choice_word = self.all_words_mix_list[self.number_word]
                # self.actual_translate_word = self.all_words_mix_list[self.number_word]
                if self.actual_language_version == self.POLISH_VERSION:
                    return self.actual_choice_word[1]
                elif self.actual_language_version == self.ENGLISH_VERSION:
                    return self.actual_choice_word[0]

    # View a correct word version
    def set_label_text_curr_ans(self, word_label):
        if word_label == "End of words":
            self.curr_ans = "End of words"
            return self.currently_answer()
        else:
            if self.all_words_list:
                if self.actual_language_version == self.POLISH_VERSION:
                    self.curr_ans = self.actual_choice_word[0]
                    self.actual_choice_word = self.all_words_mix_list[self.number_word]
                    return self.currently_answer()
                elif self.actual_language_version == self.ENGLISH_VERSION:
                    self.curr_ans = self.actual_choice_word[1]
                    self.actual_choice_word = self.all_words_mix_list[self.number_word]
                    return self.currently_answer()

    def report_counter_set(self):
        return "Words counter: " + str(self.words_counter)

    def report_correctly_set(self):
        return "Words correctly: " + str(self.words_correctly)

    def report_incorrectly_set(self):
        return "Words incorrectly: " + str(self.words_incorrectly)

    def currently_answer(self):
        return self.curr_ans

    def clear_all_word_list_variable(self):
        self.all_words_list = None
        self.all_words_mix_list = None
        self.actual_choice_word = None
        self.set_version_label()

    def close_Learning_window(self):
        self.words_window_root.destroy()
        self.main_root.destroy()
