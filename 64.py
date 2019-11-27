#self pramerter
'''
the self paramerter is a refernce to the current instance of class ,
and is used to acces variable that belong to tha class

It does not have to be name self ,
you can call it anything you want to call.

BUt it has to be first parameter of any function in the class
'''

class Subject:
    def __init__(anything,working, salary):
        anything.working=working
        anything.salary=salary

    def mywork(anything):
        print('if you work as', anything.working,'you get payed',anything.salary)

create=Subject('python developer','very good salary')
create.mywork()

print('-------------------------------------------------------')
#selfじゃなくとも大丈夫
class Countrys:
    def __init__(call,nashonal,area):
        call.nashonal=nashonal
        call.area=area

    def born(call):
        print('I am from',call.nashonal,'my city is',call.area)

create=Countrys('India','banglore')
create.born()
