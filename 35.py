# In the below program, if your input is 0 , while loop 
# will 'break' and the code inside 'else' clause will not get execuded.
# if you are using other numbers as input, while loop will complete its full cycle 
# and the code inside 'else' clause will be considered.


# while the 'else'
a=1
while a <= 3 :
    b = int (input("enter a number : "))
    if b==0 :
        print("exting loop with break command, 'else' is not executed ")
        break
    a+=1
else:
    print("loop extied without executing break command")


#using the print statment


# sei=10

# while sei<10 :
#     print(sei,end=',')
#     sei+=1