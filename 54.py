
def names(dictionary):
    for key,value in dictionary.items():
        print(f'At spiceup {key} is headled by {value}')

assingment={}

while True:
    program=input('enter the name of programming languge :')
    student=input('enter the student name : ')
    assingment[program]=student
    another=input('do you want to add one more item (y/n) :')

    if another=='y':
        continue

    else:
        break
names(assingment)