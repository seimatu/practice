def printme(*names):
    print('whith data type is added',type(names))
    print('printing the passed arguments')
    for name in names:
        print(type(name))
#callong the function
printme(100,10.90,'lohit')

print('----------------------------------------')


# def printme(*names):
#     print('whith data type is added',type(names))
#     print('printing the passed arguments')
#     for name in names:
#         print(name)
# #callong the function
# printme(100,10.90,'lohit')