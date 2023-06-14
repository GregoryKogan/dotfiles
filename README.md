# dotfiles
My MacOS/Linux configuration files

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

### Wire up configs
- [images](#images)
- [zsh](#zsh)
- [nvim](#nvim)
- [nano](#nano)
- [git](#git)
- [alacritty](#alacritty)
- [starship](#starship)
- [xournalpp](#xournalpp)
- [skhd](#skhd)
- [cups](#cups)
- [picom](#picom)
- [qtile](#qtile) 
- [rofi](#rofi)
- [telegram](#telegram)

#### images
```shell
ln -s ~/.dotfiles/images ~/Pictures
```

#### zsh
Link config (requires subtle changes according to os)
```shell
ln -s ~/.dotfiles/zsh/.zshrc ~/.zshrc
```
Install dependencies (Linux)
```shell
# zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
# exa (Ubuntu)
sudo apt install exa
# exa (Arch)
sudo pacman -S exa
# exa (Fedora)
sudo dnf install exa
```
Install dependencies (MacOS)
```shell
# zsh-autosuggestions
brew install zsh-autosuggestions
# z
brew install z
# exa
brew install exa
```
Set zsh as default shell
```shell
chsh -s $(which zsh)
```

#### nvim
Install [NvChad](https://nvchad.com/)
```shell
git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
```
Link configs
```shell
ln -s ~/.dotfiles/nvim/custom ~/.config/nvim/lua
```

#### nano
```shell
ln -s ~/.dotfiles/nano/.nanorc ~/.nanorc
```

#### git
```shell
ln -s ~/.dotfiles/git/.gitconfig ~/.gitconfig
```

#### alacritty
```shell
ln -s ~/.dotfiles/alacritty ~/.config
```

#### starship
```shell
ln -s ~/.dotfiles/starship/starship.toml ~/.config/starship.toml
```

#### xournalpp
```shell
ln -s ~/.dotfiles/xournalpp ~/.config
```

#### skhd
```shell
ln -s ~/.dotfiles/skhd ~/.config
```

#### cups
```shell
ln -s ~/.dotfiles/cups/.cups ~/.config
```

#### picom
```shell
ln -s ~/.dotfiles/picom ~/.config
```

#### qtile
```shell
ln -s ~/.dotfiles/qtile ~/.config
```

#### rofi
```shell
ln -s ~/.dotfiles/rofi ~/.config
```

#### telegram 
Telegram Dracula theme is inside `./telegram` directory. How to apply it: https://draculatheme.com/telegram

