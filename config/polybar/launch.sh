#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log

# Auto-detect the monitor for [bar/top], т.к. идентификатор (eDP-1 и т.п.) зависит от железа пользователя
export MONITOR=$(xrandr --query | awk '/ primary/{print $1; exit}')
[ -z "$MONITOR" ] && export MONITOR=$(xrandr --query | awk '/ connected/{print $1; exit}')

# Auto-detect a second connected monitor for [bar/top_external] instead of hardcoding
# "HDMI-1-1" - имя внешнего монитора зависит от порта/видеокарты пользователя
export MONITOR_EXTERNAL=$(xrandr --query | awk -v skip="$MONITOR" '/ connected/{if ($1 != skip) {print $1; exit}}')

# Auto-detect the battery device for [module/battery], т.к. имя отличается между
# производителями (BAT0, BAT1 и т.д.) - тот же фикс, что и в bin/battery-alert
BATTERY_PATH=$(find /sys/class/power_supply -maxdepth 1 -name 'BAT*' 2>/dev/null | head -n1)
[ -n "$BATTERY_PATH" ] && export BATTERY=$(basename "$BATTERY_PATH")

# Auto-detect the backlight device for [module/backlight] вместо захардкоженного
# "amdgpu_bl2" - тот же фикс, что и в bin/brightness
BACKLIGHT_PATH=$(find /sys/class/backlight -mindepth 1 -maxdepth 1 2>/dev/null | head -n1)
[ -n "$BACKLIGHT_PATH" ] && export BACKLIGHT_CARD=$(basename "$BACKLIGHT_PATH")

# Auto-detect the wireless interface for [module/wlan] вместо захардкоженного "wlan0"
export WLAN_IFACE=$(ip -o link show 2>/dev/null | awk -F': ' '$2 ~ /^wl/{print $2; exit}')

# Run on the desired monitor
if [ -n "$MONITOR_EXTERNAL" ]; then
	polybar top_external -r >>/tmp/polybar1.log 2>&1 & disown
	polybar top -r >>/tmp/polybar1.log 2>&1 & disown
	echo "Polybar launched for two monitors"
else
	polybar top -r >>/tmp/polybar1.log 2>&1 & disown
	echo "Polybar launched for one monitor..."
fi
