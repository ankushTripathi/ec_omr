# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:10:23 2017

@author: ankush
"""
from math import *
import matplotlib.pyplot as plt

alphabets = list(map(chr,range(ord('a'),ord('z')+1)))

N = 25
M = len(alphabets)


def X(c,i):
    j = ord(c)-96
    if i == 1 or i == N or j == 1:
        return 0
    else:
        return float(i*j)/(M*N)

def G(x):
    return float(0.76*(1-exp(-2*x)*cos(4*x)))

f,axarr = plt.subplots(3,figsize=(5,10))

S = raw_input("enter your name :")

p=0

P = []
v = []
y_g = []
y_a = []

for k in range(len(S)):
    
    (g,a,x) = ((float(k+1)/(2*N)),0.5,0.2) if S[k] == ' ' or S[k-1] == ' ' else (G(X(S[k],k+1)),float(abs(ord(S[k]) - ord(S[k-1])))/26,X(S[k],k+1))
    v.append(x)
    p+=float(g)*a
    P.append(p)
        
axarr[1].hist(list(map(G,v)),color='darkslategray',rwidth=0.8)
axarr[1].set_title('histogram of G(x) for given name')

axarr[2].plot([i for i in range(len(S))],P)
axarr[2].set_title('Propagating error for given name')

axarr[0].plot([i for i in range(len(S))],list(map(G,v)),color='orange',linestyle='--')
axarr[0].set_title('G(x) of given name')

f.subplots_adjust(hspace=0.3)

plt.show()
print(" error in omr :"+str(p))