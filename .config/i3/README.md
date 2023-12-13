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
| Split In Vertical Orientation | $mod+ctrl+4 |
| Split In Horizontal Orientation | $mod+ctrl+5 |
| Layout Stacking | $mod+ctrl+1 |
| Layout Tabbed | $mod+ctrl+2 |
| Layout Toggle Split | $mod+ctrl+3 |
| ... | ... |

## Packages
### dmenu
```
sudo pacman -Syu dmenu
```
### rofi
```
sudo pacman -Syu rofi
```
### Picom
```
sudo pacman -Syu picom-git
```
## Picom
### Start Manually
```
picom --config /dev/null
```
### By default it reads config ~/.config/picom.conf
### Kill Picom
```
pkill picom
```
## ERRORs
### Error: status_command not found or is missing a library dependency
```
sudo pacman -Syu i3status
```
