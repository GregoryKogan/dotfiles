#!/bin/bash

if [ ! -d ~/.config/alacritty/themes ]; then
    echo "Installing Alacritty themes"
    git clone https://github.com/alacritty/alacritty-theme ~/.config/alacritty/themes
fi