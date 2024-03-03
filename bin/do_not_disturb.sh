#!/usr/bin/env bash

notify="notify-send"
tmp_disturb="/tmp/xmonad/donotdisturb"
tmp_disturb_colorfile="/tmp/xmonad/donotdisturb/color"

if [ ! -d $tmp_disturb ]; then
	mkdir -p $tmp_disturb
fi

case `dunstctl is-paused` in
    true)
        dunstctl set-paused false &
        $notify "Dunst: Active" &
	echo "#84afdb" > $tmp_disturb_colorfile
        ;;
    false)
        $notify "Dunst: Mute Notify" &
	echo "#c47eb7" > $tmp_disturb_colorfile &
        (sleep 3 && dunstctl close && dunstctl set-paused true)
        ;;
esac
