#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:14:35 2017

@author: giorgecaique
"""

import pandas as pd
from collections import Counter

def sup(n, N):
    return(n / N)

def conf(nA, nAB):
    return(nAB / nA)

def lift(supAB, supA, supB):
    return supAB / (supA * supB)

def load_dataset():
    "Load the sample dataset."
    df = pd.read_csv("/Users/giorgecaique/Documents/Oraculum/Oraculum_Data/Data/SuperstoraDataset.csv", header=None, sep="\t", names=['productname'], encoding='UTF-16')
    dataset = []
    
    for item in df['productname']:
        text = item.split(',')
        dataset.append(text)
    return dataset

def create_freqset(dataset, k):
    "returns the frequence of each item in dataset"
    cnt = Counter()
    for l in dataset:
        if k == 1:
            for item in l:
                cnt[item] += 1
        elif k == 2:
            for i in range(0,len(l)):
                for j in range(0, len(l)):
                    if j == len(l):
                        break
                    if i == j:
                        continue
                    cnt[l[i], l[j]] += 1
    return cnt

def filter_itemsets(freqsets, minsupport, N):
    "returns the items with support higher than the minsupport"
    resultset = []
    for item in freqsets:
        s = sup(freqsets[item], N)
        if s >= minsupport:
            resultset.append({"itemset":item, "support":s, "confidence":0, "lift":0})
    return resultset
        

def run_apriori(dataset, N, minsupport):
    for i in range(1, 3): # k = 2
        freqsets = create_freqset(dataset, i) 
        resultset = filter_itemsets(freqsets, minsupport, N)
        for l in dataset:
            for item in l:
                if item not in [x['itemset'] for x in resultset]:
                    l.remove(item)
        i += 1
        yield resultset

def apriori(minsupport, minconfidence):
    dataset = load_dataset()
    N = len(dataset)
    result = []
    for item in run_apriori(dataset, N, minsupport):
        result.append(item)
    for item in result[1]:
        a = [x['support'] for x in result[0] if x['itemset'] == item['itemset'][0]][0]
        b = [y['support'] for y in result[0] if y['itemset'] == item['itemset'][1]][0]
        item['confidence'] = conf(a, item['support'])
        item['lift'] = lift(item['support'], a, b)
    filtered_result = [x for x in result[1] if x['confidence'] >= minconfidence]
    return filtered_result

result = apriori(0.001, 0.5)


    