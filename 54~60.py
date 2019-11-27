# print('------------------------54------------------------')

# def name(dictionary):
#     for key,value in dictionary.items():
#         print(f'At spiceup {key} is headled by {value}')


# assingment={}

# while True:
#     program=input('enter the name of programming languge :')
#     studet=input('enter the student name : ')
#     assingment[program]=studet
#     more=input('do you want to add one more item (y/n) :')

#     if more=='y':
#         continue
#     else:
#         break
# name(assingment)


# def human(dict):
#     for key,value in dict.items():
#         print(f'My name is {key} hoby is{value}')


# ass={}

# while True:
#     hoby=input('what is you are hoby? :')
#     name=input('what you are name? :')
#     ass[name]=hoby
#     more=input('Have you more friends? Yes or No :')
#     if more=='Yes':
#         continue
#     else:
#         break

# human(ass)

# print('------------------------55------------------------')

# def coun(dictionaly):
#     county=list(dictionaly.values())
#     for con in county:
#         val=con.count(con)
#         print(f'I was born {val},I like {con}')


# kind={}

# while True:
#     country=(input('which you are country :?'))
#     food=(input('what kind of food :?'))
#     kind[country]=food
#     more=(input('And more(y/n) :?'))
#     if more=='y':
#         continue
#     else:
#         break
# coun(kind)

# print('------------------------57------------------------')

# def simple_interest(a,b,c):
#     return(a*b*c)/100
    

# a=float(input('enter the p number :'))
# b=float(input('enter the t number :'))
# c=float(input('enter the r number :'))



# print(simple_interest(a,b,c))

# print('------------------------58------------------------')
# def me(*name):
#     for nam in name :
#         print(type(nam))

# me('lohit',10,10.3,'sei','daiki',3.14)

# print('------------------------59------------------------')

# message='water'

# def globals():

#     message='I am stay in India'
#     return message

# print(globals())
# print(message)

print('------------------------60------------------------')


def calculate(*args):
    
    sum=0
    for arg in args:
        sum=sum+arg
    print('The sum is ',sum)
sum=0
calculate(10,20,30,40,50)
print('Value of sum outside the function',sum)

