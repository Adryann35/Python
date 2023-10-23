# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:26:59 2023

@author: adrya
"""

import matplotlib.pyplot as plt
import numpy as np



x = np.linspace(-2,2,101)
y = x**2
print(x)

plt.plot(x,y)
plt.show()

#Cos function
points = int(input("Number of points to draw : "))
x = np.linspace(-1,1,points)
plt.title('Body fuction (2pix)')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.cos(2*np.pi*x))

#Cos and sin function
points = int(input("Number of points to draw : "))
x = np.linspace(-1,1,points)
plt.title('Body function (2pix)')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.cos(2*np.pi*x),label = "cos(2pix)")
plt.plot(x,np.sin(2*np.pi*x), label = "sin(2pix)")
plt.legend()

points = int(input("Number of points to draw : "))
x = np.linspace(0,4,points)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.sin(np.pi*x)*np.sin(20*np.pi*x)*np.exp(-x))

#Isotherm function
points = int(input("Number of points to draw : "))
temp = int(input("Enter the temperature : "))
x = np.linspace(2,10,points)
plt.xlabel("Vm")
plt.ylabel("p")
plt.title("Isotherm (ideal gas")
plt.plot(x,(0.082*temp)/x)

#Gaussian function
points = int(input("Number of points to draw : "))
start = int(input("Enter start value : "))
end = int(input("Enter end value : "))
x0 = int(input("Enter x0 value : "))
s = float(input("Enter s value : "))
x = np.linspace(start,end,points)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Gaussian function")
plt.plot(x,(1/np.sqrt(2*np.pi))*np.exp(-((1/2)*(x-x0)**2)/s**2))

#Functions
points = int(input("Number of points to draw : "))
x = np.linspace(0,3,points)
plt.title('Functions')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x,np.exp(-x),label = "e(-x)")
plt.plot(x,np.sin(3*np.pi*x)*np.exp(-x),label = "sin(3pix)e-x")
plt.legend()

