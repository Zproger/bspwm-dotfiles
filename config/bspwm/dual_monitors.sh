#!/bin/sh

# Determine monitor names dynamically instead of hardcoding them: xrandr output
# names differ across GPU drivers/docks, and a fixed name that doesn't match
# the real hardware makes bspc silently fail to create any desktop at all.
CONNECTED_MONITORS=$(xrandr -q | grep " connected" | awk '{print $1}')
INTERNAL_MONITOR=$(echo "$CONNECTED_MONITORS" | grep -E '^(eDP|LVDS)' | head -n1)
EXTERNAL_MONITOR=$(echo "$CONNECTED_MONITORS" | grep -vE '^(eDP|LVDS)' | head -n1)

# No laptop panel found (e.g. desktop PC) - treat the only monitor as internal
# and skip the dual-monitor layout below.
if [ -z "$INTERNAL_MONITOR" ]; then
  INTERNAL_MONITOR="$EXTERNAL_MONITOR"
  EXTERNAL_MONITOR=""
fi

monitor_add() {
  # Move first 5 desktops to external monitor
  for desktop in $(bspc query -D --names -m "$INTERNAL_MONITOR" | sed 5q); do
    bspc desktop "$desktop" --to-monitor "$EXTERNAL_MONITOR"
  done

  # Remove default desktop created by bspwm
  bspc desktop Desktop --remove

  # reorder monitors
  bspc wm -O "$EXTERNAL_MONITOR" "$INTERNAL_MONITOR"
}

monitor_remove() {
  # Add default temp desktop because a minimum of one desktop is required per monitor
  bspc monitor "$EXTERNAL_MONITOR" -a Desktop

  # Move all desktops except the last default desktop to internal monitor
  for desktop in $(bspc query -D -m "$EXTERNAL_MONITOR");	do
    bspc desktop "$desktop" --to-monitor "$INTERNAL_MONITOR"
  done

  # delete default desktops
  bspc desktop Desktop --remove

  # reorder desktops
  bspc monitor "$INTERNAL_MONITOR" -o 1 2 3 4 5 6 7 8 9
}

# On first load setup default workspaces
if [ -n "$EXTERNAL_MONITOR" ]; then
  bspc monitor "$EXTERNAL_MONITOR" -d 1 2 3 4 5
  bspc monitor "$INTERNAL_MONITOR" -d 6 7 8 9
  bspc wm -O "$EXTERNAL_MONITOR" "$INTERNAL_MONITOR"
else
  bspc monitor "$INTERNAL_MONITOR" -d 1 2 3 4 5 6 7 8 9
fi

if [ -n "$EXTERNAL_MONITOR" ]; then
  # set xrandr rules for docked setup
  xrandr --output "$INTERNAL_MONITOR" --mode 1920x1080 --pos 0x0 --rotate normal
  xrandr --output "$EXTERNAL_MONITOR" --primary --mode 2560x1440 --pos 1920x0 --rotate normal --left-of "$INTERNAL_MONITOR"

  if [[ $(bspc query -D -m "${EXTERNAL_MONITOR}" | wc -l) -ne 5 ]]; then
    monitor_add
  fi
  bspc wm -O "$EXTERNAL_MONITOR" "$INTERNAL_MONITOR"
else
  # set xrandr rules for mobile setup
  xrandr --output "$INTERNAL_MONITOR" --primary --mode 1920x1080 --pos 0x0 --rotate normal
  if [[ $(bspc query -D -m "${INTERNAL_MONITOR}" | wc -l) -ne 10 ]]; then
    monitor_remove
  fi
fi
