# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 18:48:31 2023

@author: adrya
"""

#Numpy problems :
    
import numpy as np

#Problem 1
v = np.arange(21)
v[9:16] = -v[9:16]
print(v)

#Problem 2
v2 = np.arange(15,56)
print(v2[1:-1])

#Problem 3
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
for row in range(3):
    for col in range(4):
        print(a[row, col])

#Problem 4
a = np.linspace(5,50,10)
print(a)

#Problem 5
a = np.random.randint(0, 11, 5)
print(a)

#Problem 6
a = np.random.randint(1,10,3)
b = np.random.randint(1,11,3)
print(a)
print(b)
print(a*b)

#Problem 7
m = np.arange(10, 22).reshape(3, 4)
print(m)

#Problem 8
m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
row,col = m.shape
print("Number of rows : {} \nNumber of columns : {}". format(row,col))

#Problem 9
m = np.zeros((4, 4), dtype=int)
m[1::2, ::2] = 1
m[::2, 1::2] = 1
print(m)

#Problem 10 
Array1 = [0,10,20,40,60]
Array2 = [10,30,40]
Common_val = []
for i in Array1:
    for j in Array2:
        if i == j:
            Common_val.append(i)
print(Array1)
print(Array2)
print("Common values between two arrays: ")
print(Common_val)

#Problem 11
a = np.array([10,10,20,20,30,30])
a_unique = np.unique(a)
print("Original array:")
print(a)
print("Unique elements of the above array:")
print(a_unique)

#Problem 12
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
cross = np.cross(a,b)
print(cross)

#Problem 13
cartesian_coords = np.random.rand(10, 2)
x, y = cartesian_coords[:, 0], cartesian_coords[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
print(cartesian_coords)
print(r)
print(theta)

#Problem 14
array = np.arange(100)
val = np.random.uniform(0,100)
closest = array[(np.abs(array - val)).argmin()]
print(array)
print(val)
print(closest)