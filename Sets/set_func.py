set1={1,1,1,1,1,2,2,2,2,3,3,3,3}
print(set1)

# set1.add(4)  # adds element in set , takes only argument
# print(set1)

# set1.remove(2) # removes element from set
# print(set1)

# set1.pop() #pops the element out of set from start(generally a random value)
# print(set1)

# set1.clear() #empties the set
# print(len(set1))

set2={3,4,3,2,5}
print(set1.union(set2)) # it returns the unified set of both sets.
# original sets remains the same 
print(set1)
print(set2)

print(set1.intersection(set2)) #it returns the intersection(common values) set of both sets.
