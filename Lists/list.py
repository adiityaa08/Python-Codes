# similar to arrays in other languages seperated by comma
# a built in datatype that stores a set of values
marks=[1,2,3,4,5]
print(marks)
print(type(marks))
print(marks[-1])

#it can store elements of different types(int,float,str)
random=[2,'as','a',34]
print(random[0])

# strings are immutable while lists are mutable(change)
random=[2,'as','a',34]
print(random[0])
random[0]=100
print(random) #it allows updation

#list slicing
nums=[1,2,3,4,5,6,7,8,9]
print(nums[0:5]) #excludes last digit i.e 0,1,2,3,4
print(nums[1:])
print(nums[:2])
print(nums[0:7:2]) #slicing+skip
print(nums[::-1]) #reverses the list