#!/bin/bash

echo "Installing zsh..."
sudo pacman -S zsh

echo "Setting zsh as default shell..."
chsh -s $(which zsh)

echo "Installing zoxide..."
sudo pacman -S zoxide

echo "Installing eza..."
sudo pacman -S eza

echo "Installing fastfetch..."
sudo pacman -S fastfetch