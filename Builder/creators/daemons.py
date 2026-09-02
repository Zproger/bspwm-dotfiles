import os


class Daemons:
    @staticmethod
    def enable_all_daemons():
        Daemons.__enable_network_daemon()
        Daemons.__enable_bluetooth_daemon()
        Daemons.__enable_tor_daemon()
        Daemons.__enable_mpd_daemon()

    @staticmethod
    def __enable_mpd_daemon():
        # mpd - пользовательский демон, поэтому запускается без sudo,
        # иначе systemctl --user не может подключиться к сессионной шине D-Bus
        os.system("systemctl --user enable mpd")

    @staticmethod
    def __enable_network_daemon():
        os.system("sudo systemctl enable NetworkManager")
    
    @staticmethod
    def __enable_bluetooth_daemon():
        os.system("sudo systemctl enable bluetooth.service")
        os.system("sudo systemctl start bluetooth.service")

    @staticmethod
    def __enable_tor_daemon():
        os.system("sudo systemctl enable tor.service")
        os.system("sudo systemctl start tor.service")
