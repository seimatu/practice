
# def person(dictionaly):
#     belts=list(dictionaly.values())

#     for belt in belts:
#         num=belt.count(belt)
#         print(f'There are {num} {belt} belts')


# lohit_items={}

# while True :

#     lohit_belt=input('enter the name of belt :')
#     lohit_belt_color=input('enter the color of belt :')

#     lohit_items[lohit_belt]=lohit_belt_color
#     another=input('enter another item (y/n)')

#     if another =='y':
#         continue
#     else:
#         break

# person(lohit_items)

print('-----------------------------------------------------')

def person(dictionaly):
    animal=list(dictionaly.values())

    for animl in animal:
        num=animl.count(animl)
        print(f'there are {num} {animl} pets')



pets={}

while True:
    Your_pet=input('enter the name of pet :')
    Your_pet_color=input('enter the color of pet : ')

    pets[Your_pet]=Your_pet_color
    another=input('enter another item (y/n)')

    if another =='y':
        continue
    else:
        break

person(pets)



    


