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
def command(cmd, exe_dir=''):
    if isinstance(cmd, str):
        run_cmd = cmd.split()
    elif isinstance(cmd, list):
        cmd[0] = normpath(cmd[0])
        print cmd[0]
        run_cmd = cmd

    if exe_dir != '':
        cwd = os.getcwd()
        cd(exe_dir)
        subprocess.call(run_cmd)
        cd(cwd)
    else:
        subprocess.call(run_cmd)
