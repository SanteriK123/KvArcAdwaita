#!/usr/bin/env python3
import os
import subprocess

# 1. Map GNOME accent names to their standard libadwaita hex colors
ACCENTS = {
    "blue": "#3584e4",
    "teal": "#2190a4",
    "green": "#3a944a",
    "yellow": "#c88800",
    "orange": "#ed5b00",
    "red": "#e62d42",
    "pink": "#d56199",
    "purple": "#9141ac",
    "slate": "#6f8396",
}

# 2. Set your theme folder name and the base hex color your theme currently uses
THEME_NAME = "KvArcAdwaita"
THEME_DIR = os.path.expanduser(f"~/.config/Kvantum/{THEME_NAME}")
STATE_FILE = os.path.join(THEME_DIR, ".last_accent")
FALLBACK_OLD_HEX = "#3584e4"

# 3. Get the active GNOME accent color
try:
    gnome_color = subprocess.check_output(
        ["gsettings", "get", "org.gnome.desktop.interface", "accent-color"],
        text=True
    ).strip().strip("'")
except Exception:
    gnome_color = "blue"

new_hex = ACCENTS.get(gnome_color, "#3584e4")

# 4. Determine what color we are replacing
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r") as f:
        old_hex = f.read().strip()
else:
    old_hex = FALLBACK_OLD_HEX

if old_hex.lower() == new_hex.lower():
    print(f"Theme is already using {gnome_color} ({new_hex}).")
    exit(0)

# 5. Perform the in-place replacement on .kvconfig and .svg
for filename in [f"{THEME_NAME}.kvconfig", f"{THEME_NAME}.svg"]:
    filepath = os.path.join(THEME_DIR, filename)
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Case-insensitive replace for hex strings
    content = content.replace(old_hex.lower(), new_hex.lower())
    content = content.replace(old_hex.upper(), new_hex.upper())

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# 6. Save current accent so the next run knows what to replace
with open(STATE_FILE, "w") as f:
    f.write(new_hex)

print(f"Updated {THEME_NAME}: {old_hex} -> {new_hex} ({gnome_color})")
