# area of circle
#円の面積。

# def area(ra,pai):
#     return (ra*2*pai)

# x=area(2,3.14)
# print(x)


# def trle(base,hei):
#     return (base*hei/2)

# x=trle(4,8)
# print(x)

# #selfmiss
# def number(num):
#     return (num*(!))

# x=number(6)
# print(x)

print('------------------------------------------------')


def fact(x):
    if x==0:
        return 1

    return x*fact(x-1)

x=int(input('enter the values for x'))
print(fact(x))    
    