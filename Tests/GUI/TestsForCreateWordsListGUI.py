from LOGIC.CreateWordsListLogic import *
from random import randint


class TestsForCreateWordsListGui:
    create_words_list_logic = CreateWordsListLogic()

    polish_example_words_list = [["pomniejszy,drobny"], ["aż do,do,aż"], ["wahać się, zawahać się"],
                                 ["praca,robotnik"],
                                 ["zdecydowanie"], ["składający się"], ["szept"]]
    english_example_words_list = [["minor"], ["Until"], ["hesitate"], ["labour"], ["resolutely"], ["Made up"],
                                  ["Wisper"]]

    polish_example_add_word = ["skrót", "ostatni,trwać", "taki", "rola", "czasownik", "rzeczownik"]
    english_example_add_word = ["abbreviation", "last", "such", "roll", "verb", "noun"]

    def mixing_place_words_in_polish_english_words_list(self, polish_example_words_list, english_example_words_list):
        new_words_list = []
        counter_num = 1

        for counter in range(polish_example_words_list.__len__(), 0, -1):
            rand_num = randint(0, polish_example_words_list.__len__() - 1)
            new_words_list.append(counter_num)
            new_words_list.append(polish_example_words_list[rand_num])
            new_words_list.append(english_example_words_list[rand_num])
            polish_example_words_list.remove(polish_example_words_list[rand_num])
            english_example_words_list.remove(english_example_words_list[rand_num])
            counter_num += 1
        return new_words_list

        # Test entry_words_separation()

    def test_entry_words_separation(self):
        create_words_list_logic = CreateWordsListLogic()
        polish_words_list = ['wahać', 'zawahać się']
        english_words_list = ['hesitate']

        polish_words = polish_words_list[0] + "," + polish_words_list[1]
        english_words = english_words_list[0]

        result = create_words_list_logic.entry_words_separation(polish_words, english_words)
        assert result == ([polish_words_list[0], polish_words_list[1]], [english_words_list[0]])

    def test_whether_repeat_empty_field_and_no_selected_list(self):
        self.create_words_list_logic.all_words_in_select_list = []
        # create_words_list_logic.all_words_in_select_list = [0, ["wahać się,zawahać się"], ["hesitate"]]

        all_words_in_select_list_xz = self.mixing_place_words_in_polish_english_words_list(
            self.polish_example_words_list.copy(),
            self.english_example_words_list.copy())

        # create_words_list_logic.set_name_actual_select_file = None
        list_set_name_actual_select_file = [[1, "aż do,do,aż", "Until"]]
        all_words_in_select_list = [1, ["pomniejszy,drobny"], ["minor"], 2, ["aż do,do,aż"], ["Until"]]
        polish_english_word = ["", "", "aż do,do,aż", "", "aż do,do,aż", "Until", "słowo", "words"]
        # Test 1:
        """
        :whether_repeat_empty_field_and_no_selected_list: None - List with words not choose 
        :polish_word_empty: "" - getting polish words 
        :english_word_empty: "" - getting english words
        :all_words_in_select_list: empty - list with another list which included list with 3 elem [Num in list, 
        "polish_word_version", "english_word_version]
        """

        # Test 1:
        """
        Testing: Correct behavior when set_name_actual_select_file is None.
            :set_name_actual_select_file: List "Name choosing words list"
            :polish_english_word[0]:      List "Polish word"
            :polish_english_word[1]:      List "English word"
        """
        # create_words_list_logic.set_name_actual_select_file("")
        result = self.create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                              polish_english_word[1])
        assert result == [self.create_words_list_logic.ERROR, 'You must choice any file!']

        # Test 2:
        """
        Testing: Correct behavior when function get empty field with polish word.
            :set_name_actual_select_file: List      "Name choosing words list"
            :polish_english_word[0]:      List      "Polish word"              :empty
            :polish_english_word[1]:      List      "English word"             :negligible (doesn't need to be fill)
        
        """
        self.create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
        # print(create_words_list_logic.get_name_actual_select_file())
        result = self.create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                              polish_english_word[1])
        assert result == [self.create_words_list_logic.ERROR, "Musisz wpisać polską wersje słowa."]

        # Test 3
        """
        Testing: Correct behavior when function get empty field with english word.
            :set_name_actual_select_file: List "Name choosing words list" 
            :polish_english_word[0]:      List "Polish word"              :Negligible (Must be fill)
            :polish_english_word[1]:      List "English word"             :empty
    
        """

        self.create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
        result = self.create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[2],
                                                                                              polish_english_word[3])
        assert result == [self.create_words_list_logic.ERROR, "You must writing english word version."]

        # Test 4
        """
        Testing: Correct behavior entered word exist in actual choose words list.
            :set_name_actual_select_file: List   "Name choosing words list"
            :polish_english_word[0]:      List   "Polish word"
            :polish_english_word[1]:      List   "English word"
    
        """

        self.create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
        self.create_words_list_logic.all_words_in_select_list.clear()
        random_word = randint(0, self.polish_example_words_list.__len__() - 1)
        self.create_words_list_logic.set_converted_words_from_selected_list(
            self.mixing_place_words_in_polish_english_words_list(self.polish_example_words_list.copy(),
                                                                 self.english_example_words_list.copy()))

        result = self.create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(
            self.polish_example_words_list[random_word],
            self.english_example_words_list[random_word])

        size_get_name_actual_select_file = self.create_words_list_logic.get_name_actual_select_file()

        # print([create_words_list_logic.ERROR,
        #        "The same word exist in list. In table number : {}".format(
        #            int(result[1][-1]))])

        assert result == [self.create_words_list_logic.ERROR,
                          "The same word exist in list. In table number : {}".format(
                              int(result[1][-1]))]

        # Test 5

        """
        Testing: Validates the message after adding a new word.
            :set_name_actual_select_file: List   "Name choosing words list"
            :polish_english_word[0]:      List   "Polish word"
            :polish_english_word[1]:      List   "English word"

        """

        self.create_words_list_logic.set_name_actual_select_file = list_set_name_actual_select_file[0]
        self.create_words_list_logic.set_name_actual_select_file = "noNone"
        result = self.create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[6],
                                                                                              polish_english_word[7])

        assert result == [self.create_words_list_logic.INFORMATION, "Adding new word to list"]

    def test_adding_word_for_list(self):
        """
        Testing: Validates the addition new words and correctness writing the list.
            :rand_word:                     Int   Random choose word from the examples  (0-5)
            :counter                        Int                                         (9)
            :list_before_adding_words:      List   Include list with words before saving
        """

        rand_word = randint(0, self.polish_example_add_word.__len__() - 1)
        self.create_words_list_logic.set_converted_words_from_selected_list([])
        counter = int(self.create_words_list_logic.get_converted_words_from_selected_list().__len__() / 3 + 1)
        list_before_adding_words = self.create_words_list_logic.get_converted_words_from_selected_list()
        list_before_adding_words.append(counter)
        list_before_adding_words.append([self.polish_example_add_word[rand_word]])
        list_before_adding_words.append([self.english_example_add_word[rand_word]])

        result1 = self.create_words_list_logic.adding_word_for_list(counter,
                                                                    [self.polish_example_add_word[rand_word]],
                                                                    [self.english_example_add_word[rand_word]])
        result1_1 = self.create_words_list_logic.get_converted_words_from_selected_list()

        assert result1 == [self.create_words_list_logic.INFORMATION, "Adding new word to list"]
        assert result1_1 == list_before_adding_words


def start_test():
    tests_for_create_words_list_gui = TestsForCreateWordsListGui()
    tests_for_create_words_list_gui.test_whether_repeat_empty_field_and_no_selected_list()
    tests_for_create_words_list_gui.test_entry_words_separation()
    tests_for_create_words_list_gui.test_adding_word_for_list()


start_test()
