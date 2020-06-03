class LearningLogic:

    def set_main_pop(self, main_root):
        # Default window size
        window_width = 1200
        window_height = 600
        # Set center position
        position_right = int(main_root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(main_root.winfo_screenheight() / 2 - window_height / 2)
        return "{}x{}+{}+{}".format(window_width, window_height, position_right, position_down)
