#!/bin/bash

nm-applet &
pamac-tray &
blueman-applet &
lxsession &
killall picom
picom -b --config $HOME/.config/picom/picom.conf &