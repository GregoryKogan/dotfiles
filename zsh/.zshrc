autoload -Uz compinit
compinit

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
else
  source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
  source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
  source ~/emsdk/emsdk_env.sh &> /dev/null
  alias cd='z'
fi

eval "$(thefuck --alias)"
eval "$(starship init zsh)"
eval "$(zoxide init zsh)"

export PATH="$HOME/go/bin:$PATH"

alias vim='nvim'
alias ls='exa -TL=1 --icons'
alias ls2='exa -TL=2 --icons'

clear
~/.dotfiles/colorscripts/colorscript.sh --random
echo 'Greetings master!'
