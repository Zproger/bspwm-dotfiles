Данный файл содержит последовательность команд, которая нужна для полной установки системы Arch Linux.
Он также включает в себя использование билдера из репозитория, который автоматически разворачивает BSPWM окружение.

### Подключаемся к WiFi (необязательно)
```bash
iwctl
device list
station устройство scan
station устройство get-networks
station устройство connect SSID
ping google.com
```

### Установка крупного шрифта (необязательно)
```bash
pacman -S terminus-font
cd /usr/share/kbd/consolefonts
setfont ter-u32b.psf.gz
```

### Разметка диска под UEFI GPT с шифрованием
Если вы используете SSD, тогда ваши разделы будут выглядеть примерно так:
- `/dev/nvme0n1p1`
- `/dev/nvme0n1p2`

В таком случае замените `/dev/sda` на `/dev/nvme0n1`.
А разделы `/dev/sda1` и `/dev/sda2` на `/dev/nvme0n1p1` и `/dev/nvme0n1p2`.

```bash
parted /dev/sda
mklabel gpt
mkpart ESP fat32 1Mib 512Mib
set 1 boot on

mkpart primary
# file system (нажимаем ENTER)
# start: 513Mib
# end: 100%

quit
```

### Шифруем раздел который подготавливался ранее
```bash
cryptsetup luksFormat /dev/sda2
# sda2 – раздел с шифрованием
# вводим YES большими буквами
# вводим пароль 2 раза

# Открываем зашифрованный раздел
cryptsetup open /dev/sda2 luks

# Проверяем разделы
ls /dev/mapper/*

# Создаем логические разделы внутри зашифрованного раздела
pvcreate /dev/mapper/luks
vgcreate main /dev/mapper/luks

# 100% зашифрованного раздела помещаем в логический раздел root
lvcreate -l 100%FREE main -n root

# Посмотреть все логические разделы
lvs
```

### Подготовка разделов и монтирование
```bash
# Форматируем раздел под ext4
mkfs.ext4 /dev/mapper/main-root

# Форматируем boot раздел под Fat32, на физ.разделе /dev/sda1 лежит boot
mkfs.fat -F 32 /dev/sda1

# Монтируем разделы для установки системы
mount /dev/mapper/main-root /mnt
mkdir /mnt/boot

# Монтируем раздел с boot в текущую рабочую папку
mount /dev/sda1 /mnt/boot
```

### Сборка ядра и базовых софтов
```bash
# Устанавливаем базовые софты
pacstrap -K /mnt base linux linux-firmware base-devel lvm2
dhcpcd net-tools iproute2 networkmanager vim micro efibootmgr iwd

# Генерируем fstab
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab

# Настройка системы
arch-chroot /mnt

# Нужно раскомментировать ru_RU и en_US в этом файле
micro /etc/locale.gen

# Генерируем локали
locale-gen

# Настраиваем время
ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime
hwclock --systohc

# Указать имя хоста
echo “arch” > /etc/hostname

# Укажите пароль для root пользователя
passwd

# Добавляем нового пользователя и настраиваем права
useradd -m -G wheel,users -s /bin/bash user
passwd user
systemctl enable dhcpcd
systemctl enable iwd.service

micro /etc/mkinitcpio.conf
# Пересборка ядра. Найдите строку HOOKS=(base udev autodetect modconf kms
# keyboard keymap consolefont block filesystems fsck)

# и замените на:

# HOOKS=(base udev autodetect modconf kms keyboard keymap consolefont block filesystems encrypt lvm2 fsck)

# Запустить процесс пересборки ядра
mkinitcpio -p linux
```

### Установка загрузчика
```bash
bootctl install --path=/boot
cd /boot/loader
micro loader.conf

# Вставляем в loader.conf следующий конфиг:
timeout 3
default arch

# Создаем конфигурацию для запуска
cd /boot/loader/entries
micro arch.conf

# Вставляем в arch.conf следующее:
# UUID можно узнать командой blkid
title Arch Linux by ZProger
linux /vmlinuz-linux
initrd /initramfs-linux.img
options rw cryptdevice=UUID=uuid_от_/dev/sda2:main root=/dev/mapper/main-root

# Выдаем права на sudo
sudo EDITOR=micro visudo
# После открытия раскомментируйте %wheel ALL=(ALL:ALL) ALL

# Выходим из системы и перезагружаемся
Ctrl+D
umount -R /mnt
reboot
```

### Устанавливаем оболочку
Если при загрузке системы вы получаете ошибки или у вас открывается окно от iso образа Arch'a, тогда необходимо отмонтировать образ или вытащить флешку.
Также убедитесь что загрузка идет под EFI, особенно это касается виртуальных машин.

Перед выполнением этих команд, авторизуйтесь в пользователя user. На этапе загрузки система попросит ввести пароль для дешифровки области жесткого диска,
и в дальнейшем вам будет предложено войти в пользователя, введя логин и пароль. После авторизации выполняем следующее:

```bash
sudo pacman -Sy
sudo pacman -S xorg bspwm sxhkd xorg-xinit xterm git python3

# Настройка xinitrc
micro /etc/X11/xinit/xinitrc

# Отключите любые другие строки exec и добавьте в конец файла строку:
exec bspwm
```

Загрузите репозиторий локально, но перед выполнением билдера я рекомендую перейти в `Builder/packages.py` и посмотреть пакеты, которые будут установлены.
Я не советую редактировать `BASE_PACKAGES`, так как они необходимы для правильной работы оболочки, однако вы свободно можете редактировать другие виды пакетов.
На этапе билдера вам будет предложено установить `DEV_PACKAGES`, они не нужны для системы, но могут быть полезны для разработки. Выбирайте пункты на свое усмотрение.

и выполните сборку оболочки используя данные команды:
```bash
git clone https://github.com/DIMFLIX-OFFICIAL/meowrch.git
cd meowrch
python3 Builder/install.py
```

В меню необходимо предоставить разрешение на установку `dotfiles`, обновление баз, установку `BASE_PACKAGES`. Остальные пункты выбирайте самостоятельно.
Такое разделение опций позволяет выполнить только необходимое действие, к примеру лишь заменить `dotfiles` либо установить актуальные `DEV_PACKAGES` пакеты.

Если вы все сделали правильно, то после запуска вы получите готовую оболочку BSPWM.
```bash
startx
```

Из-за разного железа / разных дистрибутивов и прочих моментов, могут быть небольшие проблемы в отображении иконок, в работе с батареей / яркостью. Решение этих
проблем было показано в [данном видео](https://youtu.be/9zewiGf7j-A).
