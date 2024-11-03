The script is taken from [this](https://askubuntu.com/a/863486/1625294) SO answer.

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

