
# Install Brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install wget
brew install youtube-dl

# Git
brew install git

# Notion
brew install --cask notion

# NodeJs
brew install node@16

# Discord
brew install --cask discord

# Deluge
brew install --cask deluge

# Chrome
brew install --cask google-chrome

# Docker
brew install docker

# Yarn
brew install yarn

# Python
brew install python@3.7

# Obsidian
brew install --cask obsidian

# iterm2
brew install --cask iterm2

# JDownloader
brew install --cask jdownloader

# Tmux
brew install tmux

# Vscode
brew install --cask visual-studio-code

# Cakebrew
brew install --cask cakebrew

# Lastpass
brew install --cask lastpass
brew install lastpass-cli

# rectangle
brew install --cask rectangle

# homyzsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# powerlevel10k
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
