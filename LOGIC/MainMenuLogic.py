from pathlib import Path
import os


class MenuLogic():
    dir_name = "../Words list"

    def create_words_list_dir(self):
        file_path = os.path.realpath(__file__)
        for i in file_path[::-1]:
            if i == "\\":
                break
            else:
                file_path = file_path[:-1]
        file_path += self.dir_name
        Path(file_path).mkdir(exist_ok=True)

    pass
