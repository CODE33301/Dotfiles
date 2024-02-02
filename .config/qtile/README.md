# MyQTileWMConfig
This is my QTile Config files. You are very welcome to copy &amp; paste, download &amp; edit, and use this as an example to help you improve your qtile config.
## Installation
### Rofi
```
sudo pacman -Syu Rofi
```
### qtile
```
sudo pacman -Syu qtile
```
### Python Xlib library
For randr and display.
```
sudo pacman -S python-xlib
```



## Configuration
Create qtile folder and then download my config.py
```
mkdir -p ~/.config/qtile/
```



## Errors
### Import Error: KhalCalendar
```
sudo pacman -Syu python-dateutil
```
### Import Error: Bluetooth
```
sudo pacman -Syu python-dbus-next
```
### Import Error: Wlan
```
sudo pacman -Syu python-iwlib
```
### Import Error: PulseVolume
```
sudo yay -S python-pulsectl-asyncio
```
