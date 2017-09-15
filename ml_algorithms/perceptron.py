#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:32:13 2017

@author: giorgecaique
"""

"""dataset = [[1,1,2], 
           [1,2,3], 
           [2,2,4], 
           [3,2,5], 
           [3,5,8], 
           [4,4,8], 
           [4,9,13], 
           [8,6,14]]"""

dataset =  [[1,1,1,9],
            [1,2,1,14],
            [2,2,3,19],
            [2,3,4,25],
            [3,3,5,29],
            [6,4,9,47],
            [6,7,12,65],
            [4,8,12,64],
            [2,1,3,14],
            [2,2,3,19]]


#w = [0, 0.8] # Weight
w = [0, 0.8, 0.6]
Sn = [] # predicted result
#learning_tax = 0.016
learning_tax = 0.01
l_error = 0.1

age = 500

Sn = [] # restart predict list
train()

def train():
    
    for x in dataset:
        erro = 10
        sn = 0
        while erro > l_error or erro < 0:
            sn = run(x)
            print('sn:',sn)
            erro = x[2] - sn
            print('erro',erro)
            update_weight(x, erro)
        Sn.append(sn)
        

def run(x):
    result = 0
    for i in range(0, len(w)):
        result += x[i] * w[i]
    
    return result

def update_weight(x, erro):
    for i in range(0, len(w)):
        w[i] = w[i] + (erro * learning_tax * x[i])
    
