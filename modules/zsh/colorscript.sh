name=$(ls -1 ~/.colorscripts/colorscripts/ | sort -R | head -1)
path="~/.colorscripts/colorscripts/"$name
exec $path