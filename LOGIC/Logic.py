from tkinter import *
import pathlib
from pathlib import Path
import os


class Logic:
    # Create dir where save your list words
    dir_name = "Words list"
    # Stores a list of files
    list_all_file = []

    # Create directory when you save new words list
    def create_directory(self):

        file_path = os.path.realpath(__file__)
        for i in file_path[::-1]:
            if i == "\\":
                break
            else:
                file_path = file_path[:-1]
        file_path += self.dir_name
        Path(file_path).mkdir(exist_ok=True)
        return ["Information", "Directory was created"]  # Do usunięcia

    def save_new_words_list(self, words=[]):
        if words.__len__() < 1:
            return True
        else:
            return False

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

        tmp_path += self.dir_name
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
        self.list_all_file = os.listdir(self.words_list_path())

        if self.list_all_file.__len__() == 0:
            self.list_all_file.append("Empty")
        return self.list_all_file

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

    def load_butt(self, file_name):
        tmp_path = self.words_list_path() + "\\" + file_name
        list_words = open(tmp_path, "r", encoding="utf=8")
        file_data = list_words.read()
        return self.set_words_from_file(file_data)

    def set_words_from_file(self, file_data):

        words_list = []
        flag = FALSE
        polish_words = ""
        english_words = ""
        # dom,ojczyzna|home
        counter = 1
        for j in file_data:
            if j != "|" and flag == FALSE and j != ";":
                if j == ",":
                    polish_words += j + " "
                else:
                    polish_words += j
            elif j == "|":
                flag = TRUE
            elif j != "|" and flag == True and j != ";":
                if j == ",":
                    english_words += j + " "
                else:
                    english_words += j
            elif j == ";":
                words_list += [counter, polish_words, english_words]
                counter += 1
                flag = FALSE
                polish_words = ""
                english_words = ""
        return words_list.copy()

    def check_polish_entry(self, polish_word):
        pass

    def check_english_entry(self, english_word):
        pass

    def add_word(self, polish_word, english_word, tmp_actual_words):
        if polish_word == "":
            return ["Error", "Musisz wpisać polską wersje słowa."]
        elif english_word == "":
            return ["Error", "You must writing english word version."]
        return self.check_change(polish_word, english_word, tmp_actual_words)

    def check_change(self, polish_word, english_word, tmp_actual_words):

        return self.save_to_table(polish_word, english_word, tmp_actual_words)

    def save_to_table(self, polish_word, english_word, tmp_actual_words):
        tmp_words = []
        index = 0

        if tmp_actual_words.__len__() > 3:
            index = int(tmp_actual_words[tmp_actual_words.__len__() - 3])
            for i in range(0, tmp_actual_words.__len__(), 3):
                tmp_words.append(tmp_actual_words[i])
                tmp_words.append(tmp_actual_words[i + 1])
                tmp_words.append(tmp_actual_words[i + 2])

        tmp_words.append(index + 1)
        tmp_words.append(polish_word)
        tmp_words.append(english_word)
        return ["Save", "The word has been added to the list", tmp_words]

    def remove_word(self):
        pass

    def find_word(self):
        pass


def test():
    logic = Logic()
    # # rano|a.m.;około|about;
    logic.save_to_table("popołudniu", "afternoon", ["1", "rano", "a.m.", "2", "około", "about"])
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
