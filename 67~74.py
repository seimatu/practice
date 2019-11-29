# print('------------------67-----------------------------------')
# class person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def fun(self):
#         print('My name is ',self.name)

# peaple=person('sei',25)
# print(peaple.age)
# peaple.fun()

# peaple.name='lohit'
# print(peaple.name)
# peaple.fun()
# print('------------------68-----------------------------------')
# class man():
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def woman(self):
#         print(f'My name is {self.name}.send me email{ self.email}')
# mans=man('yukito','dsfew@fewa')
# mans.woman()

# print('------------------69-----------------------------------')

# class Good:
#     def __init__(self,dress,bad):
#         self.dress=dress
#         self.bad=bad

#     def myFunc(self):
#         x=10
#         y=20
#         print('hello my name is ',self.dress,self.bad)
#         print(x+y)
#         #もしここに追加したら一緒にプリントされる
# sei=Good('new dress ','Im wearing')
# sei.myFunc()

print('------------------70-------------------------------')
class Man:
    def __init__(self,hand,leg):
        self.x=hand
        self.y=hand

    def woman(self):
        print('part of body is',self.x)
        print('part of body is ',self.y)
        
        x='very big hand'
        y='very big leg'

        print('This is ',x)
        print('This is',y)

ok=Man('very big hand','very big hand')
ok.woman()
# print('------------------71-----------------------------------')
# #printing the content(value) from class based variable
# #クラスベースの変数からコンテンツ（値）を出力。

# class Emproyee:
#     id='fdssd'
#     name='huku'
#     def work(self):
#         print('my name is',self.name,'id is',self.id)

# emp=Emproyee()
# emp.work()

# print('------------------72-----------------------------------')
#example
#Counting the number of objects of the class
#例えば、クラスのオブジェクトを数える

# class School:
#     count=0
#     def __init__(self):
#         School.count=School.count+1

# s1=School()
# s1=School()
# print(School.count)
# s1=School()
# s1=School()
# s1=School()
# print(School.count)

# print('------------------73,74-----------------------------------')
#inheritance
#継承

# class Culation1:
#     def summation(self,a,b):
#         return a+b
# class Culation2:
#     def friend(self,a,b):
#         return a*b
# class Derived(Culation1,Culation2):
#     def total(self,a,b):
#         return a/b

# ok=Derived()
# print(ok.summation(50,50))
# print(ok.friend(10,5))

# class Father:
#     def papa(self,name,profession):
#         print('Im',name,'Im',profession)
#         return name,profession
        
# class Mather:
#     def mama(self,adress,email):
#         print('I stay in',adress,'send me message',email)
#         return adress,email

# class Son(Father,Mather):
#     def man(self,password,number):
#         print('My passward is',password,'Phone number',number)        
#         return password,number

# family=Son()
# family.papa('sei','lower')
# family.mama('Bangrole','iooj@gmail.com')
# family.man('greatIndia','1234566')

