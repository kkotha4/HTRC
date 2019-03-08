#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:47:13 2019

@author: kashish
"""

from htrc_features import FeatureReader

import json

path= ['data.json']

f=FeatureReader(path)
with open('data.json') as f:
    data = json.load(f)
