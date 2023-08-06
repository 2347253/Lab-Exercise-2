i) Create a LIST with your domain attributes, insert the elements using the append (), insert(), extend() and add any iterables (tuples, sets, dictionaries etc.) to the list (Use all the methods ).

lst=['TenZ','Sentinels',22,10000.0,True]
print(lst)
lst.append("Shahzam")
print(lst)
lst.insert(0,1)
print(lst)
lst.extend(['Esports','Players',('Hunter','Dapr')])
print(lst)


Create a list with numeric and perform the following operations.
·Write a program to swap the first and last elements in a list.
listnew=[1,2,3,4,-5,-6,7,8,9,10]
firstelement=listnew[0]
lastelement=listnew[-1]
listnew.pop(0)
listnew.pop(-1)
listnew.append(firstelement)
listnew.insert(0,lastelement)
print(listnew)
#another way to swap elements
listnew[0],listnew[-1] = listnew[-1],listnew[0]
print(listnew)
·Write a program to find the sum of the digits in a list.
sum=0
for i in listnew:
        sum+=i
print(sum)




·Write a program to find the smallest element in a list.
listnew=[1,2,3,4,-5,-6,7,8,9,10]
smallest=listnew[0]
for j in listnew:
    if j<listnew[0]:
        smallest=j
print(smallest)

#another way to find smallest
listnew.sort()
print(listnew[0])




ii)Dictionaries
·Sort the dictionaries in ascending order based on the Key of the dictionary.
dictionary={3: "Valorant" , 1: "CSGO" , 2: "PUBG" , 4: "GTA"  }
new={}
to_a_List=list(dictionary.keys())
to_a_List.sort()
for i in to_a_List:
    sorteddict={i:dictionary[i]}
    new.update(sorteddict)
print(new)




· Create the dictionary with Numeric as Value in Key – Value pair and find the sum of all the values in the Dictionary.
dicto = {'a': 100, 'b': 200, 'c': 300, 'd':400}
list = []
sum=0
for i in dicto:
    list.append(dicto[i])
for j in list:
    sum+=j
print("Sum :", sum)



·Write a Python code to demonstrate the sorting in descending order of values with lambda function
# Sample dictionary
data = {'a': 100, 'b': 200, 'c': 300, 'd':400}
# Sorting the dictionary in descending order of values using lambda function
sorted_data = {k:v for k,v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

print(sorted_data)
