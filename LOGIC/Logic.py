from tkinter import *
import pathlib
from pathlib import Path
from os import *


class Logic:
    polish_english_words = []

    def dir_name_is_empty(self, name=""):

        if name.__len__() <= 0:
            return ["Error", "File name can't be empty"]
        else:
            return self.create_directory(name)

    # Create directory when you save new words list
    def create_directory(self, name):

        file_path = os.path.realpath(__file__)
        for i in file_path[::-1]:
            if i == "\\":
                break
            else:
                file_path = file_path[:-1]
        file_path += name
        print(file_path)

        if os.path.isdir(file_path) == True:
            return ["Error", "Directory about the same name just exist. Choice another name."]
        else:
            try:
                pathlib.Path(os.path.dirname(os.path.realpath(__file__)) + "\\{}".format(name)).mkdir(exist_ok=True)
                return ["Information", "Directory was created"]
            except Exception:
                return ["Error", "Directory was't created"]

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


import os


def test():
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
