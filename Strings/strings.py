name="aditya"
print(name)
print(name[0]) # 0-based indexing starts from front
print(name[-4]) # -1 based indexing starts from back

#string slicing
print(name[0:4]) # excludes last index
print(name[-4:-1]) # negative indexing
print(name[-5:-3])
print(name[1:]) # ends up at length
print(name[:5]) # starts from 0

#string slicing skip
print(name[1:5:2]) #it starts from '1' goes till '4' and in between it skips the letters at interval of 2
print(name[1:5]) #o/p-> 'dity'  so the skip starts from 'd' then it starts counting from 'd(1)->i(2)' then print next letter't'.
