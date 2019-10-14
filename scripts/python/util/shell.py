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
    print cmd

    if isinstance(cmd, str):
        run_cmd = cmd
    elif isinstance(cmd, list):
        run_cmd = cmd.split()

    return subprocess.call(cmd.split())
