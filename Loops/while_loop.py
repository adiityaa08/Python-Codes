#loops are used to repeat instructions
# while loop

# a=1 #iterators.
# while a<=10:
#     print("hey,aditya!!")
#     a+=1
# print(a)

# Print Number from 1 to 10
# a=1 
# while(a<=10):
#     print(a)
#     a=a+1

# ------------- BREAK-------------
# used to terminate the loop when encountered

# i=1
# while(i<=10):
#     print(i)
#     if(i==3):
#         break  # here the loop gets terminated
#     i=i+1

# -------------CONTINUE-------------
# terminates the execution in the current iteration and continues execution of the loop with the next iteration
# it generally skips the current iteration
i=1
while(i<=10):
    if(i==3):
        i+=1 #->if this is not written it will have the value 3 and it will skip the next updation statement 
        continue #-> thus the value of i will not be increased
    print(i) 
    i+=1
