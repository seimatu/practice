# We have a class defined variables.
#Exercise
'''We have a class defined for  vahicles.Create new vahicles called car1 and car2. 
Set car1 to  be a red convertible worth $60,000,000 with a name of Fer, and car2 to be a blue
van named Jump worth  $10,000,000. 
'''
# class Car:
#     def car1(self,name,Type,color,price):
#         print('This car is',name,'type is',Type,'and',color,'also',price)
#         return name,Type,color,price
#     def car2(self,name,Type,color,price):
#         print('This car is',name,'type is',Type,'and',color,'also',price)
#         return name,Type,color,price


print('--------------------------------------------')

# class Car:
#     def car1(self,name,Type,color,price):
#       self.name=name
#       self.Type=Type
#       self.color=color
#       self.price=price

#     def car1(self,name,Type,color,price):
#       self.name=name
#       self.Type=Type
#       self.color=color
#       self.price=price

#     print('This car is',name,'type is',Type,'and',color,'also',price)

# toyota=Car()
# toyota.car1('Fer','set','red','$60,000,000')

print('-----------------anther---------------------------')
class Vehical:
    name=''
    kind='car'
    color=''
    value=''

    def description(self):
        desc_str=("%s is a %s %s worth $%.2f"% (self.name,self.color,self.kind,self.value))
        return desc_str

        #instence
car1=Vehical()
car1.name='Far'
car1.kind='convertible'
car1.color='red'
car1.value=60000000
print(car1.description())
