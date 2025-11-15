# Add these lines ot ~/.bash_aliases and restart the terminal.

gc () {
    git commit -m "$@";
}

ga () {
    git add $@; 
}

gd () {
    git diff $@; 
}

gb () {
    git branch $@; 
}

gch () {
    git checkout $@; 
}

