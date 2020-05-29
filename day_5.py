#1.Write a Python program to sort a list of elements using the bubble sort Algorithm
'''
l=[25,15,10,5,0]
for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("sorted list in ascending order is",l)

'''
#2 Write a Python program for sequential search (Linear search).
'''
def linear_search(list1,key):
    for i in range(len(list1)):
        if key == list1[i]:
            print("key is found at index",i)
            break
    else:
        print("key is not found")

list1=[1,5,9,72,45,86,95,8]
print(list1)
key=int(input("pls enter the key from given list:"))
linear_search(list1,key)
'''


#3.Write a Python program for Binary search.
'''
def binary_search(list1,key):
    low=0
    high=len(list1)-1
    found=False
    while low <=high and True:
        mid=(low+high)//2
        if key == list1[mid]:
            found = True
        elif key > list1[mid]:
            low = mid + 1
        else:
            high= mid - 1
    if found == True:
        print("Key is Found")
    else:
        print("Key is not Found")

list1=[23,15,8,7,1,6]
list1.sort()
print(list1)
key=int(input("Enter the key:"))
binary_search(list1,key)

'''


#5

'''
Iterate a given list and check if a given element already exists in a
dictionary as a key’s value if not delete it from the list.
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sampledict = {“John”:47,”Peter”:64,”Mahi”:37,”Maria”:76}


roll_no=[47,64,69,37,76,89,95,97]
sampledict = {"Abhishek":47,"suresh":64,"kamlesh":37,"mukesh":76}
result = [i for i in roll_no if i in sampledict.values()]
print(result)
    
'''

#4
'''
Write a python program to concatenate two lists index-wise.
List1 = [“M”,”na”,”i”,”lak”]
List2 = [“y”,”me”,”s”,”han”]
Expected output:
[“My”,”name”,”is”,”lakhan”]

list1 = ['M','Na','i','Lak']
list2 = ['y','me','s','han']

result = [(i+j) for i, j in zip(list1, list2)]
print(result)
'''











