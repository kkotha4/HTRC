#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:19:56 2019

@author: kashish
"""

if __debug__:
    # This code will execute when running `python script.py`
    import htrc.mock.volumes as volumes
else:
    # This code will execute when running `python -O script.py`
    # The -O argument turns on optimizations, setting __debug__ = False.
    import htrc.volumes as volumes