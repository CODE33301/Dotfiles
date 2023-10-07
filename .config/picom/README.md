# MyPicomConfig
## Installation
```
yay -S picom-git
```

## Config
```
mkdir .config/picom
```
### Manually enable default compositing effects during a session.
```
picom &
```
### Run Picom
```
exec picom -b &
```
### Find a window’s class name.
* Run xprop from the command line and click on the target window.
* Search the xprop output for the WM_CLASS(STRING) property, which will show the window class name.
```
...
WM_CLASS(STRING) = "st-256color", "st-256color"
...
```
