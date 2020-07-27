import math
import os
from random import randint


class LearningLogic:
    POLISH_VERSION = "Polish version"
    ENGLISH_VERSION = "English version"
    GOOD_ANSWER = "Good answer"
    BAD_ANSWER = "Bad answer"
    COLOR_GREEN = "Green"
    COLOR_RED = "Red"

    words_counter = 0
    words_correctly = 0
    words_incorrectly = 0

    answer_for_question = None

    show_whole_dir_in_file = None
    dir_name_with_words_lists = "../Words list"

    label_version_language = ["English version", "Polish version"]
    actual_language_version = label_version_language[1]
    currently_language_flag = False

    whole_words_list = []
    whole_words_after_mix = None

    actual_choice_word = []
    number_word = 0

    view_whether_good_bad_answer = None
    view_color_good_bad_answer = "Black"
    code_end = "Error 404"
    end_words = "End of words"

    def __del__(self):
        pass

    def set_size_main_pop(self, main_root):
        window_width = 1300
        window_height = 310
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def indication_file_with_words(self):
        path_to_file = os.path.realpath(__file__)

        for i in path_to_file[::-1]:
            if i == "\\":
                break
            else:
                path_to_file = path_to_file[:-1]

        path_to_file += self.dir_name_with_words_lists
        return path_to_file

    def show_whole_file_in_file(self):
        show_whole_file_in_file = os.listdir(self.indication_file_with_words())
        if show_whole_file_in_file.__len__() == 0:
            show_whole_file_in_file.append("Empty")
        return show_whole_file_in_file

    def set_version_label(self):
        # Sets again pointer to first word
        self.number_word = 0

    def clear_to_first_position(self):
        # Sets again pointer to first word
        self.number_word = 0
        self.words_correctly = 0
        self.words_incorrectly = 0
        self.answer_for_question = ""

    def change_language_answer(self):
        if self.actual_language_version == self.label_version_language[1]:
            self.actual_language_version = self.label_version_language[0]
            return self.label_version_language[0]
        else:
            self.actual_language_version = self.label_version_language[1]
            return self.label_version_language[1]

    def load_clicked_file(self, file_name) -> str:
        path_to_file = self.indication_file_with_words() + "\\" + file_name
        list_words = open(path_to_file, "r", encoding="utf=8")
        tmp = list_words.read()
        read_data = "".join(tmp.splitlines())

        if read_data == "":
            self.clear_all_word_list_variable()
            return "Directory is empty!"
        else:
            return str(self.set_load_words(read_data))

    def set_load_words(self, file_data):
        # words_list = []
        all_polish_words_translations = []
        all_english_words_translations = []
        flag_end_words = False
        polish_words = ""
        english_words = ""
        for j in file_data:
            if j != "|" and flag_end_words == False and j != ";":
                if j == ",":
                    all_polish_words_translations.append(polish_words)
                    polish_words = ""
                    # polish_words += j + " "
                else:
                    polish_words += j
            elif j == "|":
                all_polish_words_translations.append(polish_words)
                flag_end_words = True
            elif j != "|" and flag_end_words == True and j != ";":
                if j == ",":
                    all_english_words_translations.append(english_words)
                    english_words = ""
                    # english_words += j + " "
                else:
                    english_words += j
            elif j == ";":
                all_english_words_translations.append(english_words)
                self.whole_words_list.append(
                    [all_polish_words_translations.copy(), all_english_words_translations.copy()])
                all_polish_words_translations.clear()
                all_english_words_translations.clear()
                flag_end_words = False
                polish_words = ""
                english_words = ""

        self.words_counter = self.whole_words_list.__len__()

        return self.mixing_words_after_load(self.whole_words_list.copy())

    def mix_words_after_change_language(self):
        if not self.whole_words_list:
            return ""
        else:
            return self.mixing_words_after_load(self.whole_words_list.copy())

    def mixing_words_after_load(self, words_list):

        mix_words_list = []
        size_list = words_list.__len__()
        for i in range(0, words_list.__len__()):
            draw_choose = randint(0, words_list.__len__() - 1)
            mix_words_list.append(words_list[draw_choose].copy())
            words_list.pop(draw_choose)
            size_list -= 1
        self.whole_words_after_mix = mix_words_list.copy()
        mix_words_list.clear()

        self.actual_choice_word = self.whole_words_after_mix[0]

        if self.actual_language_version == self.POLISH_VERSION:
            convert_list_to_str = ""
            for i in self.actual_choice_word[1]:
                convert_list_to_str += i
            return convert_list_to_str
        elif self.actual_language_version == self.ENGLISH_VERSION:
            convert_list_to_str = ""
            for i in self.actual_choice_word[0]:
                convert_list_to_str += i
            return convert_list_to_str

    def check_correctness_word(self, words_entry, word_label):
        particular_word_correctly = 0
        insertion_into_list_entry_words = []
        individual_word = ""

        if word_label != "End of words" or self.whole_words_list is None:
            if self.whole_words_after_mix:
                actual_trans_word = self.whole_words_after_mix[self.number_word]
                if self.whole_words_list:
                    words_entry = "".join(words_entry).replace(" ", "")
                for i, word in enumerate(words_entry):
                    if word != ",":
                        individual_word += word
                        if i == words_entry.__len__() - 1:
                            insertion_into_list_entry_words.append(individual_word)
                            individual_word = ""
                    elif word == ",":
                        insertion_into_list_entry_words.append(individual_word)
                        individual_word = ""

                if self.actual_language_version == self.POLISH_VERSION:
                    for tmp_word_translation in actual_trans_word[0]:
                        for tmp_entry_words in insertion_into_list_entry_words:
                            if tmp_entry_words.lower() == "".join(tmp_word_translation.split()).lower():
                                particular_word_correctly += 1
                                break
                    if particular_word_correctly >= math.ceil((len(actual_trans_word[0]) * 0.6)):
                        self.words_correctly += 1
                        self.view_whether_good_bad_answer = self.GOOD_ANSWER
                        self.view_color_good_bad_answer = self.COLOR_GREEN
                    else:
                        self.words_incorrectly += 1
                        self.view_whether_good_bad_answer = self.BAD_ANSWER
                        self.view_color_good_bad_answer = self.COLOR_RED

                elif self.actual_language_version == self.ENGLISH_VERSION:
                    for tmp_word_translation in actual_trans_word[1]:
                        for tmp_entry_words in insertion_into_list_entry_words:
                            if tmp_entry_words.lower() == "".join(tmp_word_translation.split()).lower():
                                particular_word_correctly += 1
                                break
                    if particular_word_correctly >= math.ceil((len(actual_trans_word[1]) * 0.6)):
                        self.words_correctly += 1
                        self.view_whether_good_bad_answer = self.GOOD_ANSWER
                        self.view_color_good_bad_answer = self.COLOR_GREEN
                    else:
                        self.words_incorrectly += 1
                        self.view_whether_good_bad_answer = self.BAD_ANSWER
                        self.view_color_good_bad_answer = self.COLOR_RED
        else:
            # Nothing to do
            pass

    def load_next_word(self):
        if self.whole_words_after_mix:
            self.number_word += 1
            if self.number_word >= self.whole_words_after_mix.__len__():
                self.number_word -= 1
                return self.end_words
            else:
                self.actual_choice_word = self.whole_words_after_mix[self.number_word]
                if self.actual_language_version == self.POLISH_VERSION:
                    return self.actual_choice_word[1]
                elif self.actual_language_version == self.ENGLISH_VERSION:
                    return self.actual_choice_word[0]

    def set_correct_answer_for_question(self, word_label):
        tmp_answer_for_question = ""
        if word_label == "End of words":
            self.answer_for_question = "End of words"
            return self.currently_answer()
        else:
            if self.whole_words_list:
                if self.actual_language_version == self.POLISH_VERSION:
                    for i, convert_to_string in enumerate(self.actual_choice_word[0]):
                        if i < len(self.actual_choice_word[0]) - 1:
                            tmp_answer_for_question += convert_to_string + ","
                        else:
                            tmp_answer_for_question += convert_to_string
                    self.actual_choice_word = self.whole_words_after_mix[self.number_word]
                    self.answer_for_question = tmp_answer_for_question
                    return self.currently_answer()

                elif self.actual_language_version == self.ENGLISH_VERSION:
                    for i, convert_to_string in enumerate(self.actual_choice_word[1]):
                        if i < len(self.actual_choice_word[1]) - 1:
                            tmp_answer_for_question += convert_to_string + ","
                        else:
                            tmp_answer_for_question += convert_to_string
                    self.actual_choice_word = self.whole_words_after_mix[self.number_word]
                    self.answer_for_question = tmp_answer_for_question
                    return self.currently_answer()

    def set_label_user_answer(self, user_answer):
        return str(user_answer)

    def report_counter_set(self):
        return "Words counter: " + str(self.words_counter)

    def report_correctly_set(self):
        return "Words correctly: " + str(self.words_correctly)

    def report_incorrectly_set(self):
        return "Words incorrectly: " + str(self.words_incorrectly)

    def currently_answer(self):
        return self.answer_for_question

    def set_label_whether_good_bad_answer(self):
        return self.view_whether_good_bad_answer

    def set_label_good_bad_answer_color(self):
        return self.view_color_good_bad_answer

    def clear_all_word_list_variable(self):
        self.whole_words_list.clear()
        self.whole_words_after_mix = None
        self.actual_choice_word.clear()
        self.clear_to_first_position()

    def close_Learning_window(self, top_window, main_window, l_logic):
        top_window.destroy()
        main_window.deiconify()
        # self.words_window_root.destroy()
        # self.main_root.destroy()
