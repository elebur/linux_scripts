# Add these lines to the end of the ~/.bash_aliases.
# Start the new terminal.
# Use as 'german_add' and 'german_remove' commands.

# Command for plain terminal usage (without escaping double quotes):
# gsettings set org.gnome.desktop.input-sources sources "[('xkb', 'us'), ('xkb', 'de')]"
alias german_add="gsettings set org.gnome.desktop.input-sources sources \"[('xkb', 'us'), ('xkb', 'de')]\""
alias german_remove="gsettings set org.gnome.desktop.input-sources sources \"[('xkb', 'us')]\""
