#!/bin/bash

BRIGHTNESS_VALUE=`brightnessctl | grep -o "(.*" | tr -d "()"`
BRIGHTNESS_NR=${BRIGHTNESS_VALUE//%}
BRIGHTNESS_ICON='%{F#61afef} %{F-}'

case "$1" in
    up)
        brightnessctl set +5%
        ;;
    down)
        brightnessctl set 5%-
        ;;
    max)
        brightnessctl set 100%
        ;;
    min)
        brightnessctl set 1%
        ;;
    status)
        echo "$BRIGHTNESS_ICON $BRIGHTNESS_VALUE"
        ;;
    *)
        echo "Invalid argument. Use 'up', 'down', or 'status'."
        ;;
esac
