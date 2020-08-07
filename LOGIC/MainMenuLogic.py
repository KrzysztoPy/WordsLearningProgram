from pathlib import Path
import os


class MenuLogic():
    dir_name = "Words list"

    def create_words_list_dir(self):
        flag = False
        file_path = os.path.realpath(__file__)
        for i in file_path[::-1]:
            if i == "\\":
                if not flag:
                    flag = True
                else:
                    file_path = file_path[:-1]
                    break
            else:
                file_path = file_path[:-1]
        file_path += self.dir_name
        Path(file_path).mkdir(exist_ok=True)
        if not Path(file_path).exists():
            exit()


    # def destroy_learning_window_variable(self, learning_window):
    #     learning_window.__del__(self)
