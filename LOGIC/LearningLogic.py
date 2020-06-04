import os
from random import randint


class LearningLogic:
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
    all_words_list_copy = None
    # Actual get word
    actual_word = None

    def set_main_pop(self, main_root):
        # Default window size
        window_width = 1200
        window_height = 620
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
        read_data = "".join(tmp.split())
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
                words_list.append([polish_words, english_words, 0, 0, 0])
                flag = False
                polish_words = ""
                english_words = ""
            self.all_words_list = words_list.copy()

        return self.mixing_words(words_list.copy())

    def mixing_words(self, words_list):
        new_words_list = []
        size_list = words_list.__len__()
        for i in range(0, words_list.__len__()):
            draw_choose = randint(0, words_list.__len__() - 1)
            new_words_list.append(words_list[draw_choose].copy())
            words_list.pop(draw_choose)
            size_list -= 1
        self.all_words_list_copy = new_words_list.copy()

        self.actual_word = self.all_words_list_copy[0]
        self.all_words_list_copy[0].pop()

        if self.actual_language_version == "Polish version":

            return self.actual_word[0]
        elif self.actual_language_version == "English version":
            return self.actual_word[1]

    def check_button(self, polish_entry, english_entry):
        polish_entry = "".join(polish_entry).replace(" ", "")
        english_entry = "".join(english_entry).replace(" ", "")

        if self.actual_language_version == "Polish version":
            if english_entry == "".join(self.actual_word[1].split()):
                print("Dobre słowo po Angielsku")
                pass
            else:
                print("Złe słowo po Angielsku")
                pass
        elif self.actual_language_version == "English version":
            # tmp = "".join(polish_entry).replace(" ", "")
            # tmp1 = "".join(self.actual_word[0].split())
            # print(tmp)
            # print(tmp1)
            if polish_entry == "".join(self.actual_word[0].split()):
                print("Dobre słowo po Polsku")
                pass
            else:
                print("Złe słowo po Polsku")
                pass

    def close_Learning_window(self):
        self.words_window_root.destroy()
        self.main_root.destroy()
