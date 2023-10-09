#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
from __future__ import annotations


class GlobalVerbose:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def __bool__(self):
        if self.enabled:
            return True
        return False

    def __repr__(self):
        return f"<GlobalVerbose enabled={self.enabled}>"

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True


gv = GlobalVerbose()
gvd = GlobalVerbose()  # gvd "global verbose debug"
