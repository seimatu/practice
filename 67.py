class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def myFun(self):
        print('hello my name',self.name)

sei=Person('sei',200)
print(sei.name)
sei.myFun()

sei.name='lohit'
print(sei.name)
sei.myFun()

sei.age='300'
print(sei.age)
sei.myFUn()

#delete item 
print('--------------------------')
del sei.name
print(sei.name)


