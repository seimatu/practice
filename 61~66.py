# print('------------------61-----------------------------------')
#class in the python oop
#pythonのobject指向のクラス
#oopとはobject orient programming

# class program():
#     something='laptop'

# instance=program()
# print(instance.something)

# print('------------------62-----------------------------------')
#create a class named Gender , Use the __into__() function to  assign values
#for name and age etc
#Genderというクラスを作成し、__into__()の関数を使用して関数を割り当てます。

# init intialize / started
#初期化と開始

# class Gender():
#     def __init__(self,name,age,price,mail):
#         self.name=name
#         self.age=age
#         self.price=price
#         self.mail=mail
# instance=Gender('kazuo','35','India','E-mail@gmail.com')

# print(instance.name)

# print('------------------63-----------------------------------')
#object methds
#objects can also contain methods.
#methods are kind off functions
#the functions belongs to the class
#オブジェクトにはメソッドも含めることができます。
#メソッドは関数の一つです。
#関数はクラスに属します。

# class Subject():
#     def __init__(self,name,language):
#         self.name=name
#         self.language=language
        
#     def value(self):
#         print('my name is',self.name)
#         print('my mejer is ',self.language)


# instance=Subject('kaito','python')
# print(instance.name)
# instance.value()

# instance1=Subject('kodai','php')
# print(instance1.name)
# instance1.value()

# print('------------------64-----------------------------------')
'''
the self paramerter is a refernce to the current instance of class ,
and is used to acces variable that belong to tha class

It does not have to be name self ,
you can call it anything you want to call.

BUt it has to be first parameter of any function in the class
自己パラメータは、クラスの現在のインスタンスへの参照です。
クラスに属する変数にアクセスするために使用されます

selfという名前である必要はありません。
好きなように呼び出すことができます。

ただし、クラス内の関数の最初のパラメーターである必要があります
'''
# class deta:
#     def __init__(call,name,age):
#         call.name=name
#         call.age=age

# function=deta('huku',21)
# print(function.age)

# print('------------------65-----------------------------------')

# class Pets:
#     def __init__(ok,color,age,kind):
#         ok.color=color
#         ok.age=age
#         ok.kind=kind
    
#     def myFunction(animals):
#         print('my pets color ',animals.color,' age ',animals.age,'kind',animals.kind)

# instance=Pets('red','7','cat')
# instance.myFunction()

print('------------------66-----------------------------------')

class Holiday:
    def __init__(self,friend,hoby,time):
        self.friend=friend
        self.hoby=hoby
        self.time=time

    def off(self):
        print('I spend time ',self.friend,' We enjoyed ',self.hoby,' at ',self.time)

last_weekend=Holiday('lohit','gutter','11 oclok')
last_weekend.off()

