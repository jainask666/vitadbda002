#3.	Print the pattern
'''
            1
            1 2 
            1 2 3
            1 2 3 4
            1 2 3 4 5

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j,end=' ')
    print()
'''

#4 .Accept data in two 3*3  matrix and calculate the sum of the matrices.

'''
import numpy as np

a=np.arange(9)
a=a.reshape(3,3)
print(a)

b=np.arange(9)
b=b.reshape(3,3)
print(b)

c=a+b
print(c)
'''


#2.From a list containing ints, strings and floats, make three lists to store them separately.
'''
x=[1,2,1.0,2.0,"Abhi","Shek"]
a=[]
b=[]
c=[]
for i in x:
    if type(i) == int:
        a.append(i)
    elif type(i) == float:
        b.append(i)
    else:
        c.append(i)
print(a,b,c)

'''


#1.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
'''
l=[1,2,3,4,5]
a=[]
for i in l:
    a.append(i*i)
print(a)
'''




#5
'''
5.Write a Python program to check whether a given number is a narcissistic number or not
For example, 371 is a narcissistic number; it has three digits, and if we cube each digits  33 + 73 + 13 the sum is 371. Other 3-digit narcissistic numbers are
153 = 13 + 53 + 33

n = int(input("Please enter number to check :"))
a = n
b = 0

if len(str(n)) >  0:
    p = len(str(n))
    while n > 0:
        d = n % 10
        b += d ** p
        n = n // 10
if a == b:
    print(a,"is a narcissistic number")
else:
    print(a,"Not a narcissistic number")

'''


















   
