# ============================================================================
# FILE: bookmark/add/file.py
# AUTHOR: <kinntai at gmail.com>
# License: MIT license
# ============================================================================

import os
import json
from denite.kind.file import Kind as File

class Kind(File):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'bookmark/add/file'
        self.default_action = 'add'

    def action_add(self, context):
        _add_bookmark(self.vim, context['targets'][0])


def _add_bookmark(vim, target):
    default_group_name = vim.call('bookmark#get_default_group')
    group = str(vim.call('denite#util#input',
                         'Group name [' + default_group_name + ']: ',
                         '',
                         ''))
    name = str(vim.call('denite#util#input',
                        'Bookmark name: ',
                        '',
                        ''))

    if not group or group == '': group = default_group_name

    path = target['action__path']

    try:
        bookmark_dict = _read(vim)
    except FileNotFoundError:
        bookmark_dict = {}

    group_dict = bookmark_dict.setdefault(group, {
        "bookmarks": [],
    })

    group_dict['bookmarks'].append({
        'name': name,
        'path': path,
    })

    _write(vim, bookmark_dict)

def _read(vim):
    with open(vim.call('bookmark#get_cache_file_path')) as f:
        return json.loads(f.read())

def _write(vim, bookmark_dict):
    dir_path = vim.call('bookmark#get_cache_directory_path')
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)

    with open(vim.call('bookmark#get_cache_file_path'), 'w') as f:
        json.dump(bookmark_dict, f, ensure_ascii=False, indent=2)
