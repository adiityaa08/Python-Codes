students={
    "name":"aditya",
    "subjects" : {
        "phy":97,
        "chem":69,
        "maths":100
    },
    "age":22
}
print(len(students)) #length of dict -total no of keys

print(students.keys()) # returns all keys 

print(list(students.keys())) #typecasing in dict 

print(students.values()) #returns all the values of keys

print("\n", students.items()) #returns all the (key,val) pairs as tuples

print(students.get("subjects")) #returns the key according to the value

new_dict={
    "hobby":"arts"
}
students.update(new_dict) # add a dic or key-val pair in the original dict
students.update({"city":"Nagpur"}) # if same key from orginal dict is passed in new dict it overwrite the original value
print(students)