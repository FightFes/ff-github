#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

# カレントディレクトリに移動
# cd `dirname $0` と同じ
# コマンドの実行結果を取得できる
cd $SCRIPT_DIR

function MakeLink() {
  #ないならディレクトリ作成
  mkdir -p -v $(dirname $2)
  #今あるファイルを削除
  rm -f -r $2
  #シンボリックリンクを貼る
  sudo ln -s $1 $2
}

MakeLink $SCRIPT_DIR/nvim ~/.config/nvim
