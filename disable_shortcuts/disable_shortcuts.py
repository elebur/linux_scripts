#!/usr/bin/env python3
import subprocess
import time
import os
import datetime


# Path pattern to block
apppattern = "pycharm"

# Write a backup that can restore the settings at the
# start of the script.
# Leave empty to not write a backup.
backupfile = "~/.keymap_backup"

# Add the keys to be disabled below.
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
    "org.gnome.desktop.wm.keybindings/toggle-shaded" : "gsettings",
    # CTRL + ALT + LEFT
    "org.gnome.desktop.wm.keybindings/switch-to-workspace-left": "gsettings",
    # CTRL + ALT + RIGHT
    "org.gnome.desktop.wm.keybindings/switch-to-workspace-right": "gsettings",
    # CTRL + SHIFT + ALT + RIGHT
    "org.gnome.desktop.wm.keybindings/move-to-workspace-right":  "gsettings",
    # CTRL + SHIFT + ALT + LEFT
    "org.gnome.desktop.wm.keybindings/move-to-workspace-left":  "gsettings",
}

#
# Helper functions
#

# Run a command on the shell
def run(cmd):
    subprocess.Popen(cmd)

# Run a command on the shell and return the
# stripped result
def get(cmd):
    try:
        return subprocess.check_output(cmd).decode("utf-8").strip()
    except:
        pass

# Get the PID of the currently active window
def getactive():
    xdoid = get(["xdotool", "getactivewindow"])
    result = get(["xprop", "-id", xdoid])
    if not result:
        return None

    pidline = [l for l in result.splitlines() if "_NET_WM_PID(CARDINAL)" in l]
    if pidline:
        pid = pidline[0].split("=")[1].strip()
    else:
        # Something went wrong
        print("Warning: Could not obtain PID of current window")
        pid = ""

    return pid

def readkey(key):
    if shortcuts[key] == "gsettings":
        return get(["gsettings", "get"] + key.split("/"))
    elif shortcuts[key] == "dconf":
        return get(["dconf", "read", key])

def writekey(key, val):
    if val == "": 
        val = "['']"
    if shortcuts[key] == "gsettings":        
        run(["gsettings", "set"] + key.split("/") + [val])
    elif shortcuts[key] == "dconf":
        run(["dconf", "write", key, val])

def resetkey(key):
    if shortcuts[key] == "gsettings":
        run(["gsettings", "reset"] + key.split("/"))
    elif shortcuts[key] == "dconf":
        run(["dconf", "reset", key])

# If val == True, disables all shortcuts.
# If val == False, resets all shortcuts.
def setkeys(flag):
    for key, val in shortcutmap.items():
        if flag == True:
            # Read current value again; user may change
            # settings, after all!
            shortcutmap[key] = readkey(key)
            writekey(key, "")            
        elif flag == False:
            if val:
                writekey(key, val)
            else:
                resetkey(key)

#
# Main script
#

# Store current shortcuts in case they are non-default
# Note: if the default is set, dconf returns an empty string!
# Optionally, create a backup script to restore the value in case
# this script crashes at an inopportune time.
shortcutmap = {}
if backupfile:
    f = open(os.path.expanduser(backupfile),'a+') 
    f.write('#!/bin/sh\n')
    f.write(f"#{datetime.datetime.now()}\n")

for key, val in shortcuts.items():
    if shortcuts[key] == "gsettings":
        shortcutmap[key] = get(["gsettings", "get"] + key.split("/"))

        if backupfile:
            if shortcutmap[key]:
                f.write(f"gsettings set {" ".join(key.split("/"))} \"{shortcutmap[key]}\"\n")
                # f.write("gsettings set " + " ".join(key.split("/")) + " " + 
                # shortcutmap[key] + "\n")
            else:
                f.write("gsettings reset " + " ".join(key.split("/")) + "\n")
    elif shortcuts[key] == "dconf":
        shortcutmap[key] = get(["dconf", "read", key])

        if backupfile:
            if shortcutmap[key]:
                f.write("dconf write " + key + " " + shortcutmap[key] + "\n")
            else:
                f.write("dconf reset " + key + "\n")

if backupfile: 
    f.write("\n\n")
    f.close()

# Check every half second if the window changed form or to a 
# matching application.
front1 = None
while True:
    time.sleep(0.5)
    checkpids = get(["pgrep", "-f", apppattern])

    if checkpids:
        checkpids = checkpids.splitlines()
        activepid = getactive()
        if activepid is None:
            continue
        #print(activepid)

        if activepid:
            front2 = True if activepid in checkpids else False
        else:
            front2 = False
    else:
        front2 = False

    if front2 != front1:
        #print("Matches: " + str(flag))
        if front2:
            setkeys(True)
        else:
            setkeys(False)
    front1 = front2
