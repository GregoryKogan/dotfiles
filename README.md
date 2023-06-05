# dotfiles
My MacOS/Linux configuration files

## Usgage
### Clone inside '~/.dotfiles'
via `HTTPS`:
```shell
git clone https://github.com/GregoryKogan/dotfiles.git ~/.dotfiles
```
or via `SSH`:
```shell
git clone git@github.com:GregoryKogan/dotfiles.git ~/.dotfiles
```

### Install software
#### Install [Homebrew](https://brew.sh/) (for MacOS)
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
#### Install everything else via homebrew (for MacOS)
```shell
brew bundle --file ~/.dotfiles/Brewfile
```
To overwrite list of software to install with your current homebrew installed programs run
```shell
rm ~/.dotfiles/Brewfile; brew bundle dump --describe --file ~/.dotfiles/Brewfile
```

### Create symlinks
```shell
# zsh
ln -s ~/.dotfiles/zsh/.zshrc ~/.zshrc
# nano
ln -s ~/.dotfiles/.nanorc ~/.nanorc
# git
ln -s ~/.dotfiles/.gitconfig ~/.gitconfig
# alacritty
mkdir ~/.config/alacritty; ln -s ~/.dotfiles/alacritty/alacritty.yml ~/.config/alacritty/alacritty.yml
# skhd (for MacOS)
mkdir ~/.config/skhd; ln -s ~/.dotfiles/skhd/skhdrc ~/.config/skhd/skhdrc
```
