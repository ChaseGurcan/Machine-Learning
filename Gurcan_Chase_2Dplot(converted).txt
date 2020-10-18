# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:25:32 2020

@author: chase
"""

import numpy as np
import matplotlib.pyplot as plt

fin = open('IrisData.txt', 'r')

astring = fin.readline()

rows = int(astring)

data = np.zeros([rows,4])


for k in  range(rows):
    astring = fin.readline()
    astring=astring.strip()
    t = astring.split('\t')  
    #print(t)
    for j in range(4):
        data[k,j] = float(t[j])
#    for j in astring[-1]:
#        data[k,j] = str(t[4])
    #print(data)
    if "setosa" in astring:
        setosa = plt.scatter(data[k,2], data[k,0], color='red', marker ='x',label = 'setosa')
    elif 'versicolor' in astring:
         versicolor = plt.scatter(data[k,2], data[k,0], color='blue', marker ='x',label = 'versicolor')
    elif 'virginica' in astring: 
        virginica = plt.scatter(data[k,2], data[k,0], color='green', marker ='x', label = 'virginica')
        
fin.close()

      
plt.xlabel("Petal Length [cm]")
plt.ylabel('Sepal Length [cm]')  
plt.title('Sepal Length vs Petal Length of Setosa, Versicolor, and Virginica Flowers')
plt.legend([setosa,versicolor,virginica], ['setosa','versicolor','virginica'])
plt.savefig('Gurcan_Chase_MyPlot.png',bbox_inches='tight')   

plt.close