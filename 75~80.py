# print('------------------75-----------------------------------')
# class Car:
#     def __init__(self,name,type,color,price):
#         self.name=name
#         self.type=type
#         self.color=color
#         self.price=price

# mycar=Car('sei','toyota','red',6000000)
# print('name is ',mycar.name,'type is ',mycar.type,mycar.color,mycar.price)

# car1=Car('daiki','tesra','blue',1000000)
# print('name is ',car1.name,'type is ',car1.type,car1.color,car1.price)

# print('----------------76------------------------------------')
# class Water:

#     name='lohit'
    
#     def fire(self,name):
#         self.name=name
#         print('I am ',name)

# water=Water()
# print(water.name)

# water.fire('sei')


# water.name='sei'
# print(water.name)

# print('----------------77------------------------------------')
# #creating a class level object
# #クラスレベルのオブジェクト作成。

# class Man:
#     def __init__(self,name,age,adress,hoby):
#         self.name=name
#         self.age=age
#         self.adress=adress
#         self.hoby=hoby

#     def person(self):
#         return f'{self.name} is {self.adress}'

# newman=Man('hideto',20,'Tokyo','cook')
# print('Name is : ',newman.name)
# print('Age is : ',newman.age)
# print('Adress is : ',newman.adress)
# print('Hoby is ',newman.hoby)

# print('----------------78------------------------------------')

# class Planet:
#     word='carcl'

#     def __init__(self,water,arth,):
#         self.water=water
#         self.arth=arth
#     def jupiter(self):
#         return f'Do you have water? {self.water} You have {self.arth}'

#     @classmethod
#     def marz(cls):
#         return f'All the planet {cls.word}'

# land=Planet('yes','ear')
# print(Planet.word)
# print(Planet.marz())
# print(land.jupiter())

print('----------------79------------------------------------')
class Earth:
    country='Japan'
    city='Tokyo'

    def __init__(self,city,place):
        self.city
        self.place=place
    def con(self):
        return f'{self.country} is not effetcd by {self.city}'

    @classmethod
    def load(cls):
        return f'{cls.city} is great city,also {cls.place}'

planet=Earth('Bangarole','colamangara')
print(Earth.country)
print(planet.cls)
print(planet.con())