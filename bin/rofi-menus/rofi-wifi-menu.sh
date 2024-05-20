#!/usr/bin/env bash

# Load NetworkManager
network_status=$(ps aux | grep NetworkManager | grep -v grep)

# Если служба не запущена
if [ -z "$network_status" ]; then
  # TODO: Скрываем ввод пароля
  echo -n "Root Password: "
  read -s password
  echo $password | sudo -S systemctl start NetworkManager
fi

# Запускаем проверку доступных SSID
notify-send "Getting list of available Wi-Fi networks..."
wifi_list=$(nmcli --fields "IN-USE,SECURITY,SSID" device wifi list | sed 1d | sed 's/  */ /g' | sed -E "s/WPA*.?\\S*/ /g" | sed "s/^--/ /g" | sed "s/  //g" | sed "/--/d" | sed 's/^* //' | sed '/^ /! s/^/  /')

connected=$(nmcli -fields WIFI g)
if [[ "$connected" =~ "enabled" ]]; then
  toggle="󱛅  Disable Wi-Fi"
elif [[ "$connected" =~ "disabled" ]]; then
  toggle="󱚽  Enable Wi-Fi"
fi

chosen_network=$(echo -e "$toggle\n$wifi_list" | uniq -u | rofi -dmenu -i -selected-row 1 -p "Wi-Fi SSID: " )
# Удаляем специальные символы из начала выбранного имени сети
chosen_id=$(echo "${chosen_network:3}" | sed 's/^[^a-zA-Z0-9]*//' | xargs)

# Анализирует список предварительно настроенных подключений,
# чтобы узнать, содержит ли он уже выбранный SSID.
# Это ускоряет процесс подключения
if [ -z "$chosen_network" ]; then
  exit
elif [ "$chosen_network" = "󱚽  Enable Wi-Fi" ]; then
  nmcli radio wifi on
elif [ "$chosen_network" = "󱛅  Disable Wi-Fi" ]; then
  nmcli radio wifi off
else
  # Управление подключением/отключением и возможностью забыть сеть
  action=$(echo -e "Connect\nDisconnect\nForget" | rofi -dmenu -p "Action: ")
  case $action in
    "Connect")
      # Сообщение, отображаемое при успешной активации соединения
      success_message="You are now connected to the Wi-Fi network \"$chosen_id\"."
      # Установить известные сети
      saved_connections=$(nmcli -g NAME connection show)
      if [[ $(echo "$saved_connections" | grep -w "$chosen_id") ]]; then
        nmcli connection up "$chosen_id" | grep "successfully" && notify-send "Connection Established" "$success_message"
      else
        wifi_password=$(rofi -dmenu -p "Password: " -password)
        nmcli device wifi connect "$chosen_id" password "$wifi_password" | grep "successfully" && notify-send "Connection Established" "$success_message"
      fi
      ;;
    "Disconnect")
      nmcli device disconnect wlan0 && notify-send "Disconnected" "You have been disconnected from $chosen_id."
      ;;
    "Forget")
      nmcli connection delete "$chosen_id" && notify-send "Forgotten" "The network $chosen_id has been forgotten."
      ;;
    *)
      exit
      ;;
  esac
fi
