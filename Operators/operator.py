a=2
b=3
#airthematic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#relational
print(a==b)
print(a>b)
print(a<b)
print(a!=b)

# assignment
a=10
print(a)
a+=10
print(a)
a-=10 # by above result a=20 
print(a)
a*=10
print(a)
a/=10
print(a)
a**=10
print(a)

#logical
print(not False)
print(True and False)
print(True or False)

#type conversion
a=1
b=3.5
print(a+b)

a="2"
print(a+b)

#type casting
a="10"
b=10 
c=int(a) # float(),string()
print(c+b)

d=10
print(type(str(d)))

#how to take input

name=input("enter any name:")
print("WELCOM",type(name)) # the type of ouput is alaways is str

name=int(input("enter any number"))
print(type(name),name)
