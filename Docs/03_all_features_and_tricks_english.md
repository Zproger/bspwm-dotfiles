### Automatically build components
By running `Builder/install.py` during the installation phase, it downloads all the necessary packages, which also
will be customized after the build. You don't need to manually customize themes and make edits to the software, after the
builder is executed, all software is immediately configured and customized.

### Browsers
The `Firefox` and `Chromium` browsers are installed by default. It is to `Firefox` that color
themes and some privacy patches. With additional edits, you can use the
the Firefox search box as a calculator.

### No extra stuff
Right from the start the shell consumes only 400-700mb of memory. All software is selected in such a way,
to eliminate many dependencies and heavy components.

### Many handy scripts in bin/:
- `bin/color-scripts`: Scripts for displaying beautiful animations and images in the terminal;
- `bin/fetchs`: A set of fetches for outputting system and hardware information;
- `bin/battery-alert`: Monitors battery power and sends notifications when the battery is low and the device needs to be unplugged;
- `bin/brightness`: Allows you to control the brightness of the monitor;
- `bin/change_language.sh`: Switch the layout;
- `bin/clear_images_meta`: Clear the metadata of all images in this folder;
- `bin/do_not_disturb.sh`: Disables all notifications. Switches to "Do Not Disturb" mode;
- `bin/rofi-menus/powermenu`: Script for power management;
- `bin/random_wallpaper`: Sets a random wallpaper on the desktop;
- `bin/screen-lock`: Lock the desktop screen;
- `bin/terminal_fullscreen`: Open a beautiful terminal to full screen;
- `bin/testfonts`: Test fonts and display all characters on the screen;
- `bin/toggle-polybar`: Allows you to minimize or maximize Polybar;
- `bin/untar_all`: Unzips all tar files inside the startup directory;
- `bin/unzip_all`: Unzips all zip files inside the startup directory;
- `bin/volume`: Controls the sound on the system;
- `bin/wallpaper_filter.py`: Removes all images that do not match the specified size;
- `bin/weather`: Output the weather of the location specified in the file;
- `bin/weather2`: Output the weather of the location specified in the file using the GUI;
- `bin/rofi-menus/rofi-wifi-menu`: Software to control wifi;
- `bin/rofi-menus/rofi-ethernet-menu`: Software to control ethernet;
- `bin/rofi-menus/rofi-clipboard-manager`: Clipboard management software;
- `bin/xcolor-pick`: Allows you to select a color on the screen and puts the hex value of the color into a buffer;
- `bin/ytd`: Download videos from youtube. There is support for multiple formats;
- `bin/ytd_audio`: Download only audio track from youtube video;
- `bin/ytd_video`: Download full video from youtube;

