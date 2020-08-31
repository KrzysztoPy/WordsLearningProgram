from pathlib import Path
from FileOperations.FileOperations import get_your_actual_path

DIR_NAME = "\Words list"


class MenuLogic:

    def create_words_list_dir(self):
        file_path = get_your_actual_path()
        file_path += DIR_NAME
        print(file_path)
        Path(file_path).mkdir(exist_ok=True)
        # if not Path(file_path).exists():
        #     exit()
