# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 10:56:31 2020

@author: chase
"""

import numpy as np

fin = open('REData.txt', 'r')

astring = fin.readline()
astring=astring.strip()

darray = astring.split('\t')

n = int(darray[1])
m= int(darray[0])
data = np.zeros((m,n+1))
X = np.ones((m,n+2))
Y = np.zeros((m,1))

X_sq = np.ones((m,n+2))
X_combo = np.ones((m,2*n+2))

#double_input = np.ones((m,2*n +1))

for row in  range(m):
    new_string = fin.readline()
    new_string=new_string.strip()
    darray = new_string.split('\t')  
    for col in range(n+1):
        data[row,col] = float(darray[col])
        
r1 = np.array([[248,7]])
X[:,1:8] = data[:,0:7]
Y[:,0] = X[:,-1]

data_sq = data*data
X_sq[:,1:8] = data_sq[:,0:7]

double_input1 = np.array((data[:,0],data_sq[:,0],data[:,1],data_sq[:,1],data[:,2],data_sq[:,2],data[:,3],data_sq[:,3],data[:,4],data_sq[:,4],data[:,5],data_sq[:,5],Y[:,0]))
double_input = double_input1.T
X_combo[:,1:14] = double_input[:,0:13]

#------------ Normal data -------------------------------------------------------------
train = X[0:248,:]
valid = X[248:331,:]
test = X[331:,:]

np.savetxt('train.txt',train,delimiter = '\t', fmt='%.6f')
np.savetxt('valid.txt',valid,delimiter = '\t',fmt='%.6f')
np.savetxt('test.txt',test,delimiter = '\t',fmt='%.6f')

    
    
#------------ squared data -------------------------------------------------------------

train_sq = X_sq[0:248,:]
valid_sq = X_sq[248:331,:]
test_sq = X_sq[331:,:]

np.savetxt('train_sq.txt',train_sq,delimiter = '\t',fmt='%.6f')
np.savetxt('valid_sq.txt',valid_sq,delimiter = '\t',fmt='%.6f')
np.savetxt('test_sq.txt',test_sq,delimiter = '\t',fmt='%.6f')

#----------Combined data---------------------------------------------------------------------

train_combo = X_combo[0:248,:]
valid_combo = X_combo[248:331,:]
test_combo = X_combo[331:,:]

np.savetxt('train_combo.txt',train_combo,delimiter = '\t',fmt='%.6f')
np.savetxt('valid_combo.txt',valid_combo,delimiter = '\t',fmt='%.6f')
np.savetxt('test_combo.txt',test_combo,delimiter = '\t',fmt='%.6f')