#!/bin/bash

# カレントディレクトリに移動
echo $0
cd `dirname $0`

rm -f ~/.hyper.js ~/.vim/vimrc ~/.vim/gvimrc ~/.config/nvim/init.vim

# 絶対パスで指定した方がいい
sudo ln -s ~/ff-github/.hyper.js ~/.hyper.js
sudo ln -s ~/ff-github/vimrc ~/.vim/vimrc
sudo ln -s ~/ff-github/gvimrc ~/.vim/gvimrc
sudo ln -s ~/ff-github/init.vim ~/.config/nvim/init.vim
