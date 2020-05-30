				
#1.  Python program to Swap Keys and Values in Dictionary.
'''
Dict={"Name":"Abhishek","city":"Rajnandgaon","state":"Chhattisgarh","pin_code":491441}
Dict1={}
for key,value in Dict.items():
    if key in Dict:
        Dict1[value]=key
    else:
        Dict1[value]=key
        
print(Dict1)
'''

#2.  Write program to implement Selection sort.
'''
list1=[56,26,89,5,0,16]
print(list1)
for i in range(len(list1)):
    min_val=min(list1[i:])
    min_ind=list1.index(min_val)
    list1[i],list1[min_ind]= list1[min_ind],list1[i]
               
print(list1)

'''
#3.  Write program to implement Insertion sort.

'''
def insertionsort(list1):
    for i in range(1,len(list1)):
        curr_element = list1[i]
        pos = i
        while curr_element < list1[pos-1] and pos >0:
            list1[pos] = list1[pos-1]
            pos = pos - 1
        list1[pos] = curr_element

l=[2,5,9,4,3]
insertionsort(l)
print(l)
'''

#4.
'''
Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list.
Given list: list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]
Sub List to be added = ["h", "i", "j"]
Expected output:-
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m",  "n"]

list1[2][1][2].extend(["h", "i", "j"])
print(list1)


'''

#5. Access the value of key “history”
'''
sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
Expected output: 80


sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]['student']['marks']['history'])


'''


