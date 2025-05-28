#!/usr/bin/env python3
# -*- coding: utf8 -*-
# tab-width:4

# pylint: disable=missing-docstring               # [C0111] docstrings are always outdated and wrong
from __future__ import annotations


class GlobalVerbose:
    _instance: GlobalVerbose | None = None

    def __new__(cls) -> GlobalVerbose:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.enabled = False
        return cls._instance

    def __bool__(self) -> bool:
        return self.enabled

    def __repr__(self) -> str:
        return f"<GlobalVerbose enabled={self.enabled}>"

    def disable(self) -> None:
        self.enabled = False

    def enable(self) -> None:
        self.enabled = True


gvd = GlobalVerbose()  # Global verbose debug singleton
