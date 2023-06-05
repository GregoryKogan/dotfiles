echo "##==##==##==UPDATING PACKAGES==##==##==##"
sudo pacman -Syu;

echo "##==##==##==INSTALLING YAY==##==##==##"
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay

echo "##==##==##==INSTALLING PACMAN PACKAGES==##==##==##"
sudo pacman -S --needed - < pacman_packages.txt
sudo pacman -Syu

echo "##==##==##==INSTALLING AUR PACKAGES==##==##==##"
yay -S --needed - < yay_packages.txt
yay

echo "##==##==##==INSTALLING PYTHON LIBS==##==##==##"
pip3 install iwlib

echo "##==##==##==CONFIGURING SNAP==##==##==##"
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap

echo echo "##==##==##==INSTALLING OTHER SOFTWARE==##==##==##"
# Starship
sh -c "$(curl -fsSL https://starship.rs/install.sh)"

# Gtk Dracula
git clone https://github.com/dracula/gtk.git
sudo mkdir ~/.themes
cd
sudo cp -r Linux-Configs/gtk/ ~/.themes
rm -rf Linux-Configs/gtk
cd Linux-Configs/

# Icons Dracula
wget https://github.com/dracula/gtk/files/5214870/Dracula.zip
unzip Dracula.zip
rm Dracula.zip
cd
sudo mkdir ~/.icons
sudo cp -r Linux-Configs/Dracula/ ~/.icons/
rm -rf Linux-Configs/Dracula/
cd Linux-Configs/