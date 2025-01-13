# a built in datatype that lets us create immutable sequences of values
# it uses parenthesis while in List we use sqaure brackets

tuple=(1,2,3,4)
print(type(tuple)) 
print(tuple[2])
print(tuple[1])

# tuple is IMMUTABLE

#empty tuple
tup=()
print(tup)

tup=(1,) #always use comma otherwise it will be treated as int
print(type(tup))

tup=(1)
print(type(tup))

# TUPLE SLICING
tup=(1,2,3,4,5,6,7)
print(tup[2:6])
print(tup[1:])
print(tup[:5])

# TUPLE FUNCTIONS
tup=(1,2,3,4,5,4)
print(tup.index(3)) # return the first occurence of elements
print(tup.count(4)) # return the total count of element