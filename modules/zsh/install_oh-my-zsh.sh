#!/bin/bash

echo "Installing Oh-My-Zsh!"

if [ -d "$HOME/.oh-my-zsh" ]; then
  echo "Oh My Zsh is already installed"
  exit 0
fi

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
