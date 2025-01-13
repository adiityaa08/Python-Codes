# if-elif-if statement
age=int(input("enter your age")) # input statement always has the str type so we conevrt it to int
if (age > 18):
    print("age greater than 18")
elif(age==18):
    print("age equals to 18")
else:
    print("age more than 18") #indentation is required 4 spaces

# practice question

marks=int(input("Enter Your Marks"))

if(marks>90):
    print("garde : A")
elif(marks>=80 and marks<90):
    print("grade : B")
elif(marks>=70 and marks<80):
    print("grade : C")
else:
    print("grade : D")

# nesting 
age=int(input("enter ur age"))
gender=input("enter ur gender ")

if(age>=18):
    if (gender == 'M'):
        print("Male")
    elif (gender == 'F'):
        print("Female")
    else:
        print("Invalid gender entered. Please enter 'M' for Male or 'F' for Female.")
else:
    print("Enter age above 18")