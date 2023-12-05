autoload -Uz compinit
compinit

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
else
  source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
  source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
  
  source ~/emsdk/emsdk_env.sh &> /dev/null
  
  source /opt/homebrew/opt/chruby/share/chruby/chruby.sh
  source /opt/homebrew/opt/chruby/share/chruby/auto.sh
  chruby ruby-3.1.3 # run chruby to see actual version

  alias cd='z'
fi

eval "$(thefuck --alias)"
eval "$(starship init zsh)"
eval "$(zoxide init zsh)"

export PATH="$HOME/go/bin:$PATH"

alias vim='nvim'
alias ls='eza -TL=1 --icons'
alias ls2='eza -TL=2 --icons'

clear
~/.dotfiles/colorscripts/colorscript.sh --random
echo 'Greetings master!'
