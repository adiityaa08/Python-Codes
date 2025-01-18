# sets is a collection of unrodered items.
# set is mutable but the elements in set are immutable
# each element in set is unique and immutable
# since elements are immutable it can only take immutable datatypes like int,float,strings,tuple etc 
# it cannot take dict,list

# set={1,2,3,4,5}
# print(set)

#it only consider unique values ignores duplicate values

set1={1,1,1,1,1,2,2,2,2,3,3,3,3}
print(set1)
print(len(set1))
# print(type(set))

#null_set
null_set={}  #it's the same syntax as empty dict
print(type(null_set))
# to convert it into set use set()

null_set = set()
print(type(null_set))