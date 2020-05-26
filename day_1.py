#4 WAP to check wheather number is even or odd using if else statement
'''
n=int(input("Enter the number:"))
if n%2==0:
    print(n," is Even Number")
elif n%2==1:
    print(n,"is Odd Number")
else:
    print(n,"is Invalid Number")
'''

#5 wap to kids aged grants or not grant
'''
age=int(input("Enter the age:"))
if (age>=8) and (age<=12):
    print("welcome to the party")
else:
    print("Sorry not allowed in party ,'byee'")
'''


#3 wap to convert a string in upper case
'''
s=input("Enter the string:")
print("The original string is:",s)
print("The Upper case string is:",s.upper())
'''


#1 wap which will find all such number divisible by 7 but not multiple by 5
'''
a=2000
e=3201
for i in range(a,e):
    if (i % 7 ==0) and (i % 5 != 0):
        print(i)
'''


#2 with a given integer  n ,wap to generate a dict that contain betn 1 to n
'''
n= int(input("Enter the Number"))
dict1=dict()

for i in range(1,n+1):
    dict1[i]= i*i
print(dict1)

'''










