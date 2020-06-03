import os


class LearningLogic:
    # Variable with all file list
    file_list = None
    # Directory name where is all file
    dir_name = "Words list"

    def set_main_pop(self, main_root):
        # Default window size
        window_width = 1200
        window_height = 600
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)

    def list_path(self):
        tmp_path = os.path.realpath(__file__)

        for i in tmp_path[::-1]:
            if i == "\\":
                break
            else:
                tmp_path = tmp_path[:-1]

        tmp_path += self.dir_name
        return tmp_path

    def file_list(self):
        self.file_list = os.listdir(self.list_path())

        if self.file_list.__len__() == 0:
            self.file_list.append("Empty")
        return self.file_list
