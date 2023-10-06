   ##################################################################
  ##########################################################################3
 ###
###                   By CODE33301 GITHUB                        
####
####################################################################
  ########################################################

# Purple Colors Main:#A020F0
colors_array=("#1F0330" "#3D075F" "#5C0A8F" "#7B0DBF" "#9911EE" "#AE40F2" "#C270F5" "#D6A0F8" "#EBCFFC" "#FFFFFF")
# Change Background Color Terminal
echo -ne "\033]11;"${colors_array[RANDOM%"${#colors_array[@]}"]}"\007"

# Run Picom
picom -b &

# set Wallpaper
feh --bg-scale /home/$USER/.config/Wallpapers/JPG/_DSC6639.jpg
