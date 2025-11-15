# Add this function to the ~/.bash_aliases
# Start new terminal.
# Use as a 'vact' command.
vact () {
    venv_dir="${PWD}/.venv"
    if [ -d "$venv_dir" ]; then
       source "$venv_dir/bin/activate"
       echo "The virtual enviroment '$venv_dir' is activated." 
    else
       echo "No .venv found!" 
    fi
}

