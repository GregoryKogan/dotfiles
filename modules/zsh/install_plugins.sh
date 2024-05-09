#!/bin/bash

echo "Installing zsh-autosuggestions..."
if [ ! -d $HOME/.oh-my-zsh/plugins/zsh-autosuggestions ]; then
    git clone https://github.com/zsh-users/zsh-autosuggestions.git $HOME/.oh-my-zsh/plugins/zsh-autosuggestions
fi

echo "Installing zsh-syntax-highlighting..."
if [ ! -d $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting ]; then
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $HOME/.oh-my-zsh/plugins/zsh-syntax-highlighting
fi