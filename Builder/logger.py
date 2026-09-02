import logging
import sys


class Logger:
    """Централизованный логгер сборки: пишет одновременно в консоль и в build_debug.log."""

    filename = "build_debug.log"
    success_count = 0
    error_count = 0
    _logger: logging.Logger | None = None

    @classmethod
    def _get(cls) -> logging.Logger:
        if cls._logger is not None:
            return cls._logger

        logger = logging.getLogger("bspwm_builder")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        file_handler = logging.FileHandler(cls.filename, mode="a", encoding="UTF-8")
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        cls._logger = logger
        return logger

    @classmethod
    def info(cls, text: str) -> None:
        cls._get().info(text)

    @classmethod
    def success(cls, text: str) -> None:
        cls.success_count += 1
        cls._get().info(f"[OK] {text}")

    @classmethod
    def warning(cls, text: str) -> None:
        cls._get().warning(text)

    @classmethod
    def error(cls, text: str) -> None:
        cls.error_count += 1
        cls._get().error(text)

    @classmethod
    def exception(cls, text: str) -> None:
        """Записывает ошибку вместе с traceback текущего исключения."""
        cls.error_count += 1
        cls._get().exception(text)

    @classmethod
    def summary(cls) -> None:
        cls._get().info(
            f"Итог: успешно {cls.success_count}, с ошибками {cls.error_count}. "
            f"Подробности в {cls.filename}"
        )
