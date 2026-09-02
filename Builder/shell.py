import subprocess

from logger import Logger


def run(command: str, description: str | None = None) -> bool:
    """
    Выполняет shell-команду, показывает её вывод в реальном времени и логирует
    итог (успех/ошибка вместе с кодом выхода и последними строками вывода) в Logger.

    Ошибка не прерывает установку - вызывающий код сам решает, критична ли она
    для дальнейших шагов, но абсолютно каждый вызов остаётся в build_debug.log.
    """
    label = description or command
    Logger.info(f"$ {command}")

    process = subprocess.Popen(
        command, shell=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )

    output_lines = []
    for line in process.stdout:
        print(line, end="")
        output_lines.append(line)
    process.wait()

    if process.returncode == 0:
        Logger.success(label)
        return True

    tail = "".join(output_lines[-10:]).strip()
    Logger.error(f"{label} (код выхода {process.returncode})" + (f": {tail}" if tail else ""))
    return False
