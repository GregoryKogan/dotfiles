#!/bin/bash

echo "Installing zsh-autosuggestions..."
if [ ! -d $ZSH/plugins/zsh-autosuggestions ]; then
    git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH/plugins/zsh-autosuggestions
fi

echo "Installing zsh-syntax-highlighting..."
if [ ! -d $ZSH/plugins/zsh-syntax-highlighting ]; then
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH/plugins/zsh-syntax-highlighting
fi