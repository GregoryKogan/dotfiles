#!/bin/bash

echo "Installing Hyprland"
sudo pacman -S hyprland --needed --noconfirm

echo "Installing Kitty"
sudo pacman -S kitty --needed --noconfirm

echo "Installing gtk3"
sudo pacman -S gtk3 --needed --noconfirm
