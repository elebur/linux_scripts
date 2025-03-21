# Custom Bash Prompt
# StackOverflow reference: https://stackoverflow.com/a/35218509/3684641
# Customisation rules: https://help.ubuntu.com/community/CustomizingBashPrompt
# Original script: https://gist.github.com/rmharrison/1885ef6bbb0226eb7b42e2135d5eeca2#file-custombashprompt-sh

# Installing:
# Add lines below to the bottom of the ~/.bashrc file and relaunch the terminal.
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\[\033[32m\]\u@\h:\[\033[34m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\]$ "
