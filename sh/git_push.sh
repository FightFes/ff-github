#!/bin/bash

# 実行時に指定された引数の数が３つでなければ終了
if [ $# -ne 3 ]; then
  exit 1
fi

# カレントディレクトリに移動
echo $0
cd `dirname $0`

# 処理
