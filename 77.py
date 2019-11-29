class Future:
    fun='vety nise day'

    #creating a class level object

    def __init__(self, name, age,game,system):
        self.name=name
        self.age=age
        self.game=game
        self.system=system
    
    def object(self):
        return f'{self.name} is ==>{self.age}'

instance=Future('lohit',20,'baseball','linear-system')

print(f'Name is : {instance.name}')
print(f'Name is : {instance.age}')
print(f'Name is : {instance.game}')
print(f'Name is : {instance.system}')

print('---------------------')
#im_writing "cla"
