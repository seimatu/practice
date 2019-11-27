#create a class named Gender , Use the __into__() function to  assign values
#for name and age etc
#Genderというクラスを作成し、__into__()の関数を使用して関数を割り当てます。

# init intialize / started
#初期化と開始

class Gender():

    def __init__(self,name,age,programm,health):
        self.name=name
        self.age=age
        self.programm=programm
        self.health=health
variable=Gender('sei',25,'python','so-so')

print(variable.name)


class Teath():

    def __init__(self,wacth,belt):
        self.wacth=wacth
        self.belt=belt
isinstance=Teath('casio','black')

print(isinstance.wacth)