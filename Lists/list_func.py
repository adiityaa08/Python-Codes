nums=[3,4,2,5,6,1]
print(len(nums)) # gives the length of list
nums.sort()  #sorts the list (ascending)
print(nums)
nums.append(9) #appends the element in list 
print(nums)
nums.sort(reverse=True) # reverses the list in sorted manner(descending)
print(nums)

list=['a','c','f','g']
list.reverse() #reversess the list
print(list)

list.insert(3,'x') #inserts the element at given index and which element is to be inserted
print(list)
print(len(list))

list.remove('c') #removes the first occurence of element
print(list)
list.pop(1) #removes element at index
print(list)