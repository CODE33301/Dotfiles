# Myi3WMConfig
## Keybinding
| Title  | Keybinding |
| ------------- | ------------- |
| Close Window  | $mode+w  |
| Open Terminal  | $mod+Return  |
| Switch Desktop/Workstation | $mode+1,2,3,4,5,6,7,8,9 |
| Reload The Configuration File | $mod+Shift+c |
| Exit i3 | $mod+Shift+q |
| Restart i3 Inplace | $mod+r |

## Packages
### dmenu
```
sudo pacman -Syu dmenu
```
### rofi
```
sudo pacman -Syu rofi
```

## ERRORs
### Error: status_command not found or is missing a library dependency
```
sudo pacman -Syu i3status
```
