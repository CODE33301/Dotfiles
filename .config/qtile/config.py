###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Package imports                                     ###
###                                                                                         ###
###############################################################################################
###############################################################################################
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.utils import guess_terminal
from libqtile import bar, layout, widget
from libqtile.lazy import lazy

from colors import selectedTheme
import subprocess
import random
import os

from Xlib import X, display
from Xlib.ext import randr
from pprint import pprint

d = display.Display()
s = d.screen()
r = s.root
res = r.xrandr_get_screen_resources()._data
# Dynamic multiscreen!
num_screens = 0
for output in res['outputs']:
    print("Output %d:" % (output))
    mon = d.xrandr_get_output_info(output, res['config_timestamp'])._data
    print("%s: %d" % (mon['name'], mon['num_preferred']))
    if mon['num_preferred']:
        num_screens += 1
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                  Personal Variables                                     ###
###                                                                                         ###
###############################################################################################
###############################################################################################
mod = "mod4"
terminal = "terminology"
browser = "firefox"
fileManager = "nautilus"
torBrowser = r".tor-browser_en-US/Browser/start-tor-browser"
currentKernel = os.listdir('/lib/modules')[0]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                        Key Bindings                                     ###
###                                                                                         ###
###   * A list of available commands that can be bound to keys can be found at https://docs.qtile.org/en/latest/manual/config/lazy.html
###                                                                                         ###
###############################################################################################
###############################################################################################
keys = [
    # Switch Focus between windows - Will Not Work With Stack
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack. Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink. Columns
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("st"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "p", lazy.spawn("dmenu_run -h 30"), desc="Run dmenu_run"),
]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                        Define groups                                    ###
###                                                                                         ###
###############################################################################################
###############################################################################################
groups = [
    Group("web", matches=[Match(title=["Firefox"])]),
    Group("Terminal"),
    Group("web", matches=[Match(title=["Firefox"])]),
   ]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Selected layouts                                    ###
###                                                                                         ###
###############################################################################################
###############################################################################################
layouts = [
    layout.Stack(
        border_normal=selectedTheme["borderNormal"],
        border_focus=selectedTheme["borderFocus"],
        border_width=3,
        margin=10,
        #
        num_stacks=2,
    ),
    layout.MonadTall(
        border_normal=selectedTheme["borderNormal"],
        border_focus=selectedTheme["borderFocus"],
        border_width=3,
        margin=10,
        #
    ),
    layout.Columns(
        border_normal=selectedTheme["borderNormal"], 
        border_focus=selectedTheme["borderFocus"], 
        border_width=3, 
        margin=10,
        #
        border_normal_stack="#000000", 
        border_focus_stack="#6699FF", 
        border_on_single=2,
        margin_on_single=10,
    ),
    layout.VerticalTile(
        border_normal=selectedTheme["borderNormal"],
        border_focus=selectedTheme["borderFocus"],
        border_width=3, 
        margin=10,
        #
        border_on_single=2,  
        margin_on_single=10,
    ),
    layout.Max(
        border_normal=selectedTheme["borderNormal"],
        border_focus=selectedTheme["borderFocus"],
        border_width=3,
        margin=10,
        #
    ),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.Zoomy(),
]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Widget defaults                                     ###
###                                                                                         ###
###############################################################################################
###############################################################################################
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Widget definitions                                  ###
###                                                                                         ###
###############################################################################################
###############################################################################################
imgList = os.listdir("/home/kitten/.config/qtile/Wallpapers/JPG")
random_num = random.choice(imgList)
path = "/home/kitten/.config/qtile/Wallpapers/JPG/" + random_num
screens = [
    # Main Laptop Screen
    Screen(wallpaper=path, wallpaper_mode='fill', top=bar.Bar
        (
            [
                widget.CurrentLayout(background="#000000", foreground="#FFFFFF", custom_icon_paths=["/home/kitten/.config/qtile/layout-icons/gruvbox-neutral_orange"]),
                widget.GroupBox(highlight_method="line", active="#33CC33", borderwidth=2),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                widget.Volume(fmt='Vol: {}'),
                widget.NetGraph(),
                widget.KhalCalendar(foreground="#9966FF"),
                widget.Clock(foreground="7733ff", format="%Y-%m-%d %a %I:%M %p"),
                widget.Battery(foreground="#5500FF", format="{percent:2.0%}", low_percentage=30.0, charge_char="***"),
            ],  30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
    # Left Dell Monitor HTML
    Screen(wallpaper=path, wallpaper_mode='fill', top=bar.Bar
        (
            [
                widget.CurrentLayout(background="#000000", foreground="#FFFFFF"),
                widget.GroupBox(highlight_method="line", active="#33CC33", borderwidth=2),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.KhalCalendar(foreground="#9966FF"),
                widget.Clock(foreground="7733ff", format="%Y-%m-%d %a %I:%M %p"),
                widget.Battery(foreground="#5500FF", format="{percent:2.0%}", low_percentage=30.0, charge_char="***"),
            ],  30,
        ),
    ),
    # Right Dell Monitor C-Type<->HTML
    Screen(wallpaper=path, wallpaper_mode='fill', top=bar.Bar
        (
            [
                widget.CurrentLayout(background="#000000", foreground="#FFFFFF"),
                widget.GroupBox(highlight_method="line", active="#33CC33", borderwidth=2),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(chords_colors={"launch": ("#ff0000", "#ffffff"),},name_transform=lambda name: name.upper(),),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.KhalCalendar(foreground="#9966FF"),
                widget.Clock(foreground="#7733FF", format="%a %I:%M %p"),
                widget.Battery(foreground="#5500FF", format="{percent:2.0%}", low_percentage=30.0, charge_char="***"),
            ],  30,
        ),
    ),
]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Special mouse actions                               ###
###                                                                                         ###
###############################################################################################
###############################################################################################
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Miscellaneous settings                              ###
###                                                                                         ###
###############################################################################################
###############################################################################################
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Floating window rules                               ###
###                                                                                         ###
###############################################################################################
###############################################################################################
floating_layout = layout.Floating(
    border_focus="#FFFF00",
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
###############################################################################################
###############################################################################################
###                                                                                         ###
###                                     Window Manager name                                 ###
###                                                                                         ###
###############################################################################################
###############################################################################################
wmname = "LG3D"
