#object methds

#objects can also contain methods.
#methods are kind off functions
#the functions belongs to the class

class subject():

    def __init__(self,language,greet):
        self.language=language
        self.greet=greet

    def Mydialog(self):

        print('I can speak',self.language)
        print('I can speak',self.greet)

    def Mydialog1(self):
    
        print('I can speak',self.language)
        print('I can speak',self.greet)
    

instance=subject('English','good Moning Guys')
print(instance.language)
instance.Mydialog1()


instance1=subject('japanese','good Moning Guys')
print(instance1.language)
instance1.Mydialog1()



print('-----------------------------------------------')
