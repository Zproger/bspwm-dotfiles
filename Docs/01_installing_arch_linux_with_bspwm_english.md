This file contains the command sequence that is needed to fully install an Arch Linux system.
It also includes the use of the builder from the repository, which automatically deploys the BSPWM environment.

### Connect to WiFi (optional)
```bash
iwctl
device list
station your_device_name scan
station your_device_name get-networks
station your_device_name connect SSID
ping google.com
```

### Setting a large font (optional)
```bash
pacman -S terminus-font
cd /usr/share/kbd/consolefonts
setfont ter-u32b.psf.gz
```

### Partitioning a disk under UEFI GPT with encryption
If you are using an SSD, then your partitions will look something like this:
- `/dev/nvme0n1p1`
- `/dev/nvme0n1p2`

In that case, replace `/dev/sda` with `/dev/nvme0n1`.
And partitions `/dev/sda1` and `/dev/sda2` to `/dev/nvme0n1p1` and `/dev/nvme0n1p2`.

```bash
parted /dev/sda
mklabel gpt
mkpart ESP fat32 1Mib 512Mib
set 1 boot on

mkpart primary
# file system (press ENTER)
# start: 513Mib
# end: 100%

quit
```

### Encrypt the partition that was prepared earlier
```bash
cryptsetup luksFormat /dev/sda2
# sda2 is the encrypted partition
# enter YES in capital letters
# enter the password 2 times

# Open the encrypted partition
cryptsetup open /dev/sda2 luks

# Check the partitions
ls /dev/mapper/*

# Create logical partitions inside the encrypted partition
pvcreate /dev/mapper/luks
vgcreate main /dev/mapper/luks

# Put 100% of the encrypted partition into the root logical partition
lvcreate -l 100%FREE main -n root

# View all logical partitions
lvs
```

### Partition preparation and mounting
```bash
### Format the partition to ext4
mkfs.ext4 /dev/mapper/main-root

# Format boot partition to Fat32, boot is on physical partition /dev/sda1
mkfs.fat -F 32 /dev/sda1

# Mount the partitions for installing the system
mount /dev/mapper/main-root /mnt
mkdir /mnt/boot

# Mount the boot partition to the current working folder
mount /dev/sda1 /mnt/boot
```

### Build the kernel and basic software
```bash
### Install basic software
pacstrap -K /mnt base linux linux-firmware base-devel lvm2
dhcpcd net-tools iproute2 networkmanager vim micro efibootmgr iwd

# Generate fstab
genfstab -U /mnt >> /mnt/etc/fstab
cat /mnt/etc/fstab

# Configure the system
arch-chroot /mnt

# You need to uncomment ru_RU and en_US in this file
micro /etc/locale.gen

# Generate locales
locale-gen

# Set the time
ln -sf /usr/share/zoneinfo/Europe/Kiev /etc/localtime
hwclock --systohc

# Specify the hostname
echo "arch" > /etc/hostname

# Specify the password for the root user
passwd

# Add a new user and configure permissions
useradd -m -G wheel,users -s /bin/bash user
passwd user
systemctl enable dhcpcd
systemctl enable iwd.service

micro /etc/mkinitcpio.conf
# Rebuild the kernel. Find the line HOOKS=(base udev autodetect modconf kms
# keyboard keymap consolefont block filesystems fsck)

# and replace it with:

# HOOKS=(base udev autodetect modconf kms keyboard keymap consolefont block filesystems encrypt lvm2 fsck)

# Start the kernel rebuild process
mkinitcpio -p linux
```

### Installing the bootloader
```bash
bootctl install --path=/boot
cd /boot/loader
micro loader.conf

# Insert the following config into loader.conf:
timeout 3
default arch

# Create a configuration for startup
cd /boot/loader/entries
micro arch.conf

# Insert the following into arch.conf:
# The UUID can be obtained with the blkid command
title Arch Linux by ZProger
linux /vmlinuz-linux
initrd /initramfs-linux.img
options rw cryptdevice=UUID=uuid_от_/dev/sda2:main root=/dev/mapper/main-root

# Grant sudo permissions
sudo EDITOR=micro visudo
# After opening, comment out %wheel ALL=(ALL:ALL) ALL

# Log out and reboot
Ctrl+D
umount -R /mnt
reboot
```

### Install the shell
If you get errors when booting the system, or if you get a window from the iso image of Arch, then you need to unmount the image or remove the flash drive.
Also make sure that the boot is under EFI, especially for virtual machines.

Before running these commands, log in as user. During the boot phase, the system will ask you to enter a password to decrypt the hard disk area,
and you will then be prompted to log in to the user by entering your username and password. After authorization, perform the following:

```bash
sudo pacman -Sy
sudo pacman -S xorg bspwm sxhkd xorg-xinit xterm git python3

# Customize xinitrc
micro /etc/X11/xinit/xinitrc

# Disable any other exec lines and add a line to the end of the file:
exec bspwm
```

Download the repository locally, but before executing builder I recommend going to `Builder/packages.py` and seeing the packages that will be installed.
I don't recommend editing `BASE_PACKAGES` as they are necessary for the shell to work properly, however you are free to edit other kinds of packages.
At the builder stage you will be prompted to install `DEV_PACKAGES`, these are not needed for the system but can be useful for development. Select items at your discretion.

and build the shell using these commands:
```bash
git clone https://github.com/DIMFLIX-OFFICIAL/meowrch.git
cd meowrch
python3 Builder/install.py
```

In the menu you need to give permission to install `dotfiles`, update bases, install `BASE_PACKAGES`. The rest of the options are up to you.
This division of options allows you to perform only the necessary action, for example, just replace `dotfiles` or install current `DEV_PACKAGES` packages.

If you have done everything correctly, you will get a ready BSPWM shell after launching.
```bash
startx
```

Due to different hardware / different distributions and other things, there may be small issues in displaying icons, battery / brightness handling. The solution to these
problems were shown in [this video](https://youtu.be/9zewiGf7j-A).
