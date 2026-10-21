# KvArcAdwaita
A Kvantum theme that somewhat aligns with libadwaita theming, intended for GNOME users.
This is simply a recolored version of the KvArcDark theme found by default in a Kvantum install, so all credits to the original project.
The colors were handpicked from Nautilus, and then I manually replaced what made sense in the .kvconfig file and the SVG.

## Installation
Clone the repo to ~/.config/Kvantum, set the theme in Kvantum and then use for example qt6ct to use the Kvantum theme.

## Update accent script
The repo includes a small python script `update-accent.py` that just replaces all instances of the accent color in the .svg file.
It is pure slop, but it works fine for my use case. It keeps track of the previous accent color in a file, and then replaces all instances of that with a new one.
Some template implementation would most likely be smarter but this should be ok.  
  
If you'd prefer not to use an AI script, a simple sed command to globally replace the previous hex color with the new one should be more than sufficient.
```bash
sed -i 's/oldhex/newhex/g' KvArcAdwaita.kvconfig KvArcAdwaita.svg
```

## Credits

[Kvantum](https://github.com/tsujan/Kvantum) for the KvArc theme.
