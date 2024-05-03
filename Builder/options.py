import os
from typing import Union
from creators.builder import SystemConfiguration


class UserInterface:
    @staticmethod
    def start():
        UserInterface.welcome_banner()
        install_params = UserInterface.get_params()
        SystemConfiguration.start(*install_params)

    @staticmethod
    def welcome_banner():
        os.system("sh Builder/assets/startup.sh")        

    @staticmethod
    def is_verify_response(text: str, default: Union[str, None] = None) -> bool:
        if ("y" in text.lower()) or (text.lower() == default):
            return True
        return False


    @staticmethod
    def get_params():
        options = [
            "Install all dotfiles? [Y/n]",
            "Update Arch DataBase? [Y/n]",
            "Install BSPWM Dependencies? [Y/n]",
            "Install Dev Dependencies? [Y/n]",
            "Install Nvidia & Intel Drivers? [Y/n]"
        ]
        
        result = []
        for i, option in enumerate(options, start=1):
            result.append(UserInterface.is_verify_response(input(f"{i}) {option}"), ""))

        return result
