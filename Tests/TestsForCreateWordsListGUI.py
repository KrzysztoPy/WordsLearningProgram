from LOGIC.CreateWordsListLogic import *
from random import randint


def mixing_place_words_in_polish_english_words_list(polish_example_words_list, english_example_words_list):
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


def test_whether_repeat_empty_field_and_no_selected_list():
    create_words_list_logic = CreateWordsListLogic()
    create_words_list_logic.all_words_in_select_list = []
    # create_words_list_logic.all_words_in_select_list = [0, ["wahać się,zawahać się"], ["hesitate"]]

    polish_example_words_list = [["pomniejszy,drobny"], ["aż do,do,aż"], ["wahać się, zawahać się"], ["praca,robotnik"],
                                 ["zdecydowanie"], ["składający się"], ["szept"]]
    english_example_words_list = [["minor"], ["Until"], ["hesitate"], ["labour"], ["resolutely"], ["Made up"],
                                  ["Wisper"]]

    all_words_in_select_list_xz = mixing_place_words_in_polish_english_words_list(polish_example_words_list.copy(),
                                                                                  english_example_words_list.copy())

    # create_words_list_logic.set_name_actual_select_file = None
    list_set_name_actual_select_file = [[1, "aż do,do,aż", "Until"]]
    all_words_in_select_list = [1, ["pomniejszy,drobny"], ["minor"], 2, ["aż do,do,aż"], ["Until"]]
    polish_english_word = ["", "", "aż do,do,aż", "", "aż do,do,aż", "Until", "słowo", "", "słowo", "words"]
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
        :set_name_actual_select_file: None  "Name choosing words list"
        :polish_english_word[0]:      empty "Polish word"
        :polish_english_word[1]:      empty "English word"
    """
    # create_words_list_logic.set_name_actual_select_file("")
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                     polish_english_word[1])
    assert result == [create_words_list_logic.ERROR, 'You must choice any file!']

    # Test 2:
    """
    Testing: Correct behavior when function get empty field with polish word.
        :set_name_actual_select_file: Fill       "Name choosing words list"
        :polish_english_word[0]:      empty      "Polish word"
        :polish_english_word[1]:      negligible "English word"
    
    """
    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    print(create_words_list_logic.get_name_actual_select_file)
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                     polish_english_word[1])
    assert result == [create_words_list_logic.ERROR, "Musisz wpisać polską wersje słowa."]

    # Test 3
    """
    Testing: Correct behavior when function get empty field with english word.
        :set_name_actual_select_file: Fill       "Name choosing words list"
        :polish_english_word[0]:      Negligible "Polish word"
        :polish_english_word[1]:      empty      "English word"

    """

    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[2],
                                                                                     polish_english_word[3])
    assert result == [create_words_list_logic.ERROR, "You must writing english word version."]

    # Test 4
    """
    Testing: Correct behavior entered word exist in actual choose words list.
        :set_name_actual_select_file: Fill   "Name choosing words list"
        :polish_english_word[0]:      Fill   "Polish word"
        :polish_english_word[1]:      Fill   "English word"

    """

    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    create_words_list_logic.all_words_in_select_list.clear()
    create_words_list_logic.set_all_words_in_select_list(
        mixing_place_words_in_polish_english_words_list(polish_example_words_list.copy(),
                                                        english_example_words_list.copy()))
    random_word = randint(0, polish_example_words_list.__len__() - 1)
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(
        polish_example_words_list[random_word],
        english_example_words_list[random_word])

    size_get_name_actual_select_file = create_words_list_logic.get_name_actual_select_file()
    print(result)
    print("x")
    print([create_words_list_logic.ERROR,
           "The same word exist in list. In table number : {}".format(
               int(create_words_list_logic.get_all_words_in_select_list().__len__() / 3))])

    assert result == [create_words_list_logic.ERROR,
                      "The same word exist in list. In table number : {}".format(
                          int(random_word))]

    # Test 5
    create_words_list_logic.set_name_actual_select_file = list_set_name_actual_select_file[0]

    create_words_list_logic.set_name_actual_select_file = "noNone"
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[6],
                                                                                     polish_english_word[7])
    assert result == [create_words_list_logic.INFORMATION, "Adding new word to list"]


def start_test():
    test_whether_repeat_empty_field_and_no_selected_list()


start_test()
