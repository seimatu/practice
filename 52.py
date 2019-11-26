# volume
# 球
# def volume(area):
#     return (area*length)

# radians=(input('enter the radius : '))
# length=(input('enter the length : '))

# area=radians*radians*3.14
# volume=area*length

# print(volume(area,length))



print('-------------------------------------------------')
#anser

def area(radius):
    return 3.14* radius*radius

def volume(area,length):
    print(area*length)

radians=int(input('enter the radius :'))
length=int(input('enter the length :'))

volume(area(radians),length)
