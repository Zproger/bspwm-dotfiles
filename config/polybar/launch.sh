#!/usr/bin/env bash

# Terminate already running bar instances
killall -q polybar

# Launch bar1 and bar2
echo "---" | tee -a /tmp/polybar1.log /tmp/polybar2.log

# Auto-detect the monitor for [bar/top], т.к. идентификатор (eDP-1 и т.п.) зависит от железа пользователя
export MONITOR=$(xrandr --query | awk '/ primary/{print $1; exit}')
[ -z "$MONITOR" ] && export MONITOR=$(xrandr --query | awk '/ connected/{print $1; exit}')

# Run on the desired monitor
if [[ $(xrandr -q | grep 'HDMI-1-1 connected' ) ]]; then
	polybar top_external -r >>/tmp/polybar1.log 2>&1 & disown
	polybar top -r >>/tmp/polybar1.log 2>&1 & disown
	echo "Polybar launched for two monitors"
else
	polybar top -r >>/tmp/polybar1.log 2>&1 & disown
	echo "Polybar launched for one monitor..."
fi
