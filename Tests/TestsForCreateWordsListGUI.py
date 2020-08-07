from LOGIC.CreateWordsListLogic import *


def test_whether_repeat_empty_field_and_no_selected_list():
    create_words_list_logic = CreateWordsListLogic()
    create_words_list_logic.all_words_in_select_list = []
    # create_words_list_logic.all_words_in_select_list = [0, ["wahać się,zawahać się"], ["hesitate"]]

    # create_words_list_logic.set_name_actual_select_file = None
    list_set_name_actual_select_file = [[1, "aż do,do,aż", "Until"]]
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
    :set_name_actual_select_file: None - 
    result: "Error", 'You must choice any file!'
    """
    # create_words_list_logic.set_name_actual_select_file("")
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                     polish_english_word[1])
    assert result == [create_words_list_logic.ERROR, 'You must choice any file!']

    # Test 2:
    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    print(create_words_list_logic.set_name_actual_select_file)
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[0],
                                                                                     polish_english_word[1])
    assert result == [create_words_list_logic.ERROR, "Musisz wpisać polską wersje słowa."]

    # Test 3

    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[2],
                                                                                     polish_english_word[3])
    assert result == [create_words_list_logic.ERROR, "You must writing english word version."]

    # Test 4
    create_words_list_logic.set_name_actual_select_file(list_set_name_actual_select_file[0])
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[4],
                                                                                     polish_english_word[5])
    size_get_name_actual_select_file = create_words_list_logic.get_name_actual_select_file()
    print("The same word exist in list. In table number : {}".format(
                          int(size_get_name_actual_select_file.__len__() / 3 + 1)))
    assert result == [create_words_list_logic.ERROR,
                      "The same word exist in list. In table number : {}".format(
                          int(size_get_name_actual_select_file.__len__() / 3 + 1))]

    # Test 5
    create_words_list_logic.set_name_actual_select_file = list_set_name_actual_select_file[0]
    create_words_list_logic.set_name_actual_select_file = "noNone"
    result = create_words_list_logic.whether_repeat_empty_field_and_no_selected_list(polish_english_word[6],
                                                                                     polish_english_word[7])
    assert result == [create_words_list_logic.INFORMATION, "Adding new word to list"]


def start_test():
    test_whether_repeat_empty_field_and_no_selected_list()


start_test()
