#!/bin/bash

# Создаем новый терминал и запускаем 4 черепах
gnome-terminal -- bash -c "ros2 run turtlesim turtlesim_node; exec bash" &
gnome-terminal -- bash -c "ros2 run turtlesim turtlesim_node; exec bash" &
gnome-terminal -- bash -c "ros2 run turtlesim turtlesim_node; exec bash" &
gnome-terminal -- bash -c "ros2 run turtlesim turtlesim_node; exec bash" &

# Даем время для старта всех черепах
sleep 5

# Устанавливаем параметр background_g для каждой из черепах
ros2 param set /turtlesim1/background_g 124
ros2 param set /turtlesim2/background_g 124
ros2 param set /turtlesim3/background_g 124
ros2 param set /turtlesim4/background_g 124

# Захват скриншота
gnome-screenshot -f ~/Desktop/screenshot.png

# Сохранение списка сервисов
ros2 service list > ~/Desktop/rosservice_list.txt

# Сохранение параметров сервера
ros2 param list > ~/Desktop/parameter_server.txt

echo "Все действия выполнены! Скриншот, сервисы и параметры сохранены на рабочем столе."
