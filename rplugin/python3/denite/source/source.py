# ============================================================================
# FILE: source.py
# AUTHOR: 年糕小豆汤 <ooiss@qq.com>
# License: MIT license
# ============================================================================

import sqlite3
from denite import util
from .base import Base
from ..kind.base import Base as BaseKind

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'source'
        self.kind = Kind(vim)

    def gather_candidates(self, context):
        sources = self.vim.call('source#get_source_list')
        candidata = []
        for source in sources:
            candidata.append({
                'word': source,
                })
        return candidata

class Kind(BaseKind):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'source'
        self.default_action = 'trigger'

    def action_trigger(self, context):
        target = context['targets'][0]
        source = target['word']
        context['sources_queue'].append([
            {'name': source, 'args': []},
            ])

    def action_args(self, context):
        target = context['targets'][0]
        source = target['word']
        args = util.input(self.vim, context, 'Enter args: ')
        args = args.split(':')
        context['sources_queue'].append([
            {'name': source, 'args': args},
            ])

