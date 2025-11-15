# Disable shortcuts
Disables system shortcuts while the focus is in a certain application.

See the inner [README](https://github.com/elebur/linux_scripts/blob/main/disable_shortcuts/README.md) for details.

# show_git_branch_in_bash
Adds a current git branch at the end of the prompt.

Installation instructions are in the script.

<img width="600" height="69" alt="example" src="https://github.com/user-attachments/assets/75b257c5-65ba-48e1-a277-6cc1304f9d15" />

# case_insensitive_terminal_autocompletions
Makes Bash's autocompletions case-insensitive (e.g. 'desktop' == 'Desktop').

Installation instructions are in the script.

# process_finder
Looks for the process by its name (currently it is hardcoded to 'python') and shows paths for each process.

Requires 'psutil' in order to work (`pip install psutil`)

Command to launch the script - `sudo `which python` process_finder.py`. 

Doing ``which python`` instead of just `python` to prevent `sudo: python: command not found` error.
