#!/bin/bash

selected=$(greenclip print | rofi -dmenu -i -p "Clipboard:")

if [ -n "$selected" ]; then
    echo -n "$selected" | xclip -selection clipboard
fi