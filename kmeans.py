#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 09:30:56 2018

@author: zhenhao
"""

from sklearn.cluster import KMeans
import numpy as np
from tensorly import decomposition

def KMProcess(arr, clusters=3):
    kmeans=KMeans(n_clusters=clusters).fit(arr)
    labels=kmeans.labels_
    
    return kmeans, labels

def generateRandomArr(dimension = (512,4,4), count=50):
    lst=[]
    for i in range(count):
        lst.append(np.random.random_sample(dimension))
    
    lst=np.asarray(lst)
    return lst

def simpleReshape(lst):
    lst=np.reshape(lst, (lst.shape[0],lst.shape[1]*lst.shape[2]*lst.shape[3]))
    return lst

def tensorDecom(lst):
    lst2=[]
    for i in lst:
        factors, weights, errors=decomposition.parafac(i, 1)
        factors=factors.reshape(factors.shape[0])
        lst2.append(factors)
    
    return np.asarray(lst2)

def main(lst=(), clusters=3):
    if len(lst)==0:
        #Generation of 50 tensors
        lst=generateRandomArr()
    
    #PCA equivalent for tensors
    lst2=tensorDecom(lst)
    
    #Kmeans for the decomposed tensor
    kmeans, label=KMProcess(lst2)
    
    return lst, label

lst, label=main()
