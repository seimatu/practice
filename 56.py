

# def simple_interest(p,t,r):
#     return(p,t,r)/100

# print(simple_interest(p=100,t=10,r=10))

print('-----------------------------------------------------')

#simple_interest(p,t,r)
#formulea
#simple Interest = (principal)*(rate)*(# of periods)



def simple_interest(p,t,r):
    return(p*t*r)/100
    

p=float(input('enter the p number :'))
t=float(input('enter the t number :'))
r=float(input('enter the r number :'))



print(simple_interest(p,t,r))

