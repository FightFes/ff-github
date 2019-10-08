#!/bin/bash

# カレントディレクトリに移動
echo $0
cd `dirname $0`

LINK_SOURCE_PATH_LIST=(~/ff-github/vim/vimrc
                       ~/ff-github/vim/init.vim)
LINK_DEST_PATH_LIST=(~/.vim/vimrc 
                     ~/.config/nvim/init.vim) 

for i in ${!LINK_SOURCE_PATH_LIST[@]}
do
  #ないならディレクトリ作成
  mkdir -p -v $(dirname ${LINK_DEST_PATH_LIST[i]})
  #今あるファイルを削除
  rm -f ${LINK_DEST_PATH_LIST[i]}
  #シンボリックリンクを貼る
  sudo ln -s ${LINK_SOURCE_PATH_LIST[i]} ${LINK_DEST_PATH_LIST[i]}
done

# -fでファイルのみ、-dでディレクトリのみ、-eで両方
# if [ ! -e ~/.vim ]
# fi

# rm -f ~/.vim/vimrc ~/.vim/gvimrc ~/.config/nvim/init.vim

# 絶対パスで指定した方がいい
# sudo ln -s ~/ff-github/vimrc ~/.vim/vimrc
# sudo ln -s ~/ff-github/gvimrc ~/.vim/gvimrc
# sudo ln -s ~/ff-github/init.vim ~/.config/nvim/init.vim
