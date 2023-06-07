# dotfiles
My MacOS/ArchLinux configuration files

![image](https://github.com/GregoryKogan/dotfiles/assets/60318411/70570850-a6e6-41bc-a77e-76a39c1dce3c)

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
#### MacOS
##### Install [Homebrew](https://brew.sh/) (for MacOS)
```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
##### Install everything else via homebrew (for MacOS)
```shell
brew bundle --file ~/.dotfiles/macos_software/Brewfile
```
To overwrite list of software to install with your current homebrew installed programs run
```shell
rm ~/.dotfiles/macos_software/Brewfile; brew bundle dump --describe --file ~/.dotfiles/macos_software/Brewfile
```
#### Arch
##### Give run permission to install script
```shell
sudo chmod +x ~/.dotfiles/arch_software/install_software_arch.sh
```
##### Run the script
```shell
~/.dotfiles/arch_software/install_software_arch.sh
```

### Create symlinks
```shell
# images
ln -s ~/.dotfiles/images ~/Pictures

# zsh
ln -s ~/.dotfiles/zsh/.zshrc ~/.zshrc

# nvim
ln -s ~/.dotfiles/nvim ~/.config
# install go formatting packages for nvim
go install mvdan.cc/gofumpt@latest
go install -v github.com/incu6us/goimports-reviser/v3@latest
go install github.com/segmentio/golines@latest

# nano
ln -s ~/.dotfiles/.nanorc ~/.nanorc

# git
ln -s ~/.dotfiles/.gitconfig ~/.gitconfig

# alacritty
ln -s ~/.dotfiles/alacritty ~/.config

# starship
ln -s ~/.dotfiles/starship.toml ~/.config/starship.toml

# xournalpp
ln -s ~/.dotfiles/xournalpp ~/.config

# skhd (for MacOS)
ln -s ~/.dotfiles/skhd ~/.config

# cups (for MacOS)
ln -s ~/.dotfiles/.cups ~/.config

# picom (for Linux)
ln -s ~/.dotfiles/picom ~/.config

# qtile (for Linux)
ln -s ~/.dotfiles/qtile ~/.config

# rofi (for Linux)
ln -s ~/.dotfiles/rofi ~/.config
```

#### Exceptions
- Telegram Dracula theme is inside `telegram` directory. How to apply it: https://draculatheme.com/telegram
