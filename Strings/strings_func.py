name="aditya"
print(len(name)) #return the length of string

print(name.endswith("tya")) #returns the value if the string ends with the given substring
print(name.endswith("adix")) #returns the value if the string starts with the given substring
print(name.capitalize()) #capitalize the first character
name="aditya hi"
print(name.title()) #capitalize the first character of each word
print(name.find("hi")) #return the index of first occurence of that word

#f-string
name=input("enter your name")
print(f"good afternoon,{name}")
# reverses the string
gfg = "aditya"
print(gfg[::-1])