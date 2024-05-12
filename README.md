# dotfiles

My MacOS/ArchLinux configuration files

This config uses **[Universal Home Builder](https://github.com/GregoryKogan/universal-home-builder)** to manage configs.  
I wrote it myself and very proud of my creation! I would be very grateful if you check it out.

## Install

```shell
git clone https://github.com/GregoryKogan/dotfiles.git ~/dotfiles
```

## Usage

**1. Install [Universal Home Builder](https://github.com/GregoryKogan/universal-home-builder)**

```shell
git clone https://github.com/GregoryKogan/universal-home-builder.git ~/uhb
```

**2. Build home directory with UHB**

`<host>` is an entry point for UHB config. Available hosts:

- `arch`
- `macos`

```shell
~/uhb/build ~/dotfiles/hosts/<host>
```

This may require to input super user's password a few times.

**3. Reboot**

Although most of the programs do not require a reboot to work well with new configs, some things may break without it.  
For example `$SHELL` environment variable will only be properly set after reboot.

```shell
reboot
```

## Misc

### ArchLinux-ARM installation

```shell
useradd -m -G wheel <username>
passwd <username>
pacman -S sudo vi
visudo
```

Uncomment `%wheel ALL(ALL:ALL) ALL` line  
Relogin as `<username>`

```shell
sudo pacman -Syu
sudo pacman -S git python3
git clone https://github.com/GregoryKogan/universal-home-builder.git ~/uhb
git clone https://github.com/GregoryKogan/dotfiles.git
~/uhb/build ~/dotfiles/hosts/arch
reboot
```
