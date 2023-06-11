#!/usr/bin/env bash

name=$(ls -1 ~/.dotfiles/colorscripts/colorscripts/ | sort -R | head -1)
path="~/.dotfiles/colorscripts/colorscripts/"$name
exec $path

