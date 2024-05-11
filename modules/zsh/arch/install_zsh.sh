#!/bin/bash

echo "Installing zsh"
sudo pacman -S zsh --needed --noconfirm

echo "Setting zsh as default shell"
chsh -s $(which zsh)

echo "Installing zoxide"
sudo pacman -S zoxide --needed --noconfirm

echo "Installing eza"
sudo pacman -S eza --needed --noconfirm

echo "Installing fastfetch"
sudo pacman -S fastfetch --needed --noconfirm