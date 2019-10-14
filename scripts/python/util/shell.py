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
def command(cmd):

    if isinstance(cmd, str):
        run_cmd = cmd.split()
    elif isinstance(cmd, list):
        cmd[0] = normpath(cmd[0])
        print cmd[0]
        run_cmd = cmd

    subprocess.call(run_cmd)

#------------------------------------------------------------------------------
# command_with_cd
#------------------------------------------------------------------------------
def command_with_cd(cmd, exe_dir):
    cwd = os.getcwd()
    cd(exe_dir)
    command(cmd)
    cd(cwd)
