import packages

from logger import Logger
from shell import run
from creators.software import AurBuilder, FirefoxCustomize
from creators.patches import PatchSystemBugs
from creators.daemons import Daemons


class SystemConfiguration:
    @staticmethod
    def start(*args):
        Logger.info(f"Запуск сборки. Опции: {args}")

        if args[0]:
            SystemConfiguration.__start_option_1()
        if args[1]:
            SystemConfiguration.__start_option_2()
        if args[2]:
            SystemConfiguration.__start_option_3()
        if args[3]:
            SystemConfiguration.__start_option_4()

        Daemons.enable_all_daemons()
        PatchSystemBugs.enable_all_patches()

    @staticmethod
    def __start_option_1():
        SystemConfiguration.__create_default_folders()
        SystemConfiguration.__copy_bspwm_dotfiles()

    @staticmethod
    def __start_option_2():
        run("sudo pacman -Syu", "Обновление базы пакетов Arch")

    @staticmethod
    def __start_option_3():
        Logger.info("Установка зависимостей BSPWM")
        AurBuilder.build()
        SystemConfiguration.__install_pacman_packages(packages.BASE_PACKAGES)
        SystemConfiguration.__install_aur_packages(packages.AUR_PACKAGES)
        FirefoxCustomize.build()

    @staticmethod
    def __start_option_4():
        Logger.info("Установка dev-зависимостей")
        SystemConfiguration.__install_pacman_packages(packages.DEV_PACKAGES)

    @staticmethod
    def __install_pacman_packages(package_names: list):
        for package in package_names:
            run(f"sudo pacman -S --noconfirm {package}", f"Пакет (pacman): {package}")

    @staticmethod
    def __install_aur_packages(package_names: list):
        for package in package_names:
            run(f"yay -S --noconfirm {package}", f"Пакет (AUR): {package}")

    @staticmethod
    def __create_default_folders():
        Logger.info("Создание директорий по умолчанию")
        default_folders = "~/Videos ~/Documents ~/Downloads " + \
                          "~/Music ~/Desktop"
        run("mkdir -p ~/.config", "Создание ~/.config")
        run(f"mkdir -p {default_folders}", "Создание пользовательских директорий")
        run("cp -r Images/ ~/", "Копирование Images/")

    @staticmethod
    def __copy_bspwm_dotfiles():
        Logger.info("Копирование dotfiles и GTK-тем")
        run("cp -r config/* ~/.config/", "Копирование config/")
        run("cp Xresources ~/.Xresources", "Копирование Xresources")
        run("cp gtkrc-2.0 ~/.gtkrc-2.0", "Копирование gtkrc-2.0")
        run("cp -r local ~/.local", "Копирование local/")
        run("cp -r themes ~/.themes", "Копирование themes/")
        run("cp xinitrc ~/.xinitrc", "Копирование xinitrc")
        run("cp -r bin/ ~/", "Копирование bin/")
