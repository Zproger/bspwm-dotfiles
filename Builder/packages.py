
BASE_PACKAGES = [
    "ffmpegthumbnailer", "tumbler",  # Создает миниатюры в thunar
    "lsd",  # Расширенная версия ls
    "alacritty",  # Эмулятор терминала
    "bat",  # Улучшенная версия cat
    "evince",  # Читалка PDF
    "xdotool",  # Dependency for ~/bin/cursor_tracker.sh
    "mesa", "lib32-mesa", "xf86-video-nouveau", "xf86-video-intel", "vulkan-intel",  # Necessary drivers
    "nvtop", # Позволяет посмотреть нагрузку на GPU в режиме терминала
    "npm",  # Зависимость для других компонентов
    "brightnessctl",  # Используется для управления яркостью (bin/brightness)
    "kitty",  # Зависимость nvim для images.lua
    "gvfs", "gvfs-mtp",  # Поддержка MTP протокола, монтирование Android через USB
    "automake", "make", "cmake", "autoconf",  # Автоматическое создание Makefile
    "bluez", "bluez-utils",  # Пакеты для модуля блютуз
    "dunst",  # Демон уведомлений
    "fakeroot",  # Создает фейковое окружение
    "feh",  # Просмотр и работа с изображениями
    "firefox",  # Основной Браузер
    "fish",  # Shell для работы с терминалом
    "thunar-archive-plugin",  # Поддержка архивов в thunar
    "gzip", "p7zip", "unrar", "zip", "unzip", "xarchiver",  # Работа с архивами
    "gedit",  # Редактор текста
    "htop", "btop",  # Системные мониторы
    "thunar",  # Файловый менеджер
    "zathura", "zathura-djvu", "zathura-pdf-mupdf",  # Просмотр PDF, DJVU, EPUB файлов
    "picom",  # Композитор для отрисовки анимаций
    "nitrogen",  # Выбор обоев из графического интерфейса
    "pavucontrol",  # Управление звуком с графического интерфейса
    "redshift",  # Задает теплый цвет монитора в зависимости от времени
    "scrot",  # Консольный софт для скринов
    "fastfetch",  # Вывод информации о системе и железе
    "rofi", "rofi-calc", "rofi-emoji",  # Меню приложений + доп.плагины
    "mat2",  # Очистка метаданных изображения
    "ranger",  # Консольный файловый менеджер
    "calcurse",  # Консольный календарь
    "ttf-jetbrains-mono", "ttf-jetbrains-mono-nerd",  # Базовые шрифты
    "ttf-fira-code", "ttf-iosevka-nerd",  # Базовые шрифты
    "libreoffice",  # Приложения офиса
    "tree",  # Отобразить дерево
    "sudo",  # Выполнение команд с правами root
    "ffmpeg",  # Утилита для работы с медиа
    "polybar",  # Верхняя панель с рабочими столами и управлением системой
    "torbrowser-launcher",  # Лаунчер тора и служба для работы в фоне
    "dpkg",  # Средство для сборки Debian пакетов
    "gcc", "clang",  # Компилятор языка С и пакет для поддержки языка
    "git",  # Система контроля версий
    "gpick",  # Определить цвета. Необходимо для встроенного софта из bin/
    "wget",  # Получить файлы с использованием HTTP/S, FTP
    "pamixer",  # Микшер командной строки Pulseaudio
    "pulseaudio-alsa",  # Управление ALSA
    "ueberzug",  # Используется для отображения превью изображений и прочего медиа-контента
    "xclip",  # Работа с буфером обмена используя терминал
    # "breeze", # TODO: Deprecated
    "openvpn",  # Поддержка протокола OpenVPN
    "reflector",  # Получить последний список зеркал
    # "uthash",  # TODO: Deprecated
    "slop",  # Получить координаты клика мыши
    "nano",  # Консольный редактор текста
    "lxappearance",  # Управления темами, иконками
    "papirus-icon-theme",  # Пак иконок для окружения
    "imagemagick",  # Набор консольных утилит для редактирования изображений / TODO: Зависимость от nvim
    "ncmpcpp", "mpd",  # Клиент для работы с медиа
    "mpc",  # Минималистичный интерфейс командной строки для MPD
    "mpv",  # Просмотр видео
    "alsa-plugins", "alsa-utils",  # Плагины и утилиты для Alsa
    # "alsa-tools",  # TODO: Deprecated
    "network-manager-applet", "networkmanager-openvpn",
    "gparted",  # Работа с носителями в системе
    "intel-ucode",  # Микрокод для процессоров intel
    "gnu-netcat",  # Утилиты для работы с сетью
    "usbutils",  # Утилиты для работы с USB-устройствами
    # "python-pyalsa",  # TODO: Deprecated
    "sshfs",  # Монтирование удаленных SSH каталогов локально
    "netctl",  # Сетевой менеджер на основе CLI
    "openssh",  # Набор программ для поддержки SSH
    "shellcheck",  # Инструмент для анализа сценариев оболочки
    "noto-fonts-emoji",  # Для отображения emoji в rofi-menu
    "noto-fonts-cjk",  # Для отображения emoji в rofi-menu
    "gthumb",  # Просмотр и редактирование изображений
    "gnome-disk-utility",  # Просмотр и редактирование дисков
]

DEV_PACKAGES = [
    "screenkey",  # Вывод нажатий клавиатуры на экран
    "timeshift",  # Софт для бэкапов
    "pinta",  # Софт для рисования
    "kdenlive",  # Монтаж видео
    "lazygit",  # Удобный интерфейс для управления git
    "wireshark-qt",  # Перехват и анализ сетевых пакетов
    "filezilla",  # Работа с FTP из графической среды
    "chromium",  # Дополнительный браузер
    "xfce4-settings",  # Зависимость для thunar и thunar actions
    "keepassxc",  # Защищенный менеджер паролей
    "audacity",  # Работа со звуком
    "gufw",  # TODO: Deprecated
    # "python-pywal",  # TODO: Deprecated
    "bleachbit",  # Софт для шрединга файлов и безопасной очистки системы
    "veracrypt",  # Создание криптоконтейнеров
    "homebank",  # Отслеживание финансов
    # "touche",  # TODO: Deprecated
    # "dconf-editor",  TODO: Deprecated
    "neovim",  # Консольный редактор кода
    "obs-studio",  # Запись видео и управление трансляциями
    "telegram-desktop",  # Мессенджер
    "tmux",  # TODO: Deprecated
    "yt-dlp",  # Утилита для работы с youtube
    "code",  # Редактор кода
    "cowsay",  # Вывод текста с ASCII артами
    "deluge-gtk",  # Торрент клиент
    "flameshot",  # Программа для скриншотов
    "sqlitebrowser",  # Работа с SQLite базами
    "obsidian",  # Работа с заметками
    "python-pip",  # Система управления пакетами Python
    "bpython",  # Выполнение Python кода построчно
    "ipython",  # Интерактивный режим Python
    "cloc",  # Посчитать количество строк кода
    "hexyl",  # Hex дампер
]

AUR_PACKAGES = [
    "lazydocker",  # Удобный интерфейс для управления docker
    "cava",  # Вывод спектра для музыки
    "i3lock-color",  # Используется для блокировки экрана
    "ptpython",  # Выполнение Python кода построчно
    "ttf-symbola",  # Для отображения emoji в rofi-menu
    "hyx",  # Редактирование и просмотр Hex внутри файла
    "arttime-git",  # Консольный таймер и секундомер
    "bluetuith",  # TUI менеджер управления bluetooth
    "rofi-bluetooth-git",  # Управление bluetooth в rofi
    "anki",  # Программа для запоминания материала через карточки
    "light",  # TODO: Нужен для управления яркостью amd (bin/brightness)
]

