# 1.Write a function to find max of three numbers
'''
def max(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c

print(max(10,20,30))
print(max(30,10,20))
print(max(20,30,10))
'''


#2.Write a Python program to detect the number of local variables declared in a function.
'''
def f1():
    x=10
    y=20
    z=1.0
    a="Abhi"
    b="shek"
print(f1.__code__.co_nlocals)
    
f1()

'''
#3.Write a recursive function to calculate the sum of numbers from 0 to 10 Expected output: 55
'''
def add(n):
    if n==1:
        return n
    else:
        return n+add(n-1)

print(add(10))
    
'''


#4
'''
    Create a function showStudent() in such a way that it should
    accept student id, name, and it’s college name  and if the id
    and college name is missing in function call it should show it as by default
    id is 1 and college name  is VITA.

def show_student(s_name,s_id=1,clg_name = "VITA"):
    print("student_name:",s_name,"\tStudent_id:",s_id,"\tCollege_name:",clg_name)
    
show_student("Abhishek")
show_student("Abhishek",2,"SMVITA")

'''



#5
'''
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [11,22,22,33,33,33,44,55,55,66]
Unique List : [11, 22,33, 44, 55,66]

def unique_list(l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2

print(unique_list([11,22,22,33,33,33,44,55,55,66]))

'''













#6

'''
Write a program to obtain the sum of the first and last digit of this number 2 user defined functions
1st for first digit
2nd for last digit
Example:
Input:  5424
Output: 9


def sum_digit(n):

    s = str(n)
    a= int(s[0])
    b= int(s[-1])
    print(a+b)

sum_digit(5424)
sum_digit(6123)

'''





