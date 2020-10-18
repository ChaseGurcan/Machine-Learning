# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 13:10:57 2020

@author: chase
"""


import numpy as np

prompt = input('Please type the name of the training dataset: Gurcan_Chase_Train.txt \n')

fin = open(prompt , 'r')

astring = fin.readline()
astring = astring.split('\t')
n = int(astring[1])
m= int(astring[0])

data = np.zeros([m,n])

for row in  range(m):
    bstring = fin.readline()
    bstring = bstring.split()
    for col in range(n):
        data[row,col] = float(bstring[col])
        
        
fin.close()    
        
#  Prints out values for all weights and final J for the training set
X = data[:,0:n-1]
#Y = np.zeros([m,1])
Y = data[:,-1]

weights = np.dot(np.linalg.pinv(np.dot(X.T,X)),np.dot(X.T,Y))

m_m1 = np.ones((m,1))

J_train = np.dot(m_m1.T,((np.dot(X,weights)-Y)*(np.dot(X,weights)-Y)))/(2*m)

#time.sleep(3)


prompt2 = input('Please type the name of the validation or testing set: Gurcan_Chase_Valid.txt or Gurcan_Chase_Test.txt \n')


fin2 = open(prompt2 , 'r')
   
string = fin2.readline()
string = string.split('\t')
nn = int(string[1])
mm = int(string[0])

data1 = np.zeros([mm,nn])

for row1 in  range(mm):
    cstring = fin2.readline()
    cstring = cstring.split()
    for col1 in range(nn):
        data1[row1,col1] = float(cstring[col1])
            
fin2.close()    

X2 = data1[:,0:n-1]
Y2 = data1[:,-1]

m_m1_2 = np.ones((mm,1))

J = np.dot(m_m1_2.T,((np.dot(X2,weights)-Y2)*(np.dot(X2,weights)-Y2)))/(2*mm)

#Calculating R squared for the test dataset
Y_mean = np.mean(Y2)

denom = (np.dot(m_m1_2.T,((Y2-Y_mean)*(Y2 - Y_mean))))/(2*mm)

R_sq = 1- (J/denom)

Adj_R_sq = 1- ((1-R_sq)*(mm-1)/(mm-nn-1))





















