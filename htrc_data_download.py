#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:19:56 2019

@author: kashish
"""
import json
if __debug__:
    # This code will execute when running `python script.py`
    import htrc.mock.volumes as volumes
else:
    # This code will execute when running `python -O script.py`
    # The -O argument turns on optimizations, setting __debug__ = False.
    import htrc.volumes as volumes

with open('/home/dcuser/kashish/HTRC/data.json') as f:
    data = json.load(f)
#convert all the volume id's into list
volume_ids=list(data)
tok=volumes.get_oauth2_token('kkothari442', 'K@shish99')
print(token)
v=volumes.get_volumes(token, [volume_ids[0]], concat=True)
#print(vol)
volume = [volume_ids[0]]
output_directory="kk"
volumes.download_volumes([volume_ids[0]],output_directory,token=tok,concat=True)


print("completed")
print(len(volume_ids))
