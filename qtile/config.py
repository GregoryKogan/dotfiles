from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook
from libqtile import qtile
import arcobattery


COLOR_PALETTES = {
    "Dracula": {
        "background": "#282a36",
        "current_line": "#44475a",
        "selection": "#44475a",
        "foreground": "#f8f8f2",
        "comment": "#6272a4",
        "cyan": "#8be9fd",
        "green": "#50fa7b",
        "orange": "#ffb86c",
        "pink": "#ff79c6",
        "purple": "#bd93f9",
        "red": "#ff5555",
        "yellow": "#f1fa8c",
    },
    "TokyoNight(Storm)": {
        "background": "#24283b",
        "foreground": "#c0caf5",
        "selection": "#364A82",
        "comment": "#565f89",
        "red": "#f7768e",
        "orange": "#ff9e64",
        "yellow": "#e0af68",
        "green": "#9ece6a",
        "magenta": "#bb9af7",
        "cyan": "#7dcfff",
        "black": "#414868",
    },
}

UI_THEMES = {
    "Dracula": {
        "bar": {
            "size": 30,
            "margin": [7, 7, 0, 7],
            # 'margin': [30, 30, 0, 30],
            "background": COLOR_PALETTES["Dracula"]["background"],
        },
        "widget": {
            "font": "Ubuntu Mono",
            "fontsize": 16,
            "foreground": COLOR_PALETTES["Dracula"]["foreground"],
        },
        "systray": {
            "font": "Ubuntu Mono",
            "fontsize": 13,
            "background": COLOR_PALETTES["Dracula"]["background"],
            "foreground": COLOR_PALETTES["Dracula"]["foreground"],
            "icon_size": 20,
            "padding": 4,
        },
        "groupbox": {
            "font": "Monospace Bold",
            "fontsize": 14,
            "background": COLOR_PALETTES["Dracula"]["background"],
            "foreground": COLOR_PALETTES["Dracula"]["foreground"],
            "borderwidth": 3,
            "margin_y": 5,
            "margin_x": 0,
            "padding_y": 0,
            "padding_x": 7,
            "active": COLOR_PALETTES["Dracula"]["pink"],
            "inactive": COLOR_PALETTES["Dracula"]["comment"],
            "rounded": False,
            "highlight_color": COLOR_PALETTES["Dracula"]["current_line"],
            "highlight_method": "line",
            "this_current_screen_border": COLOR_PALETTES["Dracula"]["comment"],
            "this_screen_border": COLOR_PALETTES["Dracula"]["green"],
            "other_current_screen_border": COLOR_PALETTES["Dracula"]["green"],
            "other_screen_border": COLOR_PALETTES["Dracula"]["green"],
        },
        "unicode_icon": {
            "padding": 0,
            "fontsize": 20,
        },
        "left_arrow": {
            "padding": 0,
            "fontsize": 57,
        },
        "background": COLOR_PALETTES["Dracula"]["background"],
        "border_focus": COLOR_PALETTES["Dracula"]["purple"],
        "border_normal": COLOR_PALETTES["Dracula"]["current_line"],
        "even_color": COLOR_PALETTES["Dracula"]["selection"],
        "odd_color": COLOR_PALETTES["Dracula"]["comment"],
    },
    "TokyoNight(Storm)": {
        "bar": {
            "size": 30,
            "margin": [7, 7, 0, 7],
            # 'margin': [30, 30, 0, 30],
            "background": COLOR_PALETTES["TokyoNight(Storm)"]["background"],
        },
        "widget": {
            "font": "Ubuntu Mono",
            "fontsize": 16,
            "foreground": COLOR_PALETTES["TokyoNight(Storm)"]["foreground"],
        },
        "systray": {
            "font": "Ubuntu Mono",
            "fontsize": 13,
            "background": COLOR_PALETTES["TokyoNight(Storm)"]["background"],
            "foreground": COLOR_PALETTES["TokyoNight(Storm)"]["foreground"],
            "icon_size": 20,
            "padding": 4,
        },
        "groupbox": {
            "font": "Monospace Bold",
            "fontsize": 14,
            "background": COLOR_PALETTES["TokyoNight(Storm)"]["background"],
            "foreground": COLOR_PALETTES["TokyoNight(Storm)"]["foreground"],
            "borderwidth": 3,
            "margin_y": 5,
            "margin_x": 0,
            "padding_y": 0,
            "padding_x": 7,
            "active": COLOR_PALETTES["TokyoNight(Storm)"]["orange"],
            "inactive": COLOR_PALETTES["TokyoNight(Storm)"]["comment"],
            "rounded": False,
            "highlight_color": COLOR_PALETTES["TokyoNight(Storm)"]["black"],
            "highlight_method": "line",
            "this_current_screen_border": COLOR_PALETTES["TokyoNight(Storm)"][
                "comment"
            ],
            "this_screen_border": COLOR_PALETTES["TokyoNight(Storm)"]["green"],
            "other_current_screen_border": COLOR_PALETTES["TokyoNight(Storm)"]["green"],
            "other_screen_border": COLOR_PALETTES["TokyoNight(Storm)"]["green"],
        },
        "unicode_icon": {
            "padding": 0,
            "fontsize": 20,
        },
        "left_arrow": {
            "padding": 0,
            "fontsize": 57,
        },
        "background": COLOR_PALETTES["TokyoNight(Storm)"]["background"],
        "border_focus": COLOR_PALETTES["TokyoNight(Storm)"]["magenta"],
        "border_normal": COLOR_PALETTES["TokyoNight(Storm)"]["selection"],
        "even_color": COLOR_PALETTES["TokyoNight(Storm)"]["black"],
        "odd_color": COLOR_PALETTES["TokyoNight(Storm)"]["comment"],
    },
}

# color_theme = "Dracula"
color_theme = "TokyoNight(Storm)"

ui_theme = UI_THEMES[color_theme]
widget_defaults = {
    "font": "Ubuntu Mono",
    "fontsize": 16,
    "foreground": COLOR_PALETTES[color_theme]["foreground"],
    "background": COLOR_PALETTES[color_theme]["background"],
    "padding": 3,
}

extension_defaults = widget_defaults.copy()

home = os.path.expanduser("~")

mod = "mod4"  # mod key = super
ALT = "mod1"
terminal = guess_terminal()
browser = "firefox"
file_manager = "pcmanfm"
volume_app = "pavucontrol"
icon_folder = "~/.config/qtile/icons"
wlan_interface = "wlp2s0"
backlight_name = "intel_backlight"
wallpaper_folder = "~/Pictures/Wallpapers/"
run_launcher = "rofi -show drun"
screenshot_app = "xfce4-screenshooter"


### Custom functions ###
def open_run_launcher():
    qtile.cmd_spawn(run_launcher)


def open_wifi():
    qtile.cmd_spawn(f"{terminal} -e sudo nmtui")


def open_pacman():
    qtile.cmd_spawn(f"{terminal} -e sudo pacman -Syu")


keys = [
    # Custom keybindings
    Key([mod], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "r", lazy.spawn(run_launcher), desc="Launch run launcher"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    # Qtile keybindings
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Keyboard layout switching
    Key(
        [ALT],
        "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    # Sound
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer --change-volume -5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer --change-volume +5")),
    # Screen brightness
    Key([], "XF86MonBrightnessDown", lazy.spawn("backlight_control -5")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("backlight_control +5")),
    # Screenshot
    Key([], "F11", lazy.spawn(screenshot_app)),
    # Window management
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    # Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    # Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    # Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "control"], "Up", lazy.layout.grow()),
    Key([mod, "control"], "Down", lazy.layout.shrink()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

# Executed on startup
@hook.subscribe.startup_once
def autostart():
    subprocess.call([f"{home}/.config/qtile/autostart.sh"])


group_names = [
    ("WEB", {"layout": "monadtall"}),
    ("CHAT", {"layout": "monadtall"}),
    ("DEV", {"layout": "monadtall"}),
    ("SYS", {"layout": "monadtall"}),
    ("DOC", {"layout": "monadtall"}),
]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key([mod], str(i), lazy.group[name].toscreen())
    )  # Switch to another group
    keys.append(
        Key([mod, "shift"], str(i), lazy.window.togroup(name))
    )  # Send current window to another group

layouts = [
    layout.MonadTall(
        border_focus=ui_theme["border_focus"],
        border_normal=ui_theme["border_normal"],
        ratio=0.55,
        border_width=2,
        margin=7,
        # margin=30,
        grow_amount=5,
        single_border_width=0,
        single_margin=7,
    ),
    layout.Stack(
        num_stacks=1,
        margin=7,
        border_width=0,
    ),
    # layout.Max(),
    # layout.Columns(
    #     border_focus_stack=ui_theme['border_focus'],
    #     border_focus=ui_theme['border_focus'],
    #     border_normal=ui_theme['border_normal'],
    #     border_normal_stack=ui_theme['border_normal'],
    #     border_on_single=False,
    #     border_width=2,
    #     margin=4,
    #     margin_on_single=0,
    #     grow_amount=5,
    #     num_columns=2,
    #     fair=False,
    # ),
    # layout.Floating(
    #     border_focus=ui_theme['border_focus'],
    #     border_normal=ui_theme['border_normal'],
    #     border_width=2,
    # ),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Bsp(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]


panel_widgets = [
    widget.Sep(
        linewidth=0,
        padding=6,
        background=ui_theme["background"],
    ),
    # 'Start' icon
    widget.Image(
        filename=f"{icon_folder}/arcolinux.png",
        margin_x=5,
        margin_y=3,
        mouse_callbacks={"Button1": open_run_launcher},
    ),
    widget.Sep(
        linewidth=0,
        padding=2,
        background=ui_theme["background"],
    ),
    # Workspaces
    widget.GroupBox(**ui_theme["groupbox"]),
    widget.Sep(
        linewidth=0,
        padding=20,
        background=ui_theme["background"],
    ),
    # Window layout
    widget.WindowCount(
        fontsize=18,
        font="Ubuntu Mono Bold",
    ),
    widget.TextBox(
        text="🗔",
        font="Ubuntu Mono",
        fontsize="20",
    ),
    widget.CurrentLayout(font="Ubuntu Mono Bold", fontsize=18),
    widget.Sep(
        linewidth=0,
        padding=15,
        background=ui_theme["background"],
    ),
    widget.Spacer(),
    # Clock widget
    widget.Clock(
        format="%H:%M %A, %d %b",
        **ui_theme["widget"],
    ),
    widget.Spacer(),
    # Wallpapers
    widget.TextBox(
        text="",
        foreground=ui_theme["odd_color"],
        **ui_theme["left_arrow"],
    ),
    widget.Wallpaper(
        directory=wallpaper_folder,
        random_selection=True,
        background=ui_theme["odd_color"],
        label="⚘",
        font="Ubuntu Mono",
        fontsize="20",
        option="fill",
    ),
    # Volume
    widget.TextBox(
        text="",
        background=ui_theme["odd_color"],
        foreground=ui_theme["even_color"],
        **ui_theme["left_arrow"],
    ),
    widget.PulseVolume(
        emoji=True,
        font="Ubuntu Mono",
        volume_app=volume_app,
        limit_max_volume=True,
        mute_command="pulsemixer --toggle-mute",
        volume_up_command="pulsemixer --change-volume +5",
        volume_down_command="pulsemixer --change-volume -5",
        get_volume_command="pulsemixer --get-volume",
        background=ui_theme["even_color"],
        **ui_theme["unicode_icon"],
    ),
    widget.PulseVolume(
        font="Ubuntu Mono",
        volume_app=volume_app,
        limit_max_volume=True,
        mute_command="pulsemixer --toggle-mute",
        volume_up_command="pulsemixer --change-volume +5",
        volume_down_command="pulsemixer --change-volume -5",
        get_volume_command="pamixer --get-volume",
        background=ui_theme["even_color"],
        update_interval=0.1,
    ),
    # Keyboard layout
    widget.TextBox(
        text="",
        background=ui_theme["even_color"],
        foreground=ui_theme["odd_color"],
        **ui_theme["left_arrow"],
    ),
    widget.TextBox(
        text="⌨",
        fontsize="18",
        font="Ubuntu Mono",
        background=ui_theme["odd_color"],
    ),
    widget.KeyboardLayout(
        configured_keyboards=["us", "ru"],
        font="Ubuntu Mono",
        fontsize="16",
        background=ui_theme["odd_color"],
    ),
    # Systray
    widget.TextBox(
        text="",
        background=ui_theme["odd_color"],
        foreground=ui_theme["even_color"],
        **ui_theme["left_arrow"],
    ),
    widget.TextBox(
        text="📡",
        fontsize="18",
        font="Ubuntu",
        background=ui_theme["even_color"],
    ),
    widget.Wlan(
        interface=wlan_interface,
        format="{essid} {percent:2.0%}",
        mouse_callbacks={"Button1": open_wifi},
        background=ui_theme["even_color"],
    ),
    widget.Systray(
        icon_size=25,
        background=ui_theme["even_color"],
        **ui_theme["widget"],
    ),
    # Screen brightness
    widget.TextBox(
        text="",
        background=ui_theme["even_color"],
        foreground=ui_theme["odd_color"],
        **ui_theme["left_arrow"],
    ),
    widget.TextBox(
        text="🔆",
        font="Ubuntu Mono",
        fontsize="18",
        background=ui_theme["odd_color"],
    ),
    widget.Backlight(
        backlight_name=backlight_name,
        background=ui_theme["odd_color"],
    ),
    # Battery wdiget
    widget.TextBox(
        text="",
        background=ui_theme["odd_color"],
        foreground=ui_theme["even_color"],
        **ui_theme["left_arrow"],
    ),
    arcobattery.BatteryIcon(
        padding=0,
        scale=0.7,
        y_poss=2,
        theme_path=f"{home}/.config/qtile/icons/battery_icons_horiz",
        update_interval=5,
        background=ui_theme["even_color"],
    ),
    widget.Battery(
        format="{percent:2.0%}",
        discharge_char="",
        charge_char="",
        empty_char="",
        full_char="F",
        low_percentage=0.15,
        low_foreground="FF0000",
        background=ui_theme["even_color"],
        **ui_theme["widget"],
    ),
    widget.Sep(
        linewidth=0,
        padding=7,
        background=ui_theme["even_color"],
    ),
]


screens = [
    Screen(
        top=bar.Bar(panel_widgets, **ui_theme["bar"]),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus=ui_theme["border_focus"],
    border_normal=ui_theme["border_normal"],
    border_width=2,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
