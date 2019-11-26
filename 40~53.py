# print('---------------40-----------------------------------')
# a=10
# while a>0:
#     a-=1
#     if a==3:
#         break
#     print(a)

# a=10
# while a>0:
#     a-=1
#     if a==3:
#         continue
#     print(a)

# a=10
# while a>0:
#     a-=1
#     print(a)
#     if a==3:
#         continue
#     else:
#         print('done')

# print('---------------41-----------------------------------')
# def all():
#     print('welcome')
# all()

# def name(name):
#     print('my name is '+name)

# name('sei')

# print('---------------42-----------------------------------')
# def student(name,age):
#     print(f'My name is {name},My age is {age}')
#     print('My name is',name,'My age is',age)
# student('daiki',20)

# print('---------------43-----------------------------------')
# def spiceup(IT,English):
#     print(IT,' is IT student. ',English,' is English student')

# I=input('who is IT student? :')
# Eng=input('who in english student? :')

# spiceup(I,Eng)

# print('---------------44-----------------------------------')
# def deta(name='lohit',age='20',country='India'):
#     print(f'my name is {name}. my age is {age}.i was born {country}.')

# deta()
# deta('sei','25','Japan')

# print('---------------45-----------------------------------')

# def my_arguments(username,phonenumber):
#     #c pragram 
#     print('hello %s,from phonenumber %s '%(username,phonenumber))

#     print(f'hello {username},from phonenumber {phonenumber}')

# my_arguments('banu','090909090')

# print('---------------46-----------------------------------')
# def sum_two(a,b):
#     return a+b
# c=(100+200)
# print(c)

# def mul(a,b,c):
#     print(a*b*c)

# x=mul(1,2,3)
# print(x)

# def mul(a,b,c):
#     return(a*b*c)

# x=mul(1,2,3)
# print(x)

# print('---------------47-----------------------------------')
# def area(radians,pai):
#     return (radians*2*pai)

# x=area(2,3.14)
# print(x)

# def number(num):
#     if num==0:
#         return 1

#     return num*number(num-1)

# num=int(input('enter the number :'))
# print (number(num))

# print('---------------48-----------------------------------')
# def score(a):
#     if 60>a:
#         return True
#     return False

# print(score(90))
# print(score(40))

# print('---------------49-----------------------------------')
# def fun(a):
#     a[1]=120

#     a=[20,30,40]

# lists=[1,2,3,4,5,6,7]

# fun(lists)
# print(lists)

# print('---------------50,51-----------------------------------')
# #仮引数の頭に米をつける
# def num(*home):
#     for house in home:
#         print(house)
# num('lohit','python','php','ruby')

# print('---------------52-----------------------------------')
# def rad(radius):
#     return radius*radius*3.14

# def vol(rad,len):
#     print(rad*len)

# radians=int(input('How long radius : '))
# len=int(input('How long length : '))
# vol(rad(radians),len)

print('---------------53-----------------------------------')
x=666
y=444

def sum():
        x=44
        print(x+y)

        x=66
        print(x+y)
sum()
print(x+y)

