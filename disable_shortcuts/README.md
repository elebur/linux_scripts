The script is taken from [this](https://askubuntu.com/a/863486/1625294) SO answer (this answer based on the other one above. The original one has instructions on how to run the script and how to handle multiple applications in the the script).

In order it to work you you have to user Xorg. Ubuntu uses Wayland since the version 22.04 (?). To disable Wayland do the following ([source](https://askubuntu.com/questions/1428525/how-to-permanetely-disable-wayland)):
1. `sudo vim /etc/gdm3/custom.conf`
2. Uncoment the line `WaylandEnable=false`
3. press `:qw` and enter.
4. Reboot the system.

## How to use
1. The script needs xdotool:
`sudo apt-get install xdotool`
2. Copy the script into an empty file, save it as disable_shortcuts.py
3. In the head of the script, replace in the line: `app = "gedit"` "gedit" by your application, meaning: the process name that owns the window.
4. Test-run the script by the command:
`python3 /path/to/disable_shortcuts.py`
5. If all works fine, add it to Startup Applications: Dash > Startup Applications > Add. Add the command: `/bin/bash -c "sleep 15 && python3 /path/to/disable_shortcuts.py"`

# shortcuts
```python
# source - https://gist.github.com/akerbos/5c9ff3ff5750ded36361d0323ac55fe6
# cf. http://askubuntu.com/a/863486/69674

# Places to look for shortcuts in dconf-editor:
# - org.compiz.integrated
# - org.freedesktop.ibus.general.hotkey (?)
# - org.gnome.settings-daemon.plugins.media-keys
# - org.gnome.desktop.wm.keybindings
# - org.gnome.metacity.keybindings
shortcuts = {
    # CTRL + ALT + Backspace
    "org.gnome.settings-daemon.plugins.media-keys/logout" : "gsettings",
    # CTRL + ALT + L
    "org.gnome.settings-daemon.plugins.media-keys/screensaver" : "gsettings",
    # CTRL + ALT + T
    "org.gnome.settings-daemon.plugins.media-keys/terminal" : "gsettings", 
    # ALT + F6
    "org.gnome.desktop.wm.keybindings/cycle-group" : "gsettings",
    # ALT + F7
    "org.gnome.desktop.wm.keybindings/begin-move" : "gsettings",
    # ALT + F8
    "org.gnome.desktop.wm.keybindings/begin-resize" : "gsettings",  
    # CTRL + ALT + S
    "org.gnome.desktop.wm.keybindings/toggle-shaded" : "gsettings"
}
```

## An example to add (disabling) the log out shortcut:

1. Open a terminal window, run the command `dconf watch /`
2. Open System Settings > "Keyboard" > "Shortcuts" > "System"
3. Re-set the shortcut to itself. In the terminal, you can see the `gsettings` key that belongs to the shortcut:

 [![enter image description here][1]][1]

4. Now we have to add the found key (in a slightly different appearance):

        ["org.gnome.settings-daemon.plugins.media-keys/logout": "gsettings"]

 ...to the "keys" list in our function:

```python
# Add the keys to be disabled below.
shortcuts = {
    # CTRL + ALT + Backspace
    "org.gnome.settings-daemon.plugins.media-keys/logout" : "gsettings",
    # CTRL + ALT + L
    "org.gnome.settings-daemon.plugins.media-keys/screensaver" : "gsettings",
}
```
  [1]: https://i.sstatic.net/4xzn4.png
