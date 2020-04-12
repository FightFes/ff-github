#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

#------------------------------------------------------------------------------
# cd
#------------------------------------------------------------------------------
def cd(path):
    print 'cd ' + os.path.relpath(path)
    os.chdir(path)

#------------------------------------------------------------------------------
# command
#------------------------------------------------------------------------------
def command(cmd, exe_dir='', shell_flag=True):
    if isinstance(cmd, str):
        if shell_flag:
            run_cmd = cmd
        else:
            run_cmd = cmd.split()
    elif isinstance(cmd, list):
        if shell_flag:
            run_cmd = ' '.join(cmd)
        else:
            run_cmd = cmd

    if exe_dir != '':
        exe_dir = os.path.normpath(exe_dir)
        if sys.platform == 'win32':
            # Winの日本語パス対策
            exe_dir = unicode(exe_dir, 'utf8').encode('cp932')
        cwd = os.getcwd()
        cd(exe_dir)
        print run_cmd
        subprocess.call(run_cmd, shell=shell_flag)
        cd(cwd)
    else:
        print run_cmd
        subprocess.call(run_cmd, shell=shell_flag)

