# MyAwesomeConfig

## Configuration
### Remove Tasklist Widget - Comment it to remove it
```
-- Create a tasklist widget
s.mytasklist = awful.widget.tasklist {
    screen  = s,
    filter  = awful.widget.tasklist.filter.currenttags,
    buttons = tasklist_buttons
}
```
### The default rc.lua file.
A copy of this file is usually installed in /etc/xdg/awesome/rc.lua
### Replace default rc.lua file to current rc.lua file
```
cp /etc/xdg/awesome/rc.lua .config/awesome
```
### Restart AwesomeWM
```
Mod4 + Control + r
```
### Remove Title Bar
Change true to false
```
properties = { titlebars_enabled = false
```
### Remove floating windows - comment "awful.layout.suit.floating"
```
-- Table of layouts to cover with awful.layout.inc, order matters.
awful.layout.layouts = {
    ..
    --awful.layout.suit.floating,
    ..
}
-- }}}
```

## Keybinding
| Title  | Keybinding |
| ------------- | ------------- |
| ... | ... |

## Arc Icon Theme
For the [icons](https://github.com/horst3180/arc-icon-theme), then follow the installation instructions.

## Awesome WM Widgets
If you want any cool [widgets](https://github.com/streetturtle/awesome-wm-widgets) for your Awesome WM.

## ERRORs
### module 'awesome-wm-widgets.battery-widget.battery' not found
Follow the installation process [here](https://github.com/streetturtle/awesome-wm-widgets#installation)
### Battery Widget - Folder with icons doesn't exist: /usr/share/icons/Arc/status/symbolic
Follow the installation process [here](https://github.com/horst3180/arc-icon-theme#installation)
