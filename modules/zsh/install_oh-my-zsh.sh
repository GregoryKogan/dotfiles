#!/bin/bash

echo "Installing Oh My Zsh"

if [ -d "$HOME/.oh-my-zsh" ]; then
  echo "Oh My Zsh is already installed"
  exit 0
fi

cp $HOME/.zshrc $HOME/.backup-zshrc
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
rm $HOME/.zshrc
rm $HOME/.zshrc.pre-oh-my-zsh
mv $HOME/.backup-zshrc $HOME/.zshrc
