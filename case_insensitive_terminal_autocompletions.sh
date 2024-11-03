# source - https://askubuntu.com/a/87066/1625294
# run this code line by line in the terminal and then start new terminal.
# if you want to remove case-insensitivity just remove
# the 'set completion-ignore-case On' line from the ~/.inputrc file,
# or remove the whole file.

# If ~/.inputrc doesn't exist yet: First include the original /etc/inputrc
# so it won't get overriden
if [ ! -a ~/.inputrc ]; then echo '$include /etc/inputrc' > ~/.inputrc; fi

# Add shell-option to ~/.inputrc to enable case-insensitive tab completion
echo 'set completion-ignore-case On' >> ~/.inputrc
