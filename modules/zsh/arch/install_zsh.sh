#!/bin/bash

echo "Installing zsh"
sudo pacman -S zsh --noconfirm

echo "Setting zsh as default shell"
chsh -s $(which zsh)

echo "Installing zoxide"
sudo pacman -S zoxide --noconfirm

echo "Installing eza"
sudo pacman -S eza --noconfirm

echo "Installing fastfetch"
sudo pacman -S fastfetch --noconfirm