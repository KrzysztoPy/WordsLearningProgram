# from FileOperations.FileOperations import *
import FileOperations.FileOperations as File_Oper
import LOGIC.MainMenuLogic
from tkinter import *
from pathlib import Path
import os


class CreateWordsListLogic:
    NOTHING_SELECTED = "Nothing"
    INITIAL_STATE = "Actual select file: "
    INITIAL_STATE_WORD = "Actual select words: "
    ERROR = 'Error'
    INFORMATION = 'Information'
    SAVE = 'Save'
    EMPTY_FILE = "Empty"
    EMPTY_LIST = []
    WITHOUT_ERROR = "Without error"

    dir_with_converted_words_list = "Words list"
    name_actual_select_file = NOTHING_SELECTED

    actual_state_popup = [WITHOUT_ERROR, "All rights"]

    list_all_converted_words_list = []
    all_words_in_select_list = []
    actual_adding_word = []
    convert_value_from_click_table_event = []
    new_adding_words_to_actual_list = []
    added_new_words = False
    number_in_list_words_will_be_removed = None

    # New -> add_new_converted_words_list
    def clear_converted_words_list_name(self, entry_tkinter):
        entry_tkinter.delete(0, 'end')

    # New -> add_new_converted_words_list
    def check_whether_exists_file_with_the_same_name(self, new_name_a_file):

        if new_name_a_file == "":
            return (["Error", "File name can't be empty.", True])
        elif new_name_a_file == ".txt":
            return (["Error", "Prohibited file name: .txt", True])
        if File_Oper.which_file_exsist(new_name_a_file):
            return (["Error", "A file with this name already exists. Choice different name. ", True])
        else:
            return (["All right", "Don't exsist file with the same name", False])

    # New -> add_new_converted_words_list
    def create_new_empty_list(self, file_name_txt):
        return File_Oper.create_new_empty_list(file_name_txt)

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

    def get_list_name_converted_words_lists(self):
        self.set_list_all_converted_words_list(File_Oper.return_lists_file_in_path(
            File_Oper.get_path_to_folder_with_words_lists()))

        if not self.get_list_all_converted_words_list():
            self.set_list_all_converted_words_list([self.EMPTY_FILE])
        return self.list_all_converted_words_list

    def file_create(self, file_name):
        file_name_txt = "\\" + file_name + ".txt"

        if file_name == "":
            self.set_actual_state_popup(["Error", "File name can't be empty."])
        elif file_name == ".txt":
            self.set_actual_state_popup(["Error", "Prohibited file name: .txt"])
        if File_Oper.which_file_exsist(file_name_txt):
            self.set_actual_state_popup(["Error", "A file with this name already exists. Choice different name. "])
        else:
            return self.create_new_empty_list(file_name_txt)

    def open_file_and_return_converted_words_list(self, file_name):
        retrieved_data_from_list_words = File_Oper.open_file_and_get_content(
            File_Oper.get_path_to_folder_with_words_lists() + "\\" + file_name)

        data_from_file = retrieved_data_from_list_words.read()
        file_data = "".join(data_from_file)

        return self.convert_input_data_for_needs_program(file_data, file_name)

    def butt_remove_file(self, file_name):
        return File_Oper.remove_file(file_name)

    def convert_input_data_for_needs_program(self, file_data, file_name):
        """

        :param file_data: don't convert data from selected file
        :return:
        """
        converted_words_list = []
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
                else:
                    english_words += j
            elif j == ";":
                english_all_translations.append(english_words)
                converted_words_list += [counter, polish_all_translations.copy(), english_all_translations.copy()]
                counter += 1

                flag = FALSE
                polish_words = ""
                polish_all_translations.clear()
                english_words = ""
                english_all_translations.clear()

        self.set_converted_words_from_selected_list(converted_words_list.copy())
        self.set_name_actual_select_file(file_name)
        return self.get_converted_words_from_selected_list()

    def set_actual_selected_file(self):
        return self.INITIAL_STATE

    def set_actual_selected_words(self):
        return self.INITIAL_STATE_WORD

    def return_separated_individual_elem(self, counter):
        return (self.get_converted_words_from_selected_list()[counter],
                ",".join(self.get_converted_words_from_selected_list()[counter + 1]),
                ",".join(self.get_converted_words_from_selected_list()[counter + 2]))

    def set_converted_words_from_selected_list(self, all_words_from_selected_list):
        self.all_words_in_select_list = all_words_from_selected_list.copy()

    def get_converted_words_from_selected_list(self):
        return self.all_words_in_select_list.copy()

    def set_list_with_old_and_new_words(self, set_list_with_old_and_new_words):
        self.set_list_with_old_and_new_words = set_list_with_old_and_new_words

    def get_set_list_with_old_and_new_words(self):
        return self.set_list_with_old_and_new_words

    def check_polish_entry(self, polish_word):
        pass

    def check_english_entry(self, english_word):
        pass

    def set_name_actual_select_file(self, name_actual_select_file):
        self.name_actual_select_file = name_actual_select_file

    def get_name_actual_select_file(self):
        return self.name_actual_select_file

    def check_fields_is_not_empty(self, polish_word, english_word):
        if self.get_name_actual_select_file() == "None":
            return [self.ERROR, "You must choice any file!"]
        elif polish_word == "":
            return [self.ERROR, "Musisz wpisać polską wersje słowa."]
        elif english_word == "":
            return [self.ERROR, "You must writing english word version."]
        else:
            return ["All right"]

    def entry_words_separation(self, polish_words, english_words):
        list_polish_words = []
        list_english_words = []
        polish_word = ""
        english_word = ""

        for count in range(0, polish_words.__len__()):
            if polish_words[count] != ",":
                polish_word += polish_words[count]
                if count == polish_words.__len__() - 1:
                    list_polish_words.append(polish_word)
                    polish_word = ""
            else:
                list_polish_words.append(polish_word)
                polish_word = ""

        for count in range(0, english_words.__len__()):
            if english_words[count] != ",":
                english_word += english_words[count]
                if count == english_words.__len__() - 1:
                    list_english_words.append(english_word)
                    english_word = ""
            else:
                list_english_words.append(english_word)
                english_word = ""

        return list_polish_words, list_english_words

    def check_is_empty_repeat_field(self, polish_words, english_words):
        polish_repeated = 0
        english_repeated = 0
        polish_repeat = False
        english_repeat = False

        check_fields_is_not_empty = self.check_fields_is_not_empty(polish_words, english_words)
        if check_fields_is_not_empty[0] != "Error":
            list_polish_words, list_english_words = self.entry_words_separation(polish_words, english_words)

            if self.all_words_in_select_list:
                for counter in range(0, self.all_words_in_select_list.__len__(), 3):
                    for words in self.all_words_in_select_list[counter + 1]:
                        for chosen_polish_word in list_polish_words:
                            if (chosen_polish_word.strip()).lower() == (words.strip()).lower():
                                polish_repeated += 1
                        if polish_repeated == list_polish_words.__len__():
                            polish_repeat = True
                        else:
                            polish_repeat = False
                    for words in self.all_words_in_select_list[counter + 2]:
                        for chosen_english_word in list_english_words:
                            if (chosen_english_word.strip()).lower() == (words.strip()).lower():
                                english_repeated += 1
                        if english_repeated == list_english_words.__len__():
                            english_repeat = True
                        else:
                            english_repeat = False
                    if polish_repeat and english_repeat:
                        break
                if polish_repeat and english_repeat:
                    return [self.ERROR,
                            "The same word exist in list. In table number : {}".format(int(counter / 3 + 1))]
                elif counter == self.all_words_in_select_list.__len__() - 3:
                    return self.add_new_word_to_list(int(self.all_words_in_select_list.__len__() / 3) + 1,
                                                     [polish_words], [english_words])
        else:
            return check_fields_is_not_empty

    def add_new_word_to_list(self, counter, polish_word, english_word):
        new_adding_words_to_actual_list = self.get_converted_words_from_selected_list()
        new_adding_words_to_actual_list.append(counter)
        new_adding_words_to_actual_list.append(polish_word)
        new_adding_words_to_actual_list.append(english_word)
        self.set_converted_words_from_selected_list(new_adding_words_to_actual_list)
        self.set_added_new_words(True)
        return [self.INFORMATION, "Adding new word to list"]

    def check_change(self, polish_word, english_word):
        return self.save_to_table(polish_word, english_word)

    def convert_value_from_table_to_remove(self, removing_words={}):
        convert_value_from_table = []
        for num, value in enumerate(removing_words.get("values")):
            if num != 0:
                tmp_value = value.__str__()
                tmp_new_list_particular_word = ""
                new_list_with_convert_words = []
                for counter, sign in enumerate(tmp_value):
                    if sign != ',':
                        tmp_new_list_particular_word += sign
                        if counter == (tmp_value.__len__() - 1):
                            new_list_with_convert_words.append(tmp_new_list_particular_word)
                            tmp_new_list_particular_word = ""
                    elif sign == ",":
                        new_list_with_convert_words.append(tmp_new_list_particular_word)
                        tmp_new_list_particular_word = ""

                convert_value_from_table.append(new_list_with_convert_words.copy())
            else:
                convert_value_from_table.append(value)
        if not convert_value_from_table:
            convert_value_from_table = self.set_actual_selected_words() + self.NOTHING_SELECTED
        self.set_convert_value_from_click_table_event(convert_value_from_table)

    def new_convert_value_from_table_to_remove(self, removing_words):
        pass

    def remove_word_from_lists(self):
        if not self.convert_value_from_click_table_event:
            return [self.ERROR, "You didn't choose element which you want remove. Please try again."]

        copy_all_words_in_select_list = (self.get_converted_words_from_selected_list()).copy()
        for i in self.all_words_in_select_list:
            for j in self.convert_value_from_click_table_event:

                if i == j:
                    copy_all_words_in_select_list.remove(j)
                    break

        self.set_converted_words_from_selected_list(copy_all_words_in_select_list.copy())
        return self.changing_id_number()

    def changing_id_number(self):

        tmp_all_words_in_select_list = self.get_converted_words_from_selected_list().copy()
        for counter in range(0, tmp_all_words_in_select_list.__len__(), 3):
            if counter == 0:
                tmp_all_words_in_select_list[counter] = counter + 1
            else:
                tmp_all_words_in_select_list[counter] = int((counter / 3) + 1)

        self.set_converted_words_from_selected_list(tmp_all_words_in_select_list.copy())
        self.convert_value_from_click_table_event.clear()
        return [self.INFORMATION, "Remove word from table!!!"]

    def save_words_to_file(self, file_name):

        if self.get_name_actual_select_file() != self.NOTHING_SELECTED:
            convered_data = self.convert_data()
            return File_Oper.save_data_to_file(file_name, convered_data)
        else:
            return [self.ERROR, "You can't save empty list."]

    def convert_data(self):
        all_words = self.get_all_words_in_select_list()
        converted_words = ""
        converted_words_list = []

        for counter in range(0, self.get_all_words_in_select_list().__len__(), 3):
            converted_words += self.get_all_words_in_select_list[counter + 1] + "|"
            print(converted_words)
            converted_words += self.get_all_words_in_select_list[counter + 2] + ";\n"
            print(converted_words)
            converted_words_list.append(converted_words)
            converted_words = ""
        return converted_words_list

    def whether_remove_lists_is_selected(self, table_with_headers, actual_selected_list):
        if self.get_name_actual_select_file() == actual_selected_list:
            return table_with_headers.delete.delete(*table_with_headers.get_children())

    def remove_list_which_is_load(self, actual_selected_list):
        return self.get_name_actual_select_file().__str__() == actual_selected_list

    def remove_data_from_table(self, table_with_headers):
        return table_with_headers.delete.delete(*table_with_headers.get_children())

    def set_actual_state_popup(self, actual_state_popup):
        self.actual_state_popup = actual_state_popup

    def get_actual_state_popup(self):
        return self.actual_state_popup

    def get_message_cons_error(self):
        return self.ERROR

    def get_message_cons_save(self):
        return self.SAVE

    def set_all_words_in_select_list(self, all_words_in_select_list):
        self.all_words_in_select_list = all_words_in_select_list

    def get_all_words_in_select_list(self):
        return self.all_words_in_select_list

    def which_selected_some_list(self, list_with_words_lists_name):
        return list_with_words_lists_name.__str__() != self.EMPTY_FILE

    def which_list_with_words_list_is_not_empty(self, selected_file_to_remove):
        return selected_file_to_remove != self.NOTHING_SELECTED

    def set_list_all_converted_words_list(self, list_all_converted_words_list):
        self.list_all_converted_words_list = list_all_converted_words_list

    def get_list_all_converted_words_list(self) -> []:
        return self.list_all_converted_words_list

    def get_new_adding_words_to_actual_list(self):
        return self.new_adding_words_to_actual_list

    def set_new_adding_words_to_actual_list(self, new_adding_words_to_actual_list):
        self.new_adding_words_to_actual_list = new_adding_words_to_actual_list

    def get_added_new_words(self):
        return self.added_new_words

    def set_added_new_words(self, added_new_words):
        self.added_new_words = added_new_words

    def get_convert_value_from_click_table_event(self):
        return self.convert_value_from_click_table_event

    def set_convert_value_from_click_table_event(self, convert_value_from_click_table_event):
        self.convert_value_from_click_table_event = convert_value_from_click_table_event

    def get_convert_by_view_value_from_click_table_event(self, actual_clicked_elem):
        return f'Nr: {actual_clicked_elem.get("values")[0]:2d}\n PL: {actual_clicked_elem.get("values")[1]:10s}\n ' \
               f'EN: {actual_clicked_elem.get("values")[2]:10s}\n'

    def decrementation_id(self):
        for counter in range(self.get_number_in_list_words_will_be_removed() * 3,
                             self.get_all_words_in_select_list().__len__(), 3):
            self.get_all_words_in_select_list()[counter] -= 1

    def remove_words_from_list(self):
        remove_word_from_list = self.get_all_words_in_select_list()
        if self.get_number_in_list_words_will_be_removed != 0:
            for i in range(0, 3):
                del remove_word_from_list[self.get_number_in_list_words_will_be_removed() * 3]
            self.set_all_words_in_select_list(remove_word_from_list)

    def set_number_word_future_to_removed(self, number_in_table):
        self.set_number_in_list_words_will_be_removed(number_in_table - 1)

    def save_to_table(self, polish_word, english_word):
        return ["Save", "The word has been added to the list", self.all_words_in_select_list.copy()]

    def get_number_in_list_words_will_be_removed(self):
        return self.number_in_list_words_will_be_removed

    def set_number_in_list_words_will_be_removed(self, number_in_list_words_will_be_removed):
        self.number_in_list_words_will_be_removed = number_in_list_words_will_be_removed

    def close_words_window(self, top_window, main_window):
        top_window.destroy()
        main_window.deiconify()
