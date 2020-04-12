#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

#------------------------------------------------------------------------------
# フォルダ作成
#------------------------------------------------------------------------------
def make_dir(path):
    if os.path.isdir(path):
        print 'already exists directory'
    else:
        print 'make dir ' + path
        os.makedirs(path)

#------------------------------------------------------------------------------
# コピー
#------------------------------------------------------------------------------
def copy(origin, target):
    origin = os.path.normpath(origin)
    target = os.path.normpath(target)
    print 'copy %s %s' % (origin, target)
    if os.path.exists(origin):
        if os.path.isdir(origin):
            shutil.copytree(origin, target)
        else:
            shutil.copy(origin, target)
    else:
        print 'Not exists ' + origin

#------------------------------------------------------------------------------
# 移動
#------------------------------------------------------------------------------
def move(origin, target):
    print 'move %s %s' % (origin, target)
    shutil.move(origin, target)

#------------------------------------------------------------------------------
# 削除
#------------------------------------------------------------------------------
def remove(path):
    path = os.path.normpath(path)
    print 'remove ' + path
    if os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    else:
        print 'Not exists ' + path

#------------------------------------------------------------------------------
# ファイル書き込み
#------------------------------------------------------------------------------
def write_file(path, content):
    print 'write file ' + path
    file = open(path, 'w')
    file.write(content)
    file.close()

#------------------------------------------------------------------------------
# ファイル読み込み
#------------------------------------------------------------------------------
def read_file(path):
    print 'read file ' + path
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content
