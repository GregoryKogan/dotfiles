autoload -Uz compinit
compinit
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh

eval "$(thefuck --alias)"
eval "$(starship init zsh)"
eval "$(zoxide init zsh)"

export PATH="$HOME/go/bin:$PATH"

alias vim='nvim'
alias nano='/opt/homebrew/bin/nano'
alias ls='exa -TL=1 --icons'
alias ls2='exa -TL=2 --icons'
alias cd='z'

clear
~/.dotfiles/colorscripts/colorscript.sh --random
echo 'Greetings master!'
