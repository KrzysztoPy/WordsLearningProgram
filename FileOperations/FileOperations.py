import os
import LOGIC.MainMenuLogic

# from LOGIC.CreateWordsListLogic import CreateWordsListLogic as Message

ERROR = 'Error'
INFORMATION = 'Information'
SAVE = 'Save'


def get_your_actual_path():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_path_to_folder_with_words_lists():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + LOGIC.MainMenuLogic.DIR_NAME


def open_folder_with_words_lists():
    path = get_path_to_folder_with_words_lists()
    os.startfile(path)


def remove_file(file_name):
    tmp_path = get_path_to_folder_with_words_lists + file_name
    os.remove(tmp_path)


def which_file_exsist(file_name_txt):
    file_name_txt = "\\" + file_name_txt + ".txt"
    file_path = get_path_to_folder_with_words_lists() + file_name_txt
    return os.path.exists(file_path)


def create_new_empty_list(file_name_txt):
    file_name_txt = "\\" + file_name_txt + ".txt"
    tmp_path = get_path_to_folder_with_words_lists() + file_name_txt

    try:
        open(tmp_path, "a").close()
        return [SAVE, "The file has been created", True]
    except IOError as message_exception:
        return [ERROR, str(message_exception), False]


def return_lists_file_in_path(path):
    return os.listdir(path)


def open_file_and_get_content(path):
    return open(path, "r", encoding="utf=8")
