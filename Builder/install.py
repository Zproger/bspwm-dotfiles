import sys

from logger import Logger
from options import UserInterface


def main():
    try:
        UserInterface.start()
    except Exception:
        Logger.exception("Установка прервана непредвиденной ошибкой")
        Logger.summary()
        sys.exit(1)

    Logger.summary()


if __name__ == "__main__":
    main()
