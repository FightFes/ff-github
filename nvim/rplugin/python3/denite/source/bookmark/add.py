# add.py
"""
denite.nvim source: add
"""

import os
import json
from denite.source.file import Source as SourceFile
from denite.kind.file import Kind as File
from denite.kind.directory import Kind as Directory

class Source(SourceFile):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'bookmark/add'

    def gather_candidates(self, context):
        candidates = super().gather_candidates(context)

        if not candidates: return candidates

        for c in candidates: 
            c['kind'] = KindDirectory(self.vim) if os.path.isdir(c['action__path']) else KindFile(self.vim)

        return candidates

class KindDirectory(Directory):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'directory'
        self.default_action = 'narrow'

    def action_narrow(self, context):
        target = context['targets'][0]
        context['sources_queue'].append([
            {'name': 'bookmark/add', 'args': []},
        ])
        context['path'] = target['action__path']

    def action_add(self, context):
        _add_bookmark(self.vim, context['targets'][0])


class KindFile(File):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'file'
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
