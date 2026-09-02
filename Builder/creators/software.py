from shell import run


class AurBuilder:
    @staticmethod
    def build():
        run("git -C /tmp clone https://aur.archlinux.org/yay.git", "Клонирование yay")
        run("cd /tmp/yay && makepkg -si", "Сборка и установка yay")


class FirefoxCustomize:
    @staticmethod
    def build():
        run("timeout 10 firefox --headless", "Первый запуск Firefox (создание профиля)")
        run("sh firefox/install.sh", "Установка стилей Firefox")
