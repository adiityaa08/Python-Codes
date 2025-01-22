# for loop is a sequential traveseral loop, for taversing list,strings,tuples etc

list=[0,1,2,3,4,5]
for i in list:
    print(i)

# string="aditya"
# for i in string:
#     print(i)

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=49
# idx=0
# for i in nums:
#     if(i==x):
#         print("element found at ",idx)
#     idx+=1

# RANGE function
# range function return a sequence of numbers,starting from 0 by deafult , increments by 1 and stops before a specified number 

# SYNTAX ---- range(start,stop,step)

# print(range(0,5))

# 1st way 
for i in range(5): #stop condition
    print(i)

for i in range(2,6): # start,stop
    print(i)

for i in range(2,10,2): #start,stop,step of 2
    print(i)

# pass statement:- it is a null statement that does nothing.
for i in range(5):
    pass
print("by")