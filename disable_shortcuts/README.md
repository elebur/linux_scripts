The script is taken from [this](https://askubuntu.com/a/863486/1625294) SO answer.

In order it to work you you have to user Xorg. Ubuntu uses Wayland since the version 22.04 (?). To disable Wayland do the following ([source](https://askubuntu.com/questions/1428525/how-to-permanetely-disable-wayland)):
1. `sudo vim /etc/gdm3/custom.conf`
2. Uncoment the line `WaylandEnable=false`
3. press `:qw` and enter.
4. Reboot the system.
