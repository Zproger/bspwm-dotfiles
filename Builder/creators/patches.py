from shell import run


class PatchSystemBugs:
    @staticmethod
    def enable_all_patches():
        PatchSystemBugs.__fix_xterm_error_in_thunar()
        PatchSystemBugs.__make_fish_the_default()
        PatchSystemBugs.__assign_permissions_to_configs()

    @staticmethod
    def __fix_xterm_error_in_thunar():
        run("sudo ln -sf /usr/bin/alacritty /usr/bin/xterm", "Симлинк xterm -> alacritty")

    @staticmethod
    def __make_fish_the_default():
        run("chsh -s /usr/bin/fish", "Установка fish shell по умолчанию")

    @staticmethod
    def __assign_permissions_to_configs():
        run("sudo chmod -R 700 ~/.config/*", "Права доступа для ~/.config")

