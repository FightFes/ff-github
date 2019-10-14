#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

#------------------------------------------------------------------------------
# 削除
#------------------------------------------------------------------------------
def remove(path):
    print 'remove ' + os.path.relpath(path)
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)

#------------------------------------------------------------------------------
# コピー
#------------------------------------------------------------------------------
def copy(origin, target):
    print 'copy %s %s' % (origin, target)
    if os.path.isdir(origin):
        shutil.copytree(origin, target)
    else:
        shutil.cp(origin, target)

#------------------------------------------------------------------------------
# 移動
#------------------------------------------------------------------------------
def move(origin, target):
    print 'move %s %s' % (origin, target)
    shutil.move(origin, target)

#------------------------------------------------------------------------------
# フォルダ作成
#------------------------------------------------------------------------------
def make_dir(path):
    print 'make dir ' + os.path.relpath(path)
    os.makedirs(path)

#------------------------------------------------------------------------------
# ファイル読み込み
#------------------------------------------------------------------------------
def read_file(path):
    print 'read file ' + os.path.relpath(path)
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content

#------------------------------------------------------------------------------
# ファイル書き込み
#------------------------------------------------------------------------------
def write_file(path, content):
    print 'write file ' + os.path.relpath(path)
    file = open(path, 'w')
    file.write(content)
    file.close()

