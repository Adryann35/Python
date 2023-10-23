# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:20:06 2023

@author: adrya
"""
import math as m
import numpy as np

n1 = 3.14
n2 = str(n1)
print(n2)

print('How much?')
rep = input()
n = float(rep)
print(2.5 + n)

'sparrow' > 'eagle'
'dog' > 'Cat' 
45%3 == 0
60 - 45 / 5 + 10 == 1


T = 298.5
P = 21.5
print ("The temperature is {} and the pressure is {} " .format (T,P))

r = float(input("Enter the row :"))
h = float(input("Enter the height :"))
v = 1/3 * 3.1415 * r**2 * h
print("The volume is {}" .format(v))

#Sinus
ang = 90
ang_rad = ang * m.pi / 180 
si = m.sin (ang_rad)
print("The sine of {} ° is {}" .format(ang,ang_rad))

#Temperature Celsius/Kelvin
C = float(input("Enter the temperature in celsius :"))
K = C + 273.15
print("The temperature in Kelvin is {}" .format(K))

#Area and volume of cube
L = float(input("Enter the lenght of the edges :"))
area = 6 * L**2
volume = L**3
print("The area of the cube is {} and the volume is {}" . format(area,volume))

#Total value of money
nb10 = int(input("Enter the number of 10 euro banknotes :"))
nb20 = int(input("Enter the number of 20 euro banknotes :"))
nb50 = int(input("Enter the number of 50 euro banknotes :"))
total = nb10 * 10 + nb20 * 20 + nb50 * 50
print("In total you have {} euros" .format(total))

#Length and area of a circle
r = float(input("Enter the radius of a circle :"))
L = 2 * m.pi * r
A = m.pi * r**2
print("The length is {} and the area is {}" .format(L,A))

#Length side triangle
a = 11.2
b = 8.5
ang = 37
ang_rad = ang * m.pi / 180
c = m.sqrt(a**2 + b**2 - 2*a*b*m.cos(ang_rad))
print("The third side is {}" .format(c))

#Print function
message = 'good morning'
print(message[8:11])
print(message.upper())
print(len(message))
print(message.count('g'))
print(message.find('o'))
message = message.replace('Morning','Afternoon')

weight = float(input("Enter your weight :"))
height = float(input("Enter your height :"))
 

#Divisible
n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
if n1 > n2 :
    if n1%n2 == 0 :
        quotient = int(n1/n2)
        print("{} is divisible by {} and the quotient is {}".format(n1,n2,quotient))
    else :
        quotient = int(n1/n2)
        remainder = int(n1 - quotient*n2)
        print("{} is not divisible by {} and {}/{} = {}x{} + {}" .format(n1,n2,n1,n2,quotient,n2,remainder))

#Units
units = int(input("Enter number of units : "))
if units > 100 :
    rs5 = units - 100
if units > 200:
    rs10 = units - 200
total = rs5 * 5 + rs10 * 10
print("Total bill is {}" .format(total))

#Division by 3
num = int (input ("Enter an int value: "))
while num>0:
    res = num // 3
    print ("The integer division of {} by 3 gives {}". format(num,res))
    num = int (input ("Enter an integer value: "))    
print("Done")

#Number of divisions
num = int (input ("Enter an int value: "))
ndiv = 1
while ndiv<num:
    res = num // ndiv
    print ("The integer division of {} by {} gives : {}". format(num,ndiv,res))
    ndiv = ndiv + 1 
print ("Done")
print ("Total number of divisions: {}". format(ndiv))

#Number divisible by 3
num = 1
ndiv = 0
while num > 0 and num < 211 :
    if num%3==0:
        print(f"The number is {num}")
        ndiv = ndiv + 1
    num = num + 1
print("total number of iterations : {}". format(ndiv))
print("Done")

#Triangle de *
i=1
while i<=4:
    print ("*"*i)
    i += 1

    
name = 'Jesaa29Roy'
size = len(name)
i = -1
while i<size -1:
    i = i + 1
    if not name[i].isalpha():
        continue
    print(name[i],end=' ')

#Total sum
n = int(input("Enter n : "))
sum = 1
for i in range (1,n+1):
    sum = sum * i
print("For {} the factorial is {}". format(n,sum))

#Without repetition
for i in range(1,10):
    for j in range(1,10):
        if(i!=j):
            print("{}{}". format(i,j))
   
#Sum of digits is 22
for i in range(1,10):
    for j in range(1,10):
        for k in range (1,10):
            if(i+j+k == 22):
                print("{}{}{}". format(i,j,k))
                
for i in range(0,10):
    for j in range(0,10):
        for k in range (0,10):
            if((i*100+j*10+k == i**3 + j**3 + k**3)):
                print("{}{}{}". format(i,j,k))
#dIVISEURS            
n = 12
for i in range (1,n+1):
    if(n%i==0):
        print(i)
        
#Sum odds  
n = 5
sum = 0
for i in range (n+1):
    odd = 2*i+1
    print(odd)
    sum += odd
print("Sum is {} ". format(sum))

#Prime number
n = int(input("Enter a number"))
prime = 'true'
for i in range(2,n):
    if(n%i==0):
        prime = 'false'
if prime == 'true' :
    print("{} is prime". format(n))
if prime == 'false':
    print("{} is not prime". format(n))

#fibonacci
f1 = 0
f2 = 1
for i in range (6):
    t = f1
    f1 = f2
    f2 = f2 + t
    print("{} & {}". format(f1,f2))
    
#Liste 
us_president_list = ['Joe Biden','Donald Trump','Barack Obama','Barack Obama','George W. Bush','George W. Bush']
print(us_president_list[2])
us_president_list.append('Bill Clinton')
print(us_president_list)
us_president_list.remove('Bill Clinton')

smooth = [3.14,7,-2 + 3j,'water',False,[1,2]]
print(smooth)
print(len(smooth))
smooth[:4]
smooth[::2]
print(smooth [5][1])
smooth[3][4] 

#Sum list
list = []
for i in range(1,11):
    list.append(1/i)
sum(list)

line = input("Enter : ")
smooth_txt = line.split()
print(smooth_txt)
temp = []
for element in smooth_txt:
    value = float(element)
    temp.append(value)
print(temp)

a = [1,3,5,7,11]
b = [13,17]
c = a + b
print("C = {}". format(c))
b[0] = -1
d = []
for e in a :
    d.append(e+1)
print("D = {}". format(d))
d.append(b[0] + 1)
d.append(b[-1] + 1)
print("Third = {}". format(d))
print("Fourth : {}". format(d[-2:]))
print("Fifth : {}". format(d[:-1]))
print("Sixth : {}". format(d[1:4]))

#List squares
n = int(input("Enter n : "))
list_num = []
for i in range(n+1):
    list_num.append((i+1)**2)
print(list_num)

#liste nom et notes
list_name = []
list_grade = []
name = input ("Enter a name : ")
while name != "":
    grade = float(input("Enter the grade : "))
    list_name.append(name)
    list_grade.append((grade))
    name = input ("Enter a name : ")
for i in range(len(list_name)):
    print("{}  {}". format(list_name[i],list_grade[i]))
sum = sum(list_grade)
average  = sum/len(list_grade)
print(average)

#Moyenne
list=[]
sum = 0
num = input("Enter number : ")
while num !="":
    list.append(num)
    num = float(num)
    sum += num
    num = input("Enter number : ")
mean = sum/len(list)
print(mean)

#Separer noms
names = input("Enter names : ")
name = ""
for i in names :
    name += i
    if i== " ":
        print("Hi {}". format(name))
        name = ""
        
names = input("Enter names : ")
list = names.split()
for i in list :
    print("Hi {}". format(i))

#Somme atome
Element = ['H','C','N','O','S','Cl']
Atomic_mass = [1.008,12.011,14.007,15.999,32.065,35.453]
sum = 0
i = 0
for molecule in Element:
    n = float(input("Numbers of {} : ". format(molecule)))
    sum += n*Atomic_mass[i]
    i += 1
print(sum)

max = int(input("Enter the maximum degree : "))
list_degree = []
for i in range (0,max+1):
    c = float(input("Enter the coefficients of degree {} : ". format(i)))
    list_degree.append(c)
x = float(input("Enter the value of x : "))
result = list_degree[0]
i = 1
for d in list_degree:
    result += d**i
    i += 1
print(result)

#Dictionnary
country_capitals = {"United States": "Washington DC",
                    "Italy": "Rome"}
print(country_capitals)
print(country_capitals["Italy"])
country_capitals["Germany"] = "Berlin"
del country_capitals["Germany"]
for country in country_capitals:
    capital  = country_capitals[country]
    print(capital)
for keys,values in country_capitals.items():
    print(country_capitals.keys())
    print(country_capitals.values())
keys = ['Ten','Twenty','Thirty']
values = [10,20,30]
res_dict = dict(zip(keys,values))
print(res_dict)

#Fonction
def my_fct(**kid):
    print("His last name is " + kid["lname"])
    
my_fct(lname = "aa",fname = "b")

#Max
def biggest_num(x,y):
    if x > y:
        return x
    else :
        return y
biggest_num(6,7)

#Max et min
def max_min(*nums):
    max = nums[0]
    min = nums[0]
    for x in nums :
        if x > max:
            max = x
        if x < min:
            min = x
    return ("Largest is {} and smallest is {}". format(max,min))

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))
e = int(input("Enter a number : "))
max_min(a,b,c,d,e)

#Paire/Impaire
try:
    num = int(input("Enter a number : "))   
except ValueError as e:
    print(e)
else:
    if(num%2) == 0:
        print("{0} is Even". format(num))
    else:
        print("{0} is Odd". format(num))
finally:
    pass

while True :
    try :
        num = int(input("Enter a number : "))
        if(num%2) == 0:
            print("{0} is Even". format(num))
        else:
            print("{0} is Odd". format(num))
            break
    except ValueError as e:
        print(e)
        
while True :
    try :
        num = int(input("Enter a number : "))
        test = True
        for i in range(2,num):
            if num%i == 0:
                test = False
        if test == True:
            print("{} is prime". format(num))
        else :
            print("{} is not prime". format(num))
        break
    except ValueError as e:
        print(e)
            
import numpy as np

a = np.array ([[1,2,1,4,5,6,7],
              [8,9,2,12,13,20,14]])
a[0,0:5:2]

arr = np.array([[1,0,1]])
r1 = np.repeat(arr,3,axis=0)
r1[1,1] = 2
print(r1)

stats = np.array([[1,2,3],[4,5,6]])
np.min(stats)
np.min(stats,axis=1)
np.max(stats,axis=1)
np.sum(stats,axis=0)
np.sum(stats,axis=1)
np.sum(stats)   

angles = [0,np.pi/4,np.pi/3,np.pi/2]
angles = np.array (angles)
sin_ang = np.sin (angles)
print(angles) 
print(sin_ang)

values=np.linspace(10, 30,int)
print(values)
    

