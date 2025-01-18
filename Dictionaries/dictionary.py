#dictionaries are used to store the data values in key:value pairs
#they are unordered,mutable and don't allow duplicate keys

info={
    "name":"aditya",
    "age":18,
    "hobby":"cooking"
}
print(info)
#keys - name,age,hobby
#value-aditya,18,cooking

#list,tuples and other datatypes can be added in value.
# list,dictionaries are not acceptable in keys as they are mutable.

dict={
   "name":"aditya",
   "subject":["english","python","cpp"],
   "age":22
}
print(type(dict))
print("the age is ",dict["age"])

dict["name"]="adi" #mutable ; it can change the values by accessing the keys
dict["surname"]="sathawane"
print(dict)

#null dictionary
null_dict={}
print(null_dict)

#nested dict
students={
    "name":"aditya",
    "subjects" : {
        "phy":97,
        "chem":69,
        "maths":100
    },
    "age":22
}
print(students)
print(students["subjects"])
print(students["subjects"]["chem"]) #accessing elements from nested dict