# 3.	Write a Python program to create the multiplication table (from 1 to 10) of a number.
'''
n=int(input("Enter the number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j)
    print()
'''

#5.Write python program to print the pattern given below
'''
Note: Take input from user
1
22
3 3 3
4 4 4 4
5 5 5 5 5


n=int(input("Enter the number:"))
for i in range(1,n+1):
    print(""*i,end='')
    for j in range(1,1+i):
        print(i,end=' ')
    print()
'''


#2 Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
num=[1,2,3,4,5,6,7,8,9]
odd=0
even=0
for i in num:
    if i % 2 ==0:
        even+=1
    else:
        odd+=1
print("numbers of even",even)
print("numbers of odd",odd)
'''




#1 Python Program to Read a Number n And Print the Series “1+2+…..+n= “

'''
n=int(input("Enter the number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print(sum)
    













#4 Given the triangle of consecutive odd  numbers Example we call function :- row_sum_odd_numbers(2)
'''
Result will be=3 + 5 = 8
if user give 4 then ur output is 13 + 15 + 17+ 19 = 64

def row_sum(n):
    return n**3
print(row_sum(4))
print(row_sum(2))

'''










