from tkinter import *
from pathlib import Path
import os


class WordWindowLogic:
    dir_with_words_list = "../Words list"

    list_all_words_list = []

    actual_select_file = "None"

    all_words_in_select_list = []

    list_with_old_and_new_words = []

    # Create directory when you save new words list
    def create_directory(self):

        file_path = os.path.realpath(__file__)
        for i in file_path[::-1]:
            if i == "\\":
                break
            else:
                file_path = file_path[:-1]
        file_path += self.dir_with_words_list
        Path(file_path).mkdir(exist_ok=True)
        return ["Information", "Directory was created"]  # Do usunięcia

    def save_new_words_list(self, words=[]):
        return words.__len__() < 1

    def xyz(self):
        pass

    def whether_empty(self):
        try:
            check_empty = open('r', "path.txt")

        except FileNotFoundError:
            create = open('w', "path.txt")
            create.write(os.path.dirname(os.path.realpath(__file__)))
            create.close()

    def words_list_path(self):
        tmp_path = os.path.realpath(__file__)

        for i in tmp_path[::-1]:
            if i == "\\":
                break
            else:
                tmp_path = tmp_path[:-1]

        tmp_path += self.dir_with_words_list
        return tmp_path

    def create_file(self, file_name):
        tmp_path = self.words_list_path() + "\\" + file_name
        open(tmp_path, "a").close()
        return ["Information", "The file has been created"]

    def check_have_txt(self, file_name):
        tmp_path = ""
        file_name = file_name[::-1]
        if len(file_name) > 4:
            for i in range(0, 5):
                tmp_path += file_name[i]
            file_name = file_name[::-1]
            if tmp_path == ".txt":
                return file_name
            else:
                return file_name + ".txt"
        else:
            file_name = file_name[::-1]
            return file_name + ".txt"

    def file_list(self):
        self.list_all_words_list = os.listdir(self.words_list_path())

        if self.list_all_words_list.__len__() == 0:
            self.list_all_words_list.append("Empty")
        return self.list_all_words_list

    def file_create(self, file_name):
        if file_name == "":
            return ["Error", "File name can't be empty."]
        elif file_name == ".txt":
            return ["Error", "Prohibited file name: .txt"]
        file_path = self.words_list_path() + "\\" + self.check_have_txt(file_name)
        if os.path.exists(file_path):
            return ["Error", "A file with this name already exists.Choice different name. "]
        else:
            return self.create_file(self.check_have_txt(file_name))

    def open_file_and_return_words_list(self, file_name):
        tmp_path = self.words_list_path() + "\\" + file_name
        list_words = open(tmp_path, "r", encoding="utf=8")
        data_from_file = list_words.read()
        file_data = "".join(data_from_file)
        return self.set_list_with_words_from_file(file_data)

    def actual_select_file_string_set(self, file_name):
        return "Actual select file: " + file_name

    def remove_button(self, file_name):
        tmp_path = self.words_list_path() + "\\" + file_name
        os.remove(tmp_path)

    def set_list_with_words_from_file(self, file_data):

        words_list = []
        flag = FALSE
        polish_words = ""
        polish_all_translations = []
        english_words = ""
        english_all_translations = []

        counter = 1
        for j in file_data:
            if j != "|" and flag == FALSE and j != ";" and j != "\n":
                if j == ",":
                    polish_all_translations.append(polish_words)
                    polish_words = ""
                    # polish_words += j + " "
                else:
                    polish_words += j
            elif j == "|":
                polish_all_translations.append(polish_words)
                polish_words = ""
                flag = TRUE
            elif j != "|" and (flag == True) and j != ";" and j != "\n":
                if j == ",":
                    english_all_translations.append(english_words)
                    english_words = ""
                    # english_words += j + " "
                else:
                    english_words += j
            elif j == ";":
                english_all_translations.append(english_words)
                english_words = ""
                words_list += [counter, polish_all_translations.copy(), english_all_translations.copy()]
                counter += 1

                flag = FALSE
                polish_words = ""
                polish_all_translations.clear()
                english_words = ""
                english_all_translations.clear()
        self.set_all_words_in_select_list(words_list.copy())
        return self.get_all_words_in_select_list()

    def return_words_line(self, counter):
        all_words_on_selected_list = self.get_all_words_in_select_list()

        return (all_words_on_selected_list[counter], ",".join(all_words_on_selected_list[counter + 1]),
                ",".join(all_words_on_selected_list[counter + 2]))

    def check_is_repeating(self, entry_polish_word, entry_english_word):
        isolated_polish_words = []
        isolated_english_words = []
        # for counter in range(0, self.actual_entered_words.len() + 1, 3):
        pass

    def set_all_words_in_select_list(self, all_words_from_selected_list):
        self.all_words_in_select_list = all_words_from_selected_list.copy()

    def get_all_words_in_select_list(self):
        return self.all_words_in_select_list.copy()

    def set_list_with_old_and_new_words(self, set_list_with_old_and_new_words):
        self.set_list_with_old_and_new_words = set_list_with_old_and_new_words

    def get_set_list_with_old_and_new_words(self):
        return self.set_list_with_old_and_new_words

    def check_polish_entry(self, polish_word):
        pass

    def check_english_entry(self, english_word):
        pass

    def check_fields_is_not_empty(self, polish_word, english_word):
        if polish_word == "":
            return ["Error", "Musisz wpisać polską wersje słowa."]
        elif english_word == "":
            return ["Error", "You must writing english word version."]
        # return self.check_change(polish_word, english_word)

    def whether_repeat_words(self, polish_words, english_words):
        polish_repeat = False
        english_repeat = False

        for counter in range(0, self.all_words_in_select_list, 3):
            if polish_words.strip() == self.all_words_in_select_list[counter + 1]:
                polish_repeat = True
            if english_words.strip() == self.all_words_in_select_list[counter + 1]:
                pass  # !!!!!!!!!!!!!!!!!!! NOT ENDING !!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def check_change(self, polish_word, english_word):

        return self.save_to_table(polish_word, english_word)

    def save_to_table(self, polish_word, english_word):
        # tmp_words = []
        # index = 0

        # for counter in range(0, self.all_words_in_select_list.__len__() + 1, 3):
        #     self.all_words_in_select_list[counter]
        # if self.all_words_in_select_list.__len__() > 3:
        #     index = int(tmp_actual_words[tmp_actual_words.__len__() - 3])
        #     for i in range(0, tmp_actual_words.__len__(), 3):
        #         tmp_words.append(tmp_actual_words[i])
        #         tmp_words.append(tmp_actual_words[i + 1])
        #         tmp_words.append(tmp_actual_words[i + 2])
        #
        # tmp_words.append(index + 1)
        # tmp_words.append(polish_word)
        # tmp_words.append(english_word)
        return ["Save", "The word has been added to the list", self.all_words_in_select_list.copy()]

    def remove_word(self):
        pass

    def find_word(self):
        pass

    def close_words_window(self, top_window, main_window):
        top_window.destroy()
        main_window.deiconify()


def test():
    # logic = Logic()
    # # rano|a.m.;około|about;
    # logic.save_to_table("popołudniu", "afternoon", ["1", "rano", "a.m.", "2", "około", "about"])
    # logic.load_butt("bla.txt")
    # path = os.path.realpath(__file__)
    # print(os.path.basename(__file__))
    # print("\\")
    #
    # print(path)
    # print(type(path))
    # print(type(pathlib.Path(__file__).parent.absolute()))
    # bla = "xyz"
    # print("\\{}".format(bla))
    pass
    # print(type(path))
    # print(path)
    # path.mkdir()
    # print(path)
    # print(path.realpath(__file__))
    # print(pathlib.Path(__file__))


test()
