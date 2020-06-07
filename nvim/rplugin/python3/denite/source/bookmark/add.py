# ============================================================================
# FILE: add.py
# AUTHOR: <kinntai at gmail.com>
# License: MIT license
# ============================================================================

import os
from denite.source.file import Source as File

class Source(File):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'bookmark/add'

    def gather_candidates(self, context):
        candidates = super().gather_candidates(context)

        if not candidates: return candidates

        for c in candidates: 
            c['kind'] = 'bookmark/add/directory' if os.path.isdir(c['action__path']) else 'bookmark/add/file'

        return candidates

