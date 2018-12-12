#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:14:37 2018

@author: zhenhao
"""

import h5py
import os
import cv2
import numpy as np
from PIL import Image

#reading in full icons file
mainfolder='LLD_favicons_full_png'
lst=os.listdir(mainfolder)

store=[]
for i in range(10):
    fname=mainfolder+'/'+lst[i]
    img=Image.open("LLD_favicons_full_png/228006.png")
    rgb=np.array(img)
    store.append(rgb)
    img.close

store=np.asarray(store)

fw = h5py.File('icons_test.hdf5','w')
#data=fw.create_group('data')
data.create_dataset('data', data=store)

fw.close()

#reading in hdf5 file
#iconsFile='LLD-icon.hdf5'
#f = h5py.File(iconsFile,'r')
#
#data=f['data']
#labels=f['labels']
#meta_data=f['/meta_data/names']
#
#f.close()